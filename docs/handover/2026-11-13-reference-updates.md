# Imported reference updates (2026-11-13)

Added the repository skill `.agents/skills/update-reference/SKILL.md` and
`pipeline/update_reference.py` (fetch, prepare, publish). The adapter discovers
Wowhead's public Forever calculator script, checks environment/version/revision,
decodes JSON without executing JS and rejects unsupported or missing data. The
website interface needs no API key but has no stable public API contract.

First imported source: Forever 1.60.1, data revision 1794343902, SHA256
40a6e759692ca1c14d0e12b46194d3c4d0478ff358816c6fc6e063cc5bf3ca98.
It contains 9 classes, 27 trees and 467 talents. New IDs preserve upstream talent
identity; every rank text comes from the source. Death Mark's `$mcrit` formula is
retained verbatim and marked; unknown variables fail. Captured evidence, named
comparison baseline, differences and source issues accompany the retained data.

Missing icons are fetched slowly and cached with integrity checks; existing
assets are never overwritten. Publication is an offline repository operation
with validation and cleanup on failure. Repeating an identical source preserves
the original snapshot and import date. No schedule or runtime scraping is added.

`data/current-reference.json` selects the class-picker baseline and carries a
validated small source label. Cards and new-reference class switching preserve
explicit identity; code-only sharing is disabled for scoped snapshots. Legacy
routes, original video data/encoding and the Shaman experiment remain unchanged.
The source is labelled as publisher data, not verified live game state. Schema,
TS/Zod, tooltip attribution and warning display support that distinction.

Validation: 611 Python tests and 588 web tests passed, with production build,
lint and all reference/ruleset validators. The complete browser run passed 98
of 100 cases; two new cases caught a duplicate source label, which was removed,
and all four new reference cases then passed. PR CI runs the full 100 cases.
Original snapshots and the Shaman experiment retain all their hashes.

The first implementation was interrupted by environment loss and resumed from
preserved files. Code and data are separated into commits so `sourceCommit`
identifies the importer used. Final validation and remote PR/merge state are
reported at delivery. Follow `docs/REFERENCE-UPDATES.md` for subsequent refreshes.
