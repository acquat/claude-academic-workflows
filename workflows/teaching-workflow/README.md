# Teaching Workflow

Claude for **teaching with a duty of care**: student-project supervision, problem sets, and reading lists — under one hard rule: **student work is never edited**. Feedback is always a separate, versioned memo. Beamer-only (no Quarto).

## What's inside

```
.claude/
├── CLAUDE.md                       # role, two tracks, compile recipe, quality gates (decks 90 / handouts 80)
├── rules/
│   ├── no-edits-to-student-work.md # HARD RULE — feedback is a separate memo; never touch the submission
│   ├── quality-gates.md            # incl. TF-solution-leakage = -100; deck/handout thresholds
│   ├── verification-protocol.md    # Beamer 3-pass + visual check + solution-leak grep
│   └── plan-first-workflow.md · orchestrator-protocol.md · session-logging.md
├── skills/
│   ├── supervise-project/          # three-lens review + per-student tracker, check-in timeline, due-check-in sweep
│   ├── tf-builder/                 # problem-set handout + separate solutions, lecture-notation-matched
│   └── reading-list/               # 3–5 core + 2–3 extensions, every citation verified or flagged
├── templates/ · hooks/ · settings.json
```

Plus `/rigor` from this repo's `skills/` library (no fabricated citations in reading lists, no invented quotes in feedback memos).

> **Producing lecture materials** (slide creation, TikZ diagram tooling, multi-agent slide review) is not bundled — excellent open toolkits exist for that side. See **[Other helpful resources](../../ATTRIBUTIONS.md)**; they install alongside this config.

## How to use it

1. **Copy** `.claude/` into your teaching folder.
2. **Fill** `CLAUDE.md` placeholders (name, institution, courses, active year).
3. Organize as `<year>/<Course>/Lecture N/` for content and `<year>/<Course>/Group N - <topic>/` for student projects.

## The loop

**Feedback:** `/supervise-project` reviews a student's folder through three lenses and writes a dated memo — while a per-student tracker logs feedback given and content reviewed against an advisor-confirmed check-in timeline; run it with no arguments to see who's due a check-in. Never edits the student's files. **Materials:** `/tf-builder` for tutorials (solutions in a separate file, leakage-checked), `/reading-list` for syllabus readings (verify-or-flag citations).
