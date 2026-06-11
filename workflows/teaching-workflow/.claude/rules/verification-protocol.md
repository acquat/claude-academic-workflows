---
paths:
  - "**/*.tex"
  - "**/*.R"
---

# Task Completion Verification Protocol (teaching)

**At the end of every task, verify the output renders/runs correctly.** Non-negotiable.

## Lecture decks / TF handouts (Beamer or article .tex)

1. **Compile 3-pass + bibtex** with XeLaTeX (set `TEXINPUTS` to the per-course preamble dir if one is used):
   ```bash
   xelatex -interaction=nonstopmode file.tex
   bibtex file
   xelatex -interaction=nonstopmode file.tex
   xelatex -interaction=nonstopmode file.tex
   ```
2. **Open the PDF** and confirm figures render and nothing overflows the frame.
3. **Check the log** for undefined references/citations, `??`, and overfull `hbox` > 10pt on display content.
4. **TF handouts:** grep the *handout* for solution leakage ("solution", "answer", worked-derivation phrases) — the handout must contain none.

## TikZ diagrams

1. Compile the standalone diagram → valid PDF.
2. Check label positions, overlaps, and visual consistency by eye on the compiled PDF.
3. **Freshness:** if a diagram appears both standalone and embedded in a deck, confirm they match the current source.

## Student R exercises / replication code

1. Run `Rscript <file>.R`; confirm outputs created with non-zero size.
2. Spot-check estimates for reasonable magnitude.

## Feedback memos (supervision)

1. The student's source file was **not** modified (see `no-edits-to-student-work.md`).
2. Every quote anchoring a score is real (no invented quotes); every suggested-revision citation resolves (apply `/rigor`).
3. Memo saved to the right place (`.claude/quality_reports/supervision/`).
4. Tracker updated — feedback row appended, inventory snapshot refreshed, next check-in date set.

## Checklist

```
[ ] Deck/handout compiles clean (3-pass), PDF opened, no overflow/undefined refs
[ ] TF handout has zero solution leakage
[ ] TikZ standalone compiles; embedded copy matches
[ ] Student code runs (if applicable)
[ ] Feedback memo: source untouched, quotes/citations verified, saved correctly
[ ] Reported results to user
```
