# Authoring experimental talent trees

The sandbox supports complete class datasets pinned to immutable reference
snapshots. A ruleset is `(id, revision)`; numeric encoding versions are local to
that revision. No patches, editor, simulation or automatic rebasing is involved.

## Try it

Run the site from `web/` with `npm run dev`. Choose Shaman, then select
**Shaman investment study · revision 1** in the Ruleset control. The draft
includes a relocated talent, reduced rank investment, a removed option and
Totemic Relay, a prototype healing/damage weaving incentive. These are design
proposals, not official data or a claim of balance. The shared pool stays at 51.

Custom cells have text badges. Their tooltips explain intent. “Design changes”
lists before/after investment details and removals. Switching starts an empty
build; Back returns to the old build. Copy the full link to share a revision;
bare build codes deliberately cannot identify an experiment. Reference-only
review, race, spell and Classic comparison pages remain separate.

## Create a design or revision

Run these from `pipeline/`. Start from either the reference baseline or another
experiment. This command copies one supported class; it never overwrites a target.

```bash
uv run --frozen python ruleset.py create \
  --from-id shaman-investment-study --from-revision 1 \
  --id my-shaman --revision 1 --name 'My Shaman study' --class shaman
```

To start unchanged, use `--from-id reference-2026-11-10`. To revise your own
experiment, copy its last revision to the same ID with a new positive revision.
An old link always retains its old content; there is no “latest” alias.

Edit the new files under `data/rulesets/<id>/r<N>/`:

1. `manifest.json`: name, overall intent and `changes.<class>.<talent-id>` notes
   for every added/modified/moved/removed talent. Include removed IDs; omit stale
   notes. Pin the baseline explicitly. A copy of an experiment retains its pin.
2. `classes/<class>.json`: the complete effective class, not a patch. Preserve
   unchanged records. Custom records use `source.kind: manual`,
   `source.reviewed: false`, `ranksSource: manual`, `ranksObserved: []` and a
   `ranksNote` explaining authored effects. Do not invent observed confidence.
   Supply all designed rank values and keep `ranks.length == maxRank`.
3. Run `seal` **before `git add`** to generate explicit digit order and hashes.
   You can repeat it while the new revision remains untracked, then validate:

```bash
uv run --frozen python ruleset.py seal --id my-shaman --revision 1
uv run --frozen python validate_rulesets.py
uv run --frozen pytest -q
# in web/
npm test
npm run build
npm run e2e
```

Stage and commit the manifest, class and encoding together. After tracking or
publishing, create a new revision instead of resealing. The validator checks
that intents match computed differences, encoding covers the effective dataset,
assets exist and hashes match. PR CI compares with the target branch and rejects
rewritten/deleted revision files or assets retained by older revisions.

## Contract and limitations

- `data/schema/ruleset.schema.json` is the strict manifest contract;
  `experimental-class.schema.json` mirrors the reference class schema except
  that manually authored designs may have no observed ranks. The reference
  schema itself is unchanged. TS types remain in `web/src/data/schema.ts`.
- Class IDs/talent IDs, unique cells, rank limits 1–9 and prerequisite cycles
  are validated. V1 retains the baseline's rules, page and tree metadata.
  Requirements are AND, same tree, same/earlier row, at most three targets.
  Cross-tree hard prerequisites, exclusion groups, OR rules and extra trees
  are future work. Shared-budget cross-tree allocations already work.
- Runtime loading uses a separate cache and encoding registry for each complete
  identity. Production relies on mandatory Python/CI validation; build alone
  is not sufficient. Development also parses class shapes with Zod.
- Full links use `#/shaman?ruleset=my-shaman&rev=1&v=1&t=...`; empty experiment
  links keep `ruleset/rev`. Existing links without those fields retain the
  original captured reference semantics. Malformed/unavailable identities
  never silently become another ruleset. Old baseline migration notices remain.
- Manifests retain hashes of class data, encoding and shared image assets.
  Keep those assets unchanged or give new art a new filename. Retention is
  required in the deployed static files; Git history by itself is insufficient.

## Updating reference data

For the current automated Wowhead import, see [reference updates](REFERENCE-UPDATES.md)
and the repository [update-reference skill](../.agents/skills/update-reference/SKILL.md).
The class picker follows `data/current-reference.json`; legacy routes stay pinned.

`data/talents/`, extraction, overrides and promotion remain the reference
correction workflow. They do not write into retained snapshots. Legacy calculator
links resolve to `reference-2026-11-10` revision 1, captured from commit
`0bc85aa239c2dfca79345986db07b57ccd7aaa9b`; current `data/encoding/v1.json` is now
frozen without changing its talent positions. Earlier upstream rewrites cannot
be reconstructed from an already ambiguous link.

A future reference update must add a new baseline directory/identity, capture
all classes and required encoding/migrations, record the source commit, and
hash all retained files/assets. Leave old snapshots deployed. An experiment
moves to that baseline only in a new revision with reviewed changes and new
hashes. Do not point existing experiment pins or bare legacy routes at new data.

## Development ownership

The owner authorized autonomous implementation, PR creation and merging on
2026-11-12. Make small tested changes, retain reviewable plans and report remote
access/CI blockers accurately. Do not bypass branch protection or claim a merge
or deployment that has not been verified.
