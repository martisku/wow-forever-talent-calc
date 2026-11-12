# Experimental rulesets: requirements

Status: first-release subset implemented under the owner’s 2026-11-12
autonomous-development authorization. See [authoring](../RULESETS.md).
See [implementation plan](../plans/experimental-rulesets-v1.md) for the proposed
first-release subset and [architecture](../ARCHITECTURE.md) for current behavior.

## Purpose

Make this fork a sandbox for designing alternative WoW Forever talent trees.
Explore new branches, placement and prerequisite changes, rank investments,
cross-tree incentives, exclusive choices and, when justified, additional trees.
Borrow distinct build mechanics from Path of Exile and archetypes/opportunity
costs from Pathfinder 2e while keeping recognizable WoW class identities.

Keep the 51-point budget initially: explore competing uses of scarce investment,
not a larger point pool. Show legal allocations, spent/remaining points, tier
and prerequisite requirements and blocked-action reasons. Design notes should
explain what an investment competes with. These are structural checks, not a
combat simulator, damage model or evidence that a build is balanced.

Shaman caster, melee, support or defensive archetypes may illustrate tradeoffs;
the shipped Shaman investment study is a proposal for iteration, not a
combat-balance claim. The owner has delegated routine design choices.

## Required behavior

| ID | Requirement |
| --- | --- |
| R1 | Preserve an identifiable, immutable reference baseline: record upstream/fork source commit, captured class files, rules, encoding orders and content hashes. Describe it as a snapshot, not current official game data. Retain referenced assets or stable asset copies. |
| R2 | Allow named experiments with stable slug IDs and immutable positive-integer revisions. Every revision pins a baseline ID and explicitly lists supported classes. Changes to talents, rules, notes or encoding require a new published revision. Never resolve an old revision to “latest.” |
| R3 | Repository-authored experiments can add, modify, move or remove talents. IDs preserve conceptual identity across moves; replacements get new IDs. Validate references and rank/grid consistency. Designs remain separate from `data/talents/`, `data/extracted/` and correction overrides. |
| R4 | Switch baseline ↔ experiment for a supported class, with active name, revision and baseline visible. Never silently transfer allocations between incompatible datasets. First release may switch to an empty build, leaving the previous build recoverable via Back. Unsupported classes/revisions get explicit feedback. |
| R5 | Mark custom additions, modifications and moves with text as well as color, with accessible design-intent notes. List removals in a change summary because no cell remains. Compare to the pinned baseline, distinct from “changed vs Classic Era.” Preserve evidence for unchanged reference records; do not imply a new design was observed in game. |
| R6 | Full shared links identify class, ruleset, exact revision and encoding version, including empty experiment builds. All share/import/history/print/embed/continue paths retain this identity. Unavailable or malformed identities show a clear error, never a plausible build under another ruleset. |
| R7 | Existing baseline links without a ruleset continue to mean the reference baseline, with their current encoding interpretation. Preserve present valid allocations and existing migration/notice behavior. Do not reinterpret bare codes as experiment identity. No guarantee can restore historical links whose mutable encoding was already overwritten before capture. |
| R8 | Baseline updates create a new snapshot; keep old snapshots, experiment revisions, their encoding and required assets available. Updating/rebasing an experiment is an explicit new revision, not a mutation. Opening a retained revision reproduces its dataset and legal build after a baseline update. |
| R9 | Preserve static-site deployment, base-path/hash routing and the existing stack. Validate every shipped experiment before production; production does not need a backend or in-browser authoring engine. Reject unsupported rule fields, dangling refs, duplicate identities and schema mistakes rather than silently ignoring them. |

## Release boundary

The smallest release implements R1–R9 using existing allocation semantics:
51 total points, existing tier gates, same-tree AND prerequisites and rank
limits. It makes alternative layouts and investments usable without introducing
new legality rules. Keep all baseline classes accessible; one synthetic test
experiment can demonstrate plumbing. Publishing a playable custom design is a
separate review of actual content, not implicit approval from this plan.

Later releases may support cross-tree requirements, explicit opportunity-cost
choices/exclusion groups and extra-tree progression. Each needs defined legality,
refund/reset/import semantics and UI explanations before implementation.
Cross-tree synergy expressed in talent text is a design proposition; the
calculator will not simulate it or verify its performance.

Defer a visual editor, automatic patch rebasing, build conversion across revisions,
combat simulation, accounts, cloud saves, generic rule DSL and unrelated UI work.

## Review questions

Review the proposed storage and compatibility contract and the narrow first-release
boundary in the plan. A playable first experiment needs owner-approved talents
and values later; none are needed to implement and test ruleset infrastructure.
