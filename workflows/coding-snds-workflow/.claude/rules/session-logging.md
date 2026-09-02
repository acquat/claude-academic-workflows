# Session Logging

**Location:** `quality_reports/session_logs/YYYY-MM-DD_description.md`
**Template:** `templates/session-log.md`

## Four Triggers (all proactive)

### 1. Post-Plan Log

After plan approval, immediately capture: goal, approach, rationale, key context.

### 2. Incremental Logging

Append 1-3 lines whenever: a design decision is made, a problem is solved, the user corrects something, or the approach changes. Do not batch.

### 3. End-of-Session Log

When wrapping up: high-level summary, quality scores, open questions, blockers.

### 4. End-of-Day Handoff (spoken, in the terminal -- NOT a file)

The spoken counterpart to trigger 3, and a different artefact: the log is the durable record,
this is what the user reads before closing the laptop. **Give it unprompted whenever the user
signals the day is ending** ("done for the day", "signing off", "wrapping up"), and on request.

Three sections, in order:

1. **Action items.** Numbered, each executable tomorrow *without re-reading the conversation*:
   the exact command, the exact log line or value that signals success, and what to do in each
   branch if it fails. Mark items blocked on other people as non-blocking so they can be picked
   up opportunistically.
2. **Project status.** What is DONE and validated, what is IN FLIGHT, and -- the section that
   earns its place -- **what is not yet known.** Never let a validated instrument, pipeline or
   dataset read as a validated *result*.
3. **What we did today.** Narrative, not a changelog. Include what went wrong and what it taught,
   anything the user overruled and why they were right, and work done in parallel sessions so the
   repo state makes sense.

Also: flag **expiring assets with their deadline** (scratch tables under a purge policy, tokens,
data access windows) -- that converts a silent future loss into a dated decision. Close on a
substantive point about the research, not on logistics.

Every figure obeys the project's numbers rule: it comes from the ledger or a directly-observed
log. A handoff is exactly where a half-remembered number gets laundered into fact -- if a run is
not yet archived, say the numbers are pending rather than reconstructing them.

## Quality Reports

Generated **only at merge time** -- not at every commit or PR.
Save to `quality_reports/merges/YYYY-MM-DD_[branch-name].md` using `templates/quality-report.md`.
