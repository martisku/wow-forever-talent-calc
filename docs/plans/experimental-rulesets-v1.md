# First release: repository-authored rulesets

Status: **implemented under autonomous-development authorization (2026-11-12)**.
See [current authoring contract](../RULESETS.md). The design below records the
original release plan; shipped paths use `data/rulesets/<id>/r<N>/` for both kinds.
The owner delegated design choices, PRs and merging; the first Shaman study is
explicitly exploratory rather than an approved balance conclusion. [Requirements](../briefs/experimental-rulesets.md) define the
goal; [architecture](../ARCHITECTURE.md) records the inspected baseline and limits.
Paths and URL parameters below are proposals, not implemented interfaces.

## Recommendation and scope

Ship immutable baseline snapshots and complete class datasets for each supported
experiment revision. Reuse the existing `ClassData` shape and allocation engine;
add a small ruleset manifest, scoped loader/encoding context and experiment UI.
Start with the current 51-point rules and existing tree/page structure. Verify
with synthetic fixtures, then publish playable designs only after content review.

| Approach | Advantages | Cost and failure modes |
| --- | --- | --- |
| Complete datasets pinned to a baseline | Existing class types and rendering can consume them; explicit effective state; deterministic load; no patch interpreter; easy to retain revisions. | Duplicates unchanged talent data; larger diffs. A computed comparison and intent notes must catch unexplained changes. Baseline updates require deliberate copying/review, not inheritance. |
| Patches against a pinned baseline | Concise change lists; naturally describe adds/removes/moves. Pinning can make them reproducible too. | Needs operation ordering, field/unset semantics, conflict and dangling-reference detection, materialization and validation. Rebase tooling is still needed when the pin changes. Mistakes can leave partial datasets. |

Complete datasets are simplest at this scale. Only copy supported classes into
an experiment, not all classes or image assets. Store intent in the manifest;
compute the structural diff against the pin instead of maintaining an unverified
second change list. If authoring duplication later becomes costly, patches may
be an authoring tool that emits the same validated datasets; no generic patch
system in v1.

## Existing capabilities to reuse

- Pure `rules/` already handles budgets, tier gating, same-tree prerequisites,
  max ranks, refusal messages and sanitization. No new legality operators in v1.
- `ClassData`, grid placement, rank text and local arrows express additions,
  removals, moves and changed rank counts. Updated ranks/descriptions must remain
  consistent; rows/columns cannot collide.
- `url/codec.ts` accepts a registry and already supports explicit digit ordering,
  migration and notices. Reuse it with an isolated registry; do not merge an
  experiment into the current global numeric version map.
- Lazy data imports, build summary, keyboard/touch interactions and static base
  paths remain. Extend their identity plumbing rather than rebuilding the app.
- Existing tests cover schema parity, data structure, generated freshness,
  allocation, codec migrations, routing/imports, storage/history and browser UX.

## Proposed storage and schemas (R1–R3, R8–R9)

```text
data/rulesets/
  baselines/reference-<id>/
    manifest.json          # identity, source commit, file/asset hashes
    classes/<class>.json   # all current reference classes at capture
    encoding/…             # captured versions and required migrations
  experiments/<id>/r1/
    manifest.json          # id, revision, name, baselineId, classes, intent
    classes/<class>.json   # complete effective data for supported classes
    encoding/v1.json       # local, immutable order for these classes
```

A manifest schema uses explicit `kind` (baseline or experiment), manifest format
version, identity and supported class list. Experiment manifests require a pinned
baseline ID, overall design intent and per-change intent keyed by talent ID;
removals can reference the baseline ID of the removed talent. A moved/modified
record can have multiple computed change labels. Include tree-level intent if
tree metadata changes. Reject unexplained semantic differences and stale intent
entries; omit purely mechanical serialization/timestamp fields from the semantic
diff. Use `source.kind: manual`, `dataSource: manual` where appropriate for custom
records; do not copy video confidence as evidence for a new design. Preserve
unchanged records and their provenance. A source-review flag is not design approval.

Keep reference schema v1 intact. Add an authoritative JSON Schema for the manifest
and corresponding TS/Zod types; use strict manifest validation (Zod's current
loose class mirror alone will not catch misspelled custom rule keys). Reuse class
shape validation, supplementing it with the existing structural constraints:
unique class-wide talent/tree IDs, valid pages/orders/cells, bounds, rank/slot
lengths, prerequisites/cycles and required sources/assets. Reject unknown class
fields with the authoritative class JSON Schema in the validation path. Validate
manifest ↔ class ↔ encoding coverage, each talent exactly once in its tree's
order, distinct id/revision keys, 51-point budgets and supported v1 structure.
Treat encoding and rank constraints separately: manifest revision, class schema
version and `dataVersion` are not interchangeable.

