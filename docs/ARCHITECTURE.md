> 2026-11-13: [reference updates](REFERENCE-UPDATES.md) add a source-verified
> Wowhead adapter, retained source evidence and a small current-reference pointer.
> The landing page imports only identity/label metadata, keeping class data and
> encoding registries lazy. Legacy routes and experiments remain pinned.

# Current ruleset architecture

The calculator resolves `(ruleset ID, revision, class)` in
`web/src/data/rulesets.ts`, returning an immutable class dataset, scoped encoding
registry, pinned baseline and computed custom changes. Bare legacy links select
the retained original baseline; reference correction/review pages still use
`data/talents/`. New baseline files do not alter retained experiment pins.

`url/route.ts` and `url/import.ts` retain ruleset/revision. `ClassPage` uses the
identity in loading, editing/history keys, imports and last-build storage.
`RulesetPanel` provides switching and before/after investment details. Its
experiment context gives cells and tooltips custom badges/intent while keeping
reference confidence/Classic comparisons separate. Full links, text export,
print, embed and continue retain identity; experiment bare codes are disabled.

`pipeline/validate_rulesets.py` reuses reference structural checks without global
export/encoding assumptions. It validates manifest/schema, pins, classes, assets,
hashes, per-change intent and local frozen orders. CI rejects modifications to
already-published revisions using the PR base. `pipeline/ruleset.py` creates and
seals new untracked revisions. See [authoring](RULESETS.md) for exact commands,
contracts and supported rules. Stack and static deployment are unchanged.

The implementation adds an experimental class schema to allow manual designs
with zero observed ranks; it does not reinterpret designs as game observations.
Reference class schema and the pure legality engine are unchanged. Extra trees,
exclusions and hard cross-tree requirements remain later work.

The original inspection below is retained as a dated account of the starting
point, not a description of the new runtime. Validation results for the current
implementation are in the [implementation handover](handover/2026-11-12-rulesets.md).

---

# Original architecture inspection (2026-11-10)

Inspected at commit `0bc85aa239c2dfca79345986db07b57ccd7aaa9b` on 2026-11-10.
This describes implemented behavior; proposals live in the
[requirements](briefs/experimental-rulesets.md) and [plan](plans/experimental-rulesets-v1.md).

## Data to calculator

| Area | Current behavior and source |
| --- | --- |
| Reference contract | `docs/DATA-SCHEMA.md`, `data/schema/class.schema.json`; plain TS in `web/src/data/schema.ts`, Zod in `schema.zod.ts`. JSON Schema rejects unknown properties; Zod uses loose objects. |
| Extraction/corrections | `pipeline/stages/08_export.py` and `src/wowtalents/export.py` promote extracted data plus overrides into `data/talents/`; reference provenance is retained. Experiments must not enter this path. |
| Loading | `web/src/data/load.ts` lazily globs `data/talents/*.json`, keyed/cached by class only. With `VITE_INCLUDE_EXAMPLES=1`, examples and fixtures join at lower precedence. Zod parsing runs in development; production trusts prior validation. No ruleset catalog exists. |
| Generated data | `web/scripts/gen-data-index.mjs` and `gen-classic-index.mjs` write committed indexes, facts and Classic comparisons. Vite's dev plugin regenerates data indexes; builds/tests do not silently regenerate them. `generated.test.ts` compares temporary generated output. |
| Rules | `web/src/rules/{types,points,validate,mutate}.ts`: `Build` is tree → talent → rank. Total budget, optional page budgets, row gating using points strictly above the row, max ranks, and AND prerequisites. `canRemove` simulates removal; `sanitize` removes invalid ranks. `resetTree` simply deletes a tree, safe today because prerequisites are local. |
| Rendering | `App.tsx` routes lazy pages; `ClassPage.tsx` loads/decodes, manages history, URL writes and saved builds. `TreePanel.tsx` uses declared rows/cols, one keyboard grid per tree, a tier gutter and local arrows. Panels wrap with flex layout in `calculator.css`. |
| Links | `url/codec.ts` takes an encoding registry, writes one decimal digit per talent, trims trailing zeros and joins tree segments with `-`. `data/encoding.ts` eagerly loads version orders/migrations; lookup uses numeric version and class, not ruleset. Decode migrates, clamps and sanitizes with notices. |
| Related state | `url/route.ts` parses `v`, `t`, `sel`, `embed`; empty builds omit `v/t`. `url/import.ts` handles own links, bare codes and Wowhead mapping. `ui/storage.ts` stores one last build with class/version/code; `ClassPage`, `summaryText.ts`, `ImportDialog` and print/embed consume these identities. |

No ruleset identity or custom-versus-reference comparison is implemented.
The existing “new”/Classic-diff display compares against Classic Era, not against
an experimental baseline; extraction confidence describes evidence, not design quality.

## Boundaries verified in code

- The schema caps ranks at 9 (single digit). Talent IDs are unique within a
  class; cells are unique per tree. Rank arrays must match max rank.
- `requires` accepts 1–3 entries. Python validation and Zod require targets in
  the same tree, same or earlier row, another cell, a satisfiable target rank
  and no cycles. Rules, arrows and nested tooltip lookup also assume same tree.
- Trees are arrays, not a hard-coded triple. Pages are limited to `primary`
  and `secondary`. Arbitrary tree counts are not a verified product capability:
  layout, print, summaries, page budgets and link orders must be checked.
- No exclusion groups, OR prerequisites or cross-tree investment thresholds exist.
- Current reference classes use 51 points. `pointsPerRow`, levels and budget
  are data-driven, not globally fixed constants.
- `data/encoding/v1.json` is **`frozen: false`**, and old docs explicitly allow
  mutation before launch. This fork's compatibility goal is stricter. A future
  approved implementation must capture the present order and freeze its
  meaning; rewriting historical links cannot recover already lost semantics.

## Checking changes

Use commands in [AGENTS.md](../AGENTS.md). CI is `.github/workflows/deploy.yml`:
Python tests and all three validators; web generation/diff, typecheck, Vitest,
Playwright production build/preview. `npm run build` is not the whole CI suite.
CI's deployment job publishes on main pushes; do not push/trigger deployment
as part of planning. Build output stays in ignored `web/dist/`.

For reference corrections follow [CONTRIBUTING.md](../CONTRIBUTING.md).
For sandbox work: requirements → written plan → review/revision → explicit
approval → small implementation changes with tests. Approval covers routine
fixes and implementation choices within scope. Material rule/scope changes
return to review. New game mechanics/numbers need design approval separately;
synthetic fixtures can test plumbing without endorsing a playable design.

## Validation of this documentation change

On 2026-11-10: Vitest **575 passed** (27 files), pytest **571 passed**,
production build/typecheck passed, and talent/race/spell validators exited 0.
Validators retain warnings about reference data; these are not balance checks.
No runtime code, dataset, schema or encoding was changed. Browser tests were
not rerun for this documentation-only change. In the preceding setup run,
92 passed using system Chromium through an external config; downloading
Playwright's managed Chromium was denied at `cdn.playwright.dev`. The standard
browser installation path remains a setup limitation, not a test success here.
