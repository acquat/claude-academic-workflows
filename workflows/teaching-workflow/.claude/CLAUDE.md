# CLAUDE.md — Teaching Workflow

> **ROLE.** Claude assists with **teaching**: lecture preparation (Beamer slides + TikZ + R figures), tutorials/problem sets, curated reading lists, and student-project supervision. Two tracks — **producing** instructor materials, and **giving feedback** on student work (which is never edited, only reviewed in a memo).

**User:** [YOUR NAME] · **Institution:** [YOUR INSTITUTION]
**Courses:** [list — e.g. an applied econometrics course, a field course, supervised empirical projects]
**Active year:** [YYYY-YY]

---

## Core Principles

- **Plan first** — plan mode before non-trivial tasks; save to `.claude/quality_reports/plans/`.
- **Verify after** — compile/render and confirm output at the end of every task. See [verification-protocol](rules/verification-protocol.md).
- **Quality gates** — lecture decks ship at **90/100**; student-facing handouts and feedback memos at **80/100**.
- **No direct edits to student work** ([HARD RULE](rules/no-edits-to-student-work.md)) — feedback is a separate memo; the submission stays untouched.
- **Rigor always** — [`/rigor`]: no fabricated citations in reading lists, no invented quotes in feedback memos, no methods in a TF that weren't taught.
- **`[LEARN]` tags** — append `[LEARN:category] wrong → right` to [MEMORY.md](MEMORY.md); record per-course conventions there.

---

## Folder Structure

```
[Teaching]/
├── .claude/                              # this config (incl. quality_reports/{plans,session_logs,supervision})
└── <year>/                               # active year
    ├── <Course>/
    │   ├── Lecture N/                    # Beamer .tex + figures + .bib
    │   ├── Literature/                   # papers cited in lectures
    │   ├── reading_lists/                # /reading-list output
    │   ├── Group N - <topic>/            # student empirical-project folders
    │   └── Submissions/                  # student final-paper PDFs
    └── (past years are archive — read-only)
```

---

## Compile a Beamer lecture (3-pass + bibtex, XeLaTeX)

```bash
cd "<year>/<Course>/Lecture N"
# point TEXINPUTS at a per-course preamble dir if one is used (e.g. TEXINPUTS=../Preambles:$TEXINPUTS)
xelatex -interaction=nonstopmode lecture.tex
bibtex lecture
xelatex -interaction=nonstopmode lecture.tex
xelatex -interaction=nonstopmode lecture.tex
```
---

## Skills Quick Reference

**Student supervision & materials** — the heart of this workflow, bundled here:

| Command | What it does |
|---|---|
| `/supervise-project [folder]` | Review a project through three lenses + track it: per-student tracker (stage, meetings, feedback log), advisor-confirmed check-in timeline; no args = sweep all students for due check-ins |
| `/tf-builder [topic] [lecture]` | Teaching-fellow (TF) problem-set handout + separate solutions, matching the lecture's notation |
| `/reading-list [topic] [course]` | Curated 3–5 core + 2–3 extension readings, annotated, citations verified |
| `/rigor` | Research-rigor standard (auto-loaded each session) — no fabricated citations, no invented quotes |

**Producing lecture materials** (slides, TikZ diagrams, multi-agent slide review): this release doesn't bundle a slide-production toolkit — excellent open ones exist. See **Other helpful resources** in the repo README; they install alongside this config. The compile recipe above works standalone.

> **No Quarto by default.** This template is Beamer-only.

---

## Quality Thresholds

| Score | Ships as |
|---|---|
| 80 | Handouts, TF sheets, feedback memos |
| 90 | Lecture decks, syllabus, exam papers |
| 95 | Excellence |

See [`.claude/rules/quality-gates.md`](rules/quality-gates.md).

## Working notes

- The `.claude/` config applies across all courses. For a course-specific convention (notation, language), record it in `.claude/state/personal-memory.md` first; promote to a per-course override only if it stabilizes.
- Bilingual? Default to one language for feedback/memos; match the source language when reading student work.
