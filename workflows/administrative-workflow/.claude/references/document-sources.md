# Document Sources Map

> Declares, per maintained document, **where its content comes from** so [`/update-document`](../skills/update-document/SKILL.md) can refresh it without fabricating. Fill in your own documents. The **CV block below is a worked example** — adapt or replace it. Records may live in this project or elsewhere; give the path either way (relative, or absolute like `~/Dropbox/...`).

---

## Document: CV  *(example — edit for your setup)*

- **File / format:** `[cv.tex]` (LaTeX, e.g. the `res.cls` resume class) — or your format (`.docx`, etc.).
- **Build:** `cd <newest version folder> && pdflatex -interaction=nonstopmode [cv.tex]`
- **Versioning:** one folder per revision named `YEAR_MM` (e.g. `2024_05`, `2026_06`). Always copy the newest into a new dated folder and work there; **never edit an old version in place**.

### Sources of truth

| Section | Source | Caveats |
|---|---|---|
| Referee service | `[path]/Refereeing/` — one folder per journal | exclude any lower-tier `_extra/` folder unless told otherwise; flag folder-vs-CV mismatches before changing |
| Conferences / seminars / talks | `[path to reimbursements]/conference_expenses/` — one folder per trip (`YEAR_Venue`) | **a folder proves you TRAVELED, NOT that you presented — always ask presented-vs-attended, which paper, exact venue name; some trips are excluded by choice** |
| Working papers / in progress / publications + status | your research webpage (current self-listing) + `[path to reimbursements]/submissions.md` | reconcile titles/coauthors/status; confirm any status change |
| Published-citation details (volume, pages, year, DOI) | Crossref: `https://api.crossref.org/works/<DOI>` | never write a guessed citation — verify first |

### Formatting conventions to preserve

- *[Example: list NBER program meetings (Summer Institute, Health Care, …) under "Participant in:" even when you presented — don't reclassify.]*
- *[Example: conferences in year-descending order; add a new `YEAR:` line at the top.]*
- *[Add your document's conventions here.]*

### Always ask before adding / changing

- Presented vs. only attended? If presented — which paper, and the exact venue/seminar name?
- Include this trip/item at all? (Some are deliberately omitted.)
- Any status change (in-progress → working paper → R&R → published / rejected)?
- A title/date that differs between a source and the current document — which is authoritative?

---

## Document: [add others — bio, teaching statement, annual activity report, …]

- **File / format:** …
- **Build / render:** …
- **Versioning:** …
- **Sources of truth:** …
- **Always ask:** …
