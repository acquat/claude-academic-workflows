---
name: session-discipline
description: Recreates the useful parts of the Claude hook pattern in Codex form: session-start rigor reminder, plan-first discipline, verify-after-edit reminder, and session-log wrap-up.
---

# Session Discipline

Use this skill at the start and end of substantial work.

## Start-of-session checklist

1. Activate `codex-safety`.
2. State the active repo boundary in one sentence.
3. For non-trivial work, write a short plan before touching files.
4. If the task involves research claims, activate `rigor`.
5. If the task involves data work, activate `empirical-coding-discipline`.

## After any edit

1. Verify the edited artifact in the cheapest reliable way.
2. Report what changed.
3. Name any unverified assumptions.

## End-of-session log

Before declaring completion, record:

- what was changed
- what was verified
- what remains open
- any permissions that were requested or deferred

## Codex note

Codex does not run the Claude hook lifecycle from `settings.json`.
So this skill turns those hook behaviors into an explicit operating procedure.
