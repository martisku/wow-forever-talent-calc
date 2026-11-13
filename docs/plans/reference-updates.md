# Updating the imported reference (2026-11-13)

Goal: keep a reference snapshot aligned with what Wowhead publishes for Forever,
without silently rebasing experiments or reinterpreting existing links.

Verified today: the Forever calculator page exposes environment 16, client
version 1.60.1 and an exact cache-versioned `nether.wowhead.com/forever/data/talents-classic`
script. Its `wow.talentCalcClassic.classicplus.data` JSON contains all nine classes,
27 trees, 467 talents, prerequisites and complete rendered rank descriptions.
The page and data both returned HTTP 200 without credentials. This is the site's
own web data interface, not a documented supported API. No authenticated Blizzard
Forever tree API was established. Existing wago.tools DB2 tooling is retained;
its build-list request returned 403 here, so it is not the primary source.

Implement in small changes:

1. A deterministic Python adapter: discover the exact script from the Forever
   page, verify environment/version/cache revision, decode JSON without executing
   JavaScript, require complete supported class trees/ranks/prerequisites and
   compatible five-point tier gates. Cache source bytes and checksums. Fail on
   schema drift or HTTP errors; no Classic fallback or inferred higher ranks.
2. Prepare a candidate and name-matched difference report. Download missing icons
   sequentially at most twice per second; retain existing image assets. Validate
   all classes before publication. Keep network work out of the static app.
3. Publish a new immutable baseline and its source evidence; update a small
   current-reference pointer used by the class picker. Explicit links and all
   legacy class/build routes continue loading their original snapshot. Experiments
   retain their pins. Distinguish publisher data from video/manual/client extracts.
4. Document and provide an agent skill for checking, preparing, validating and
   delivering reference updates through PR/CI. Do not promise continuous/live
   accuracy or automatically apply an unchecked scraper result on a schedule.

Acceptance: the real source imports all 467 talents; all rank texts originate
from the captured response; repeated publication of identical input is a no-op;
corrupt/incomplete/wrong-environment data fails without modifying retained data;
old links/experiments remain identical; the new snapshot is selectable and is the
landing-page reference; source/version/retrieval date are visible and truthful.
Exercise parsing, cache integrity, failure cleanup, publication/retention, unit
suites, production build and browser navigation. Merge only after CI passes under
the owner's standing autonomous-development authorization.

Observed source issue: Death Mark includes `$mcrit`. The adapter preserves this
known variable verbatim with an explicit warning/report; unknown variables still
fail. No statistic is invented to force a fully rendered description.
