---
paths:
  - "**/*.tex"
  - "**/*.R"
---

# Quality Gates & Scoring Rubrics (teaching)

## Thresholds (audience-dependent)

| Score | Ships as | Meaning |
|---|---|---|
| 80 | Student-facing handouts, TF sheets, feedback memos | Good enough to send out |
| 90 | Lecture decks, syllabus, exam papers | Ready for the room |
| 95 | Excellence | Aspirational |

## Lecture decks (Beamer .tex)

| Severity | Issue | Deduction |
|---|---|---|
| Critical | XeLaTeX compilation failure (3-pass) | -100 |
| Critical | Undefined citation / `??` reference in the PDF | -15 |
| Critical | Content overflow off the slide / overfull `hbox` > 10pt | -10 |
| Major | Notation inconsistent across the deck | -10 |
| Major | TikZ diagram with overlapping or mispositioned labels | -10 |
| Major | A slide that fails a pedagogy check (no takeaway, prerequisite assumed without stating) | -5 |
| Minor | Notes-to-self left in output (`% TODO`, `\hl{}`) | -5 |

## TF sheets / problem sets (.tex)

| Severity | Issue | Deduction |
|---|---|---|
| Critical | Solutions leak into the student handout | -100 |
| Critical | An exercise uses a method NOT taught in the target lecture | -20 |
| Major | Notation doesn't match the lecture | -10 |
| Major | Citation doesn't resolve in the lecture `.bib` | -10 |

## Student R code (.R)

| Severity | Issue | Deduction |
|---|---|---|
| Critical | Does not run / hardcoded absolute paths | -100 / -20 |
| Major | Missing `set.seed()` where randomness is used | -10 |

## Enforcement

- Decks **< 90** / handouts **< 80**: don't ship; list fixes.
- Feedback memos: never edit the student's source (see `no-edits-to-student-work.md`); a fabricated citation in a memo is critical.
