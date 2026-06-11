---
paths:
  - "**/*.tex"
  - "scripts/**/*.R"
---

# Task Completion Verification Protocol

**At the end of EVERY writing task, verify the manuscript compiles and the output is clean.** Non-negotiable.

## For the manuscript (.tex)

1. **Compile, 3-pass** (so cross-refs and bibliography resolve):
   ```bash
   [pdflatex|xelatex] -interaction=nonstopmode main.tex
   bibtex main
   [pdflatex|xelatex] -interaction=nonstopmode main.tex
   [pdflatex|xelatex] -interaction=nonstopmode main.tex
   ```
   *(Use `xelatex` if the preamble needs it — e.g. `fontspec`; otherwise `pdflatex`.)*
2. **Check the log** for: `Undefined references`, `Citation ... undefined`, `??` in the PDF, overfull/underfull boxes in displays.
3. **Confirm the PDF was produced** with non-zero size and the expected page count.
4. **No notes-to-self in the compiled output** — grep the source and resolve every `\hl{}`, `\textcolor{orange}{}`, `% TODO`, `\begin{comment}…\end{comment}`, `////` before declaring done.
5. **No-fabrication post-draft audit** (see `no-fabrication.md`) — re-scan prose for pattern triggers; verify or flag each.
6. **Citations** — every `\citet`/`\citep` key resolves in the `.bib`, and the claim it supports is logged in `lit_review.md`.

## For analysis scripts (.R)

1. Run the script (`Rscript scripts/R/<file>.R`).
2. Confirm output files (figures, tables, RDS) were created with non-zero size.
3. Spot-check estimates for reasonable magnitude.
4. If the script feeds a manuscript number, re-derive that number from the script's outputs and check it against the tolerances in `replication-protocol.md`.

## Common pitfalls

- **Assuming success** — a non-zero exit or missing PDF means the task is NOT done.
- **Stale figures/tables** — a derived artifact older than its source is out of date; regenerate it.
- **One-pass compile** — cross-references and the bibliography need the full 3-pass sequence.

## Verification checklist

```
[ ] Compiles clean (3-pass + bibtex), PDF produced
[ ] No undefined refs / citations / ?? in PDF
[ ] No notes-to-self (\hl, comments, TODO) in output
[ ] No unverified factual claims (no-fabrication audit done)
[ ] Citations resolve and are logged in lit_review.md
[ ] Numbers within replication tolerance (if empirical)
[ ] Reported results to user
```