Do not run the reference validator unchanged on experiments: it assumes global
reference encoding and canonical export ownership. Extract/reuse only appropriate
checks or add a narrow experiment validator. No broad pipeline rewrite. Add a
required test/CI validation step that discovers every shipped ruleset and fails
on zero discovery. Production casts data rather than validating it on load,
so `npm run build` alone is insufficient.

Capture the baseline from the inspected commit (or explicitly record the new
commit if source changed before implementation), including current encoding
bytes and hashes of relevant assets. Keep `data/talents/` as the correction/export
path; do not repurpose it as writable design files. At initial implementation,
make the legacy default resolve to the captured reference and freeze v1's digit
meaning. Changing its `frozen` flag is a reviewed implementation action; it has
not happened in this documentation change. Future reference updates need new
baseline IDs and retained legacy decoding, not an overwrite of the default.
Hash checks enforce retained snapshot content in validation; CI should also
compare retained published revision files against the target branch to reject
rewrites, deletions or changed hashes disguised as the same revision. Git history alone
is insufficient: the static deployment must include revisions needed by old links.

## Loading and state (R4, R6–R8)

Add a small statically discovered catalog; load by `(rulesetId, revision, classId)`
and return the class plus its scoped registry, baseline and intent/diff context.
Cache by that whole identity. Do not fall back to reference files for unsupported
experiment classes. Keep example/fixture flags separate from public experiments.
Lazy-load class datasets; eager small manifest metadata is sufficient. No runtime
patch application or external service.

Thread identity through `App`, `ClassPage` props/effect dependencies/route keys,
history, imports, storage and all URL writes. Guard async loads against stale
class/ruleset results. Switching uses deliberate navigation, starts empty and
resets edit history; Back returns to the previous URL/build. Do not auto-sanitize
a baseline allocation into an experiment as part of switching. Same-ruleset
edits and imported malformed allocations retain existing notices/sanitization.

Use a separate last-build storage version or explicitly default legacy entries
to baseline. Never resume experiment points as baseline points. `sel` and `embed`
remain view state and must survive appropriate navigation without losing ruleset.

## URLs and compatibility (R6–R8)

Proposed experiment URL:
`#/shaman?ruleset=<slug>&rev=1&v=1&t=<digits>`.
`v` stays encoding version; `rev` selects an immutable experiment revision whose
manifest pins the baseline. Even an empty experiment keeps `ruleset` and `rev`.
Explicit baseline URLs can use their baseline catalog ID and revision; bare
legacy routes continue selecting the original captured baseline. No “latest”
alias in persisted links. Revision identity must precede decoding the digits.

An experiment-local encoding order may also be numbered 1; it must never enter
`loadRegistry()`'s global map (currently first entry for a version wins). Always
pass the selected registry and class together to encode/decode; prohibit derived
order fallback for published experiment data. New experiment revision = fresh
immutable context; no cross-revision migration required in v1.

Update `route.ts` round trips, `classHash`'s empty-build behavior, `url/import.ts`,
`ClassPage.applyImport`, summary copy actions/text, embed return links, printed
identity and saved/continue links. Full links are the authoritative portable
format. Preserve baseline bare-code and Wowhead import behavior; disable those
ambiguous formats while in experiments with an explanation and request a full
ruleset link. Disable experiment bare-code copying rather than suggesting digits
alone are reproducible. Never strip ruleset parameters from a pasted full link.
Unknown/malformed ruleset, missing/invalid revision, unsupported class or unavailable
encoding shows an actionable error before allocation; no baseline/latest fallback.
Keep existing baseline codec notices for invalid build strings and old versions.

Compatibility cannot recover links from earlier upstream rewrites of mutable
v1; acceptance covers the current captured interpretation and existing migration
fixtures. Add fixed baseline link fixtures before changing identity plumbing.

## UI and investment costs (R4–R5)

Provide a labeled selector for the active class's baseline and available experiment
revisions. Show ruleset name/revision and baseline label; retain custom identity
in compact embed and print. Explain switching resets the allocation before the
user switches. Do not render unsupported classes under an experiment label.

Compute additions/modifications/moves relative to the pinned baseline. Add text
badges, accessible labels and intent in tooltips/details; provide a small change
summary including removed talents and before/after rank/placement/prerequisite
changes. Use a separate presentation from the current Classic-new highlight.
In experiments, suppress reference-only trust/rank claims and misleading Classic
comparisons for custom records; reference review/races/spells pages remain clearly
reference-only. Never send a custom design to the upstream wrong-reading report
flow. No new general comparison dashboard in v1.

