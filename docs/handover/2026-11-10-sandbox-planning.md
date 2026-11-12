# Sandbox preparation (2026-11-10)

Added root `AGENTS.md`, fork purpose/status/attribution in `README.md`, inspected
architecture in `docs/ARCHITECTURE.md`, requirements in
`docs/briefs/experimental-rulesets.md`, and the reviewable plan in
`docs/plans/experimental-rulesets-v1.md`. Marked older plan/agent notes as
upstream context. No runtime code, reference data, schemas or encoding changed.

Verified current rules are same-tree AND prerequisites; encoding v1 is still
mutable. Recommendation: complete experimental class datasets pinned to retained
baseline snapshots, with scoped encoding registries. Extra trees, cross-tree
hard prerequisites and exclusions are later work. No Shaman design is approved.

Checks: 575 Vitest tests, 571 pytest tests, production build/typecheck and all
three reference validators passed. Data validators retain warnings. Browser
suite not rerun for docs; earlier onboarding used external system-Chromium
configuration because managed browser download was blocked. See architecture
notes for distinction. No processes started by this documentation task.

Next: owner reviews/revises/approves the plan. First implementation change should
capture baseline data/encoding and add schema/validation/link regression fixtures.
Do not implement experiments before approval; do not merge or deploy.
