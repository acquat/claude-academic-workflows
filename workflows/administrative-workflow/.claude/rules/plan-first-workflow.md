# Plan Before Building

Non-trivial work — more than ~3 files, a new pipeline stage, anything first-of-its-kind — starts in plan mode, not in the editor.

1. **Draft the plan:** goal, files touched, order of operations, and how the result will be verified.
2. **Save it to disk** at `.claude/quality_reports/plans/YYYY-MM-DD_<slug>.md`. Plans on disk survive context compression; plans that live only in the conversation do not.
3. **Get approval**, then hand off to the orchestrator ([orchestrator-protocol.md](orchestrator-protocol.md)).

Skip planning for single-file fixes with an obvious diff.

## When the ask is vague

"Improve X" / "analyze Y" admits many readings. Before planning: ask up to three clarifying questions, then write a one-page spec ([templates/requirements-spec.md](../templates/requirements-spec.md)) and have the user approve it. Ten minutes of spec beats an afternoon of rework.

## Recovering after compaction or a new session

Re-read the newest plan and the latest session log **before doing anything**, then state your understanding of where the task stands. Never resume from memory alone.
