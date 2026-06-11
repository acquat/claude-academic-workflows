# Session Logging

One log per working session: `.claude/quality_reports/session_logs/YYYY-MM-DD_<slug>.md` (format: [templates/session-log.md](../templates/session-log.md)).

Write to it at **three moments** — never as one batch at the end:

1. **Right after a plan is approved** — goal, approach, and why this approach.
2. **The moment something happens** — a decision made, a problem solved, a correction from the user. One or two lines, immediately; details evaporate.
3. **At wrap-up** — outcome, quality scores, anything left open.

Completion reports are separate and rarer: only when a task is finalized, to `.claude/quality_reports/completions/`, using [templates/quality-report.md](../templates/quality-report.md).
