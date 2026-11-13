# WoW Forever Talent Design Sandbox

This fork, **[martisku/wow-forever-talent-calc](https://github.com/martisku/wow-forever-talent-calc)**,
is a sandbox for alternative WoW Forever talent trees:
new branches, changed placements and ranks, cross-tree incentives, meaningful
choices and eventually additional trees. The starting budget stays **51 points**;
the goal is different investment tradeoffs while preserving WoW class identities.
Path of Exile's distinct build mechanics and Pathfinder 2e's archetypes and
opportunity costs are design inspirations.

The calculator assesses legal allocations and investment requirements. It is
not a combat simulator and cannot prove balance. The current dataset is a
**reference snapshot**, not a claim about the latest game or approved custom designs.

## Current reference updates

The class picker opens the latest imported Wowhead Forever reference, with its
source/version/retrieval date visible. Old builds and experiments retain their
original snapshots. Publisher data may lag hotfixes; this is not independent
verification of live game behavior.

Use the repository [update-reference skill](.agents/skills/update-reference/SKILL.md)
or the [fetch → prepare → publish commands](docs/REFERENCE-UPDATES.md) to check
for updates, review differences and create a new retained snapshot. No API key
or browser-time data fetch is required. There is no automatic update schedule.

## Implemented and planned

Today this fork retains the upstream static calculator: reference class trees,
point allocation, share links, tooltips, Classic comparisons, races and spellbooks.
Named, revisioned experimental rulesets, switching, custom-change labels and
revision-specific links are implemented. Start with **Shaman investment study**
in the Shaman page’s Ruleset selector; its proposed effects and investment costs
are an exploratory sketch, not validated balance. [Author another design or
revision in repository files](docs/RULESETS.md). A visual editor, extra trees,
cross-tree hard prerequisites and mutually exclusive choices remain future work.
The screenshots and hosted site linked below show the upstream app.

- [Experimental ruleset requirements](docs/briefs/experimental-rulesets.md)
- [First-release implementation plan and scope](docs/plans/experimental-rulesets-v1.md)
- [Architecture and validation notes](docs/ARCHITECTURE.md)
- [Contributor/agent workflow](AGENTS.md): requirements → plan → review/revision →
  small tested implementation changes. The owner authorized autonomous development,
  PRs and merging; routine decisions do not need repeated approval.

Reference corrections continue through the upstream override/export workflow in
[CONTRIBUTING.md](CONTRIBUTING.md). Custom designs live under `data/rulesets/`; do not
use correction overrides to author experiments. Original briefs and
[project history](docs/PLAN.md) describe upstream work rather than an approved
fork roadmap.

## Upstream attribution

Based on **[Deradon/wow-forever-talent-calc](https://github.com/Deradon/wow-forever-talent-calc)**,
a fan-made World of Warcraft: Forever (Classic+) calculator built from BlizzCon
2026 footage. The original extraction pipeline, reference data and calculator
remain the foundation of this fork.

**[Upstream hosted calculator](https://deradon.github.io/wow-forever-talent-calc/)**
— static site, no account, no tracking, no backend. This is not a deployment of
the fork's proposed sandbox.

[![The class picker](docs/images/landing.webp)](https://deradon.github.io/wow-forever-talent-calc/)

## Existing reference-calculator functionality

- **Original footage snapshot:** all nine classes, 469 of 470 talents, with the Classic-style rules:
  51 points, five per row, prerequisite arrows, tier gating.
- **Shareable builds.** `#/warrior?v=1&t=...` is the whole build; also a short
  build code, a Discord-ready text summary, a print view and `embed=1` for
  forums. Wowhead Classic strings can be imported by talent name.
- **Honest tooltips.** Every talent says how well it was read. Open a tooltip
  and press `d` (or move into it) for where the numbers come from: the frame it
  was read from, the Classic talent its higher ranks were scaled from, and the
  second reader's wording when the two disagreed.
- **What changed vs Classic Era** — 145 new talents, 81 moved, 26 with a
  different rank count, 127 reworded and 108 gone, with an inline word diff.
- **Races** — 37 racial traits for 9 races (both Skyborne variants) and the
  race/class matrix, with the 16 combinations Classic Era never allowed.
- **The spellbook as the stream showed it** — 410 entries and 152 full
  tooltips over eight classes, every tab of all eight opened at least once.
- **Keyboard and touch**: arrow keys across the grid, shift-click to max,
  ctrl-click to clear, undo/redo, tap-to-open tooltips with +/− controls.

| A class page, tooltip pinned | What changed against Classic |
|---|---|
| [![A class page](docs/images/class.webp)](https://deradon.github.io/wow-forever-talent-calc/#/druid) | [![The changes page](docs/images/changes.webp)](https://deradon.github.io/wow-forever-talent-calc/#/changes) |

[![The race and class matrix](docs/images/races.webp)](https://deradon.github.io/wow-forever-talent-calc/#/races)

## Where the reference data comes from

A local vision model read every talent tooltip out of the BlizzCon 2026 demo
stream, one hovered cell at a time, and OpenCV placed each reading in its grid
cell, matched its icon and traced the prerequisite arrows. Only rank 1 was ever
on screen, so higher ranks are scaled from the matching Classic Era talent and
the point rules are assumed to be the Classic ones. Every record keeps the
video timestamp, the frame and the reader's confidence, and nothing claims to
be official.

The inherited reference snapshot has these caveats:

- **Numbers are the least reliable part.** Rank 1 was read from a screenshot;
  ranks 2+ are arithmetic on a Classic scaling pattern, which is wrong wherever
  Forever retuned a talent.
- **57 of 469 records have been checked by a human**, 6 are still below the
  0.8 confidence threshold. The rest are a good draft.
- **One talent is missing** (mage, Fire, row 1 column 3): it was never hovered
  on stream.
- **The rules are assumed**: 51 points, 5 per row, first point at level 10.
  Nobody has confirmed them for Forever.
- **The Classic Era comparison is a reference dataset**, not a database dump.

## Report or correct a reference reading

Open **[a wrong-reading issue](https://github.com/Deradon/wow-forever-talent-calc/issues/new?template=wrong-reading.yml)**
with the talent and what it should say. The fastest route is the review page —
`#/review/<class>`, for example
[`#/review/warrior`](https://deradon.github.io/wow-forever-talent-calc/#/review/warrior) —
which shows every record beside the tooltip crop it was read from and has a
"Report on GitHub" link per row that fills the form in for you.

Fixing it yourself is one JSON entry and a pull request: `CONTRIBUTING.md`.

## Run it yourself

Requires `node` >= 22 and, for the data half, [`uv`](https://docs.astral.sh/uv/)
(Python 3.12). `ffmpeg` and `yt-dlp` are only needed to re-run the extraction
from video, which also wants an NVIDIA GPU for the local vision model.

```bash
# once per clone: the tracked hook that keeps AI session links out of commits
git config core.hooksPath scripts/git-hooks

# the site
cd web
npm ci               # install from the committed lockfile
npm run dev          # http://localhost:5173
npm test             # Vitest unit/data tests
npm run e2e          # Playwright (once: npx playwright install chromium)
npm run build        # static files in web/dist, deployable anywhere

# the data
cd ../pipeline
uv sync --frozen
uv run --frozen pytest
uv run --frozen python validate_rulesets.py
uv run python validate.py --check ../data/talents/*.json   # must exit 0
uv run stages/08_export.py --help                          # extract / promote
```

`data/talents/<class>.json` remains the original video-reference source of truth; the app
also reads encoding orders, generated indexes, crops and the race/spell datasets.
`data/current-reference.json` selects the imported reference for the class picker.
Retained baseline snapshots and complete experimental datasets live under
`data/rulesets/`; see [authoring](docs/RULESETS.md).
Stage by stage: `pipeline/README.md`. Web details: `web/README.md`. The data contract: `docs/DATA-SCHEMA.md`. Plan and history: `docs/PLAN.md`.
Contributor rules, including the commit-message hook: `CONTRIBUTING.md`.

## License and affiliation

Code is MIT (`LICENSE`). Talent names, descriptions, icons and the frame crops
under `data/review/` are © Blizzard Entertainment and are not covered by it;
they are included as a factual reference to a publicly broadcast demo.

**Not affiliated with, endorsed by, or connected to Blizzard Entertainment.**
World of Warcraft is a trademark of Blizzard Entertainment, Inc. This is an
unofficial fan project, and its data is unofficial and partly unverified.
