---
name: update-reference
description: Check Wowhead Forever for updated talent trees, prepare and validate a reproducible reference snapshot, and deliver the update without rebasing existing experiments or changing legacy links.
---

# Update the Forever reference

Use the existing checkout; cloud tasks are isolated. Do not create a worktree
unless the user explicitly asks. Read `AGENTS.md` and `docs/REFERENCE-UPDATES.md`.
Keep reference updates separate from custom designs and from corrections to the
original video dataset. Never edit an existing retained revision or its assets.

## Fetch and inspect

From `pipeline/` run:

```bash
uv run --frozen python update_reference.py fetch
```

Use the absolute bundle path printed by that command in subsequent commands.
The adapter discovers the public data script from the actual Forever page,
checks the environment/revision and caches bytes and hashes. It does not require
an API key. Do not execute the downloaded JavaScript. Do not guess a URL, fall
back to Classic, bypass access restrictions or invent missing ranks/values.
If the request or adapter fails, retain the last valid reference and report the
specific failure. Investigate schema drift with the saved response before
changing the parser; add an offline regression fixture for the discovered case.

```bash
uv run --frozen python update_reference.py prepare --bundle <absolute-bundle-path>
```

Read `diff.md` and `source-issues.json` in the bundle. Confirm all nine classes,
27 supported class trees, complete rank descriptions, same-tree prerequisites,
compatible tier gating and the shared 51-point sandbox budget. The report matches
by name; a rename may appear as an addition/removal. Stable imported talent IDs
are derived from Wowhead IDs, not names. Known unresolved source formulas are
retained verbatim and marked, never numerically filled in. Unknown variables,
new rule fields or unsupported structures must fail rather than disappear.

## Add a new retained snapshot

When the candidate is coherent, from `pipeline/` run:

```bash
uv run --frozen python update_reference.py publish --bundle <absolute-bundle-path>
uv run --frozen python validate_rulesets.py
uv run --frozen pytest -q
```

`publish` here only writes repository files and the current-reference pointer;
it does not deploy the site or publish a cloud environment. The command is
idempotent for the same source identity. It must never rewrite a retained revision,
old reference file or existing icon. Check `git diff` and `git status`.

From `web/` run `npm test`, `npm run build` and the relevant Playwright cases
(`npm run e2e` for a full suite). Check current-reference navigation, source/date
labels, one allocation/share/reload, the old baseline link regression and the
existing Shaman experiment pin. Validate retained content against the fetched PR
base with `validate_rulesets.py --base <base-sha>`.

Create a PR with source URL/version/data revision/retrieval date, change totals,
known source issues and validation evidence. Merge when CI succeeds under the
owner's standing autonomous-development authorization. If the source already
has a retained identical snapshot and the current pointer is unchanged, do not
create an empty PR or touch timestamps to manufacture a change.

## Report accurately

Call the result “last imported from Wowhead”, not verified live game state.
Wowhead may lag hotfixes and its website data interface is not a stable API
contract. Do not claim the full client build number from unrelated calculators.
Old links and experiment revisions keep their original snapshots. A source
update does not automatically rebase, rebalance or migrate any custom design.
