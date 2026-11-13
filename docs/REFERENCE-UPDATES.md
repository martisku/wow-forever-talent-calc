# Updating the current reference from Wowhead

The class picker opens the last imported reference; each link identifies the
retained snapshot explicitly. The source, version and retrieval date appear in
the calculator. This is publisher data, not a claim of verified live game state.

## Source and alternatives

On 2026-11-13, the public Forever calculator page exposed environment 16, version
`1.60.1` and a cache-versioned script at
`https://nether.wowhead.com/forever/data/talents-classic?dv=34&db=1794343902`.
It contained all nine classes, 27 trees and 467 talents with names, grid positions,
prerequisites and complete per-rank descriptions. No API key was required.

The adapter discovers the URL from [the actual calculator page](https://www.wowhead.com/forever/talent-calc/shaman),
not a hard-coded cache revision. It decodes the JSON argument to
`WH.setPageData("wow.talentCalcClassic.classicplus.data", …)` without running JS.
It verifies that page metadata and data revision agree, requires the supported
class/tree mapping, and rejects missing ranks and unsupported rule changes.
The interface is used by the website itself; it is not a documented supported API.
A failure leaves the last valid reference in place. Never substitute Classic
placeholder data just to make an update succeed.

The existing wago.tools DB2 importer remains available for a suitable identified
client build; the build-list endpoint returned HTTP 403 in this environment during
research. The public Blizzard documentation page did not establish an available
Forever talent-tree API. Neither result proves that no other API exists.

## Run an update

Use the repository skill **[update-reference](../.agents/skills/update-reference/SKILL.md)**,
or run these commands from `pipeline/`:

```bash
uv run --frozen python update_reference.py fetch
uv run --frozen python update_reference.py prepare --bundle <absolute-path-printed-by-fetch>
# Inspect <bundle>/diff.md and <bundle>/source-issues.json.
uv run --frozen python update_reference.py publish --bundle <absolute-bundle-path>
uv run --frozen python validate_rulesets.py
uv run --frozen pytest -q
```

Then run the web tests/build/browser checks and deliver the changes by PR.
`publish` writes repository files, not a cloud environment or a website deployment.
There is no unattended schedule or browser-time network dependency. The skill can
be invoked whenever a check is wanted. Identical source input reuses the retained
snapshot; a check without changes should not create a PR.

Fetch stores raw source evidence under ignored `pipeline/work/wowhead-reference/`.
Prepare regenerates candidates from verified bytes, validates the class contract,
writes the name-matched difference report, and downloads only missing icons,
sequentially at at most two requests/second. Per-rank spell IDs preserve the
publisher's repetitions; rank effects come from `descriptions`, not guessed
interpolation. A rename can appear as an addition/removal in the report.

Publish records:

- Complete class files and a local frozen encoding registry under a new
  `data/rulesets/wowhead-forever-<revision>-<hash>/r1/` directory.
- Original calculator data, discovery metadata, change report and source issues.
- Provider URL, version, upstream data revision, retrieval time and checksums.
  `sourceCommit` identifies the importer code at snapshot creation; the source
  data itself is identified by its retained response hash.
- Retained icon hashes. Existing assets are reused without being overwritten.
- A small mutable `data/current-reference.json` pointer for the class picker.

The importer validates the result before updating that pointer. Failed publication
rolls back only files created by that invocation. CI validates the pointer,
source evidence, all snapshots and immutability relative to the PR base.

## Source limitations

Full rank descriptions do not imply that all values have been verified in game.
Some depend on level/stats and the publisher may lag hotfixes. The first import
has one known unresolved formula in **Death Mark** (`$mcrit`). It is preserved
verbatim and marked in its cell, tooltip and source-issues report. The adapter
fails on unknown formula variables instead of guessing their values. HTML and
calculation comments are converted to the visible text; the original is retained.

The 51-point budget, level relationship and five-point tier gates remain the
calculator's supported rule model. Incompatible source rules require an explicit
adapter/engine change rather than silently being approximated. This is not a
combat simulator or a balance verifier.

## Compatibility

Bare legacy routes and links continue selecting the original captured baseline.
Current-reference cards use explicit snapshot links, including empty builds.
New snapshots do not mutate original `data/talents/`, global encoding versions,
previous baseline files or existing experiments. The Shaman investment study
stays pinned to its original reference until deliberately revised.

Classic comparisons and video-review/race/spell pages continue describing the
original data, and are labelled accordingly. New-reference class switching keeps
its selected snapshot; sharing, imports, print/embed and continue retain identity.