Keep the current spent/remaining total, tree totals, tier gutter and prerequisite
requirements/refusal explanations. Combined with change details and intent, these
show investment costs/tradeoffs. Do not promise an optimal-path cost solver,
DPS estimates or a balance score.

## Constraints and deferred mechanics

| Mechanic | Current constraint | First release / later work |
| --- | --- | --- |
| More branches, moves, ranks | Grid bounds and occupancy, ranks 1–9, rank text/arrays, local arrows. | Essential within existing trees. Validate effective dataset, not just changed cells. |
| Extra trees | Arrays and digit segments are generic; page IDs only primary/secondary; layout wraps. Print/summary/order assumptions need testing. | Keep v1 tree/page identities and counts equal to baseline. Later approve an extra-tree layout/progression, page budget policy, responsive/print tests and explicit encoding order. Never allocate extra points by default. |
| Cross-tree builds | Already spend the shared 51 across trees. Textual synergy is possible; no evaluation of its power. | v1 supports changed investments and descriptive incentives. Later cross-tree hard requirements need tree-qualified targets, class-wide graph validation, reset/refund/sanitize behavior, tooltip lookup and a legible alternative to local SVG arrows. |
| Exclusive talents | No schema or engine support. Ordinary prerequisites cannot express exclusion. | Later explicit named groups (at most one member with rank >0), class-wide enforcement on add/import/validate, deterministic sanitization, explanation and tests. Do not silently auto-refund one choice to buy another. |
| OR/generic mechanics | Existing prerequisites are AND, same/earlier row, at most 3. | Reject unsupported fields in v1. No rule DSL or balance simulator. |

## Reviewable change sequence and acceptance

Each step includes its tests; the owner authorized implementation on 2026-11-12. Do not combine
playable content design with infrastructure approval.

1. **Capture baseline and define contracts.** Add retained snapshot/manifests,
   hashes, explicit orders, strict validation and baseline link regression fixtures.
   Capture all current classes; freeze current link meaning. Use synthetic
   experiments only in tests covering add/edit/move/remove and changed rank count.
   Acceptance: hashes match the source capture, malformed data fails, all existing
   baseline tests/links retain current meaning, no reference correction/export
   path is redirected into experiments.
2. **Load and route exact revisions.** Add catalog/scoped cache/registry context,
   URL parsing and error states. Thread identity through imports, history,
   continue/storage, all sharing, print/embed. Acceptance: two revisions with the
   same class/encoding number decode independently; empty links retain identity;
   Back/Forward and full-link imports work; unknown identities never fall back;
   baseline links with no ruleset still pass fixtures. No playable experiment is
   enabled publicly until its content is reviewed.
3. **Expose switching and custom intent.** Add selector/active identity, computed
   change badges and removal summary, intent details and appropriate reference
   labels. Acceptance: keyboard/touch users can distinguish changes without color,
   see investment requirements, switch to an empty build and return via Back;
   custom data is not presented as observed or as a reference correction.
4. **Validate release end to end and document authoring.** Add production browser
   coverage using a test-only synthetic experiment, supported by a deliberate
   fixture flag so it does not masquerade as a published Shaman design. Document
   adding a revision, new-baseline retention and validator commands. Acceptance:
   after adding a newer baseline/revision, the old URL still resolves identical
   data/allocation; the app builds/loads under a non-root base path; all baseline
   and new checks pass. A first real experiment, if desired, is a separate content
   review with approved talents/values.

Relevant tests: extend schema parity/data validation with negative cases (duplicate
IDs/cells, missing targets, cycles, rank limits, broken pins/assets/order, unknown
properties and changed immutable revision); codec/route/import round trips and
malformed identities; storage/history isolation; diff classification including
removals; production Playwright for switching, editing, sharing/reload, empty
builds, print/embed identity and the baseline-update reproduction case. Retain
existing pure-rule tests and test 51-point enforcement for experimental classes.
No trivial tests that only mirror manifest getters.

## Review decisions

The recommendation is complete datasets, immutable captured legacy default,
existing rule semantics only, and synthetic infrastructure fixtures before any
playable content. The owner’s standing authorization now covers implementation and iteration.
The first release ships a clearly marked Shaman design study so the sandbox is
usable immediately; this supersedes the original test-only demonstration scope. If cross-tree hard gates, exclusive choices or a fourth tree
must be in the first release, revise and review scope before coding. Specific
Shaman talents and values remain unapproved and can be decided separately.

## Shipped implementation notes

Complete datasets, retained hashes, append-only PR validation, scoped loading,
revision-aware URL/import/history/continue handling, switching, change intent and
repository authoring commands are implemented. A separate experimental class
schema permits zero observed ranks for manual designs; the reference schema is
unchanged. Synthetic and real-data tests exercise isolation and retention.
Cross-tree hard gates, exclusions and extra trees remain deferred.
