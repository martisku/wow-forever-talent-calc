# Working in this fork

`martisku/wow-forever-talent-calc` is becoming a static sandbox for alternative
WoW Forever talent trees. Revisioned experimental rulesets are implemented; see [authoring](docs/RULESETS.md).
Start with [README.md](README.md), then [architecture](docs/ARCHITECTURE.md),
[requirements](docs/briefs/experimental-rulesets.md) and the
[first-release plan](docs/plans/experimental-rulesets-v1.md).

## Workflow

Requirements → implementation plan → implementation and verification in small,
reviewable changes. On 2026-11-12 the owner approved autonomous development, PR
creation and merging without repeated confirmation. Keep plans current and make
routine product/implementation decisions; ask only for genuinely blocking input.
Do not weaken checks or bypass branch protection to merge.
Use the existing checkout; cloud tasks are isolated, so do not create a worktree
unless explicitly requested.

## Navigation and commands

- `web/`: React + TypeScript + Vite/Tailwind. `src/data/` loads and describes
  data; `src/rules/` handles legality; `src/url/` handles links/imports;
  `src/ui/` renders; `tests/` contains Playwright tests.
- `pipeline/`: Python 3.12 + uv; `src/wowtalents/`, `stages/`, `tests/`, standalone
  validators. Large generated artifacts belong in ignored `pipeline/work/`.
- Refresh the reference with [.agents/skills/update-reference/SKILL.md](.agents/skills/update-reference/SKILL.md); see [source/update contract](docs/REFERENCE-UPDATES.md).
- `data/rulesets/`: retained baselines and experiments (append-only revisions).
- `data/talents/`: reference class data; `data/encoding/`: link orders/migrations;
  `data/overrides/`: reference corrections; `data/review/`: evidence crops.
- `docs/DATA-SCHEMA.md` governs reference talents, mirrored by
  `data/schema/class.schema.json`, `web/src/data/schema.ts` and `schema.zod.ts`.
  `web/README.md`, `pipeline/README.md`, `CONTRIBUTING.md` cover detailed workflows.
  `docs/PLAN.md` and old briefs/handovers record upstream history, not fork approval.

Node >=22 (CI uses 22); Python 3.12 and uv. Once per clone:
`git config core.hooksPath scripts/git-hooks`.

```bash
# in web/
npm ci
npm run dev
npm test
npm run lint
npm run build                   # includes type checking
npx playwright install chromium # once; Linux libraries may also be required
npm run e2e
# npm run gen updates committed indexes; review its diff after reference edits

# in pipeline/
uv sync --frozen
uv run --frozen pytest -q
uv run --frozen python validate_rulesets.py
uv run --frozen python validate.py --check ../data/talents/*.json
uv run --frozen python validate_races.py --check ../data/races/*.json
uv run --frozen python validate_spells.py --check ../data/spells/*.json
```

## Constraints

- Keep static deployment, base-path support and hash routing; no backend or
  combat simulation. Legal builds and costs do not prove balance.
- Keep 51 points and recognizable class identity. Shaman investment study is
  an experimental design sketch, not reference data or validated tuning.
- Treat current data as a dated reference, not the latest game. Custom designs
  must remain separate from reference corrections and extraction provenance.
- Never hand-edit `data/extracted/`; reference corrections use overrides and
  export/promotion per `CONTRIBUTING.md`. Do not alter baseline data/encoding
  as a side effect of experimentation. Preserve existing links.
- Keep rules and codecs pure (no DOM/React); avoid unrelated refactoring.
  Add relevant behavior tests during implementation and report skipped/failed
  checks accurately. Build alone does not run data validation or tests.
- Preserve user changes, dependency lockfiles and generated indexes unless the
  task calls for changing them. Public docs are English; no private identifiers,
  credentials or AI session URLs. Follow `CONTRIBUTING.md` privacy/hook guidance.
- Record completed phases in `docs/PLAN.md`; add a concise indexed handover for
  state worth passing on. Detailed architecture/workflow belongs under `docs/`.
