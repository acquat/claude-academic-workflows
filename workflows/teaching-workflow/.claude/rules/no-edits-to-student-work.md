# No Direct Edits to Student Work — HARD RULE

**Student submissions are never modified. Feedback is always delivered as a separate memo on disk.**

This is the teaching analogue of the proofreading protocol (review-and-propose, never silently apply) — but stricter, because the artifact belongs to the student and the feedback record must be auditable.

## The rule

- **Never edit** a student's `.pdf`, `.tex`, `.docx`, `.R`, `.do`, slides, or any submitted file — not to "fix a typo," not to "improve a sentence," not even with tracked changes.
- All feedback goes to a **separate memo**:
  - Supervision → `.claude/quality_reports/supervision/<group_slug>_<date>.md`
- **Append, don't overwrite.** A follow-up adds a new dated memo in the thread — it never silently replaces prior feedback.

## Why

1. **Integrity of the record** — the submission is the evidence; the memo is the assessment. Mixing them destroys both.
2. **Auditability** — a student (or a grade appeal) must be able to see the original work and the feedback as separate documents.
3. **Trust** — students must know their files are read, not rewritten.

## What's allowed

- Reading the submission (any format; use the `pdf`/`docx` skills for those formats).
- Quoting short passages in the memo to anchor feedback (≤ ~30 words each; never invent quotes).
- Producing *new* instructor artifacts (a solutions document, a model answer) in instructor space — clearly separate from the student's files.

## Cross-references

- `supervise-project` skill — enforces this rule; writes memos, never touches the source.
