# Document Maintenance — versioned documents from sources of truth

Some administrative documents — a **CV**, a short bio, a teaching statement, an annual activity report — are *assembled from records you already keep* and re-issued periodically. This rule governs maintaining them: pull from declared sources of truth, **never fabricate**, **always confirm** ambiguous items, match the document's existing formatting, and version every revision. It is the document-side of the same rigor the reimbursement side applies.

## Sources of truth

- Each maintained document declares its sources in [`.claude/references/document-sources.md`](../references/document-sources.md) — a table of *"section → where the data lives."* Pull from there.
- **Never invent content** — no papers, coauthors, dates, venues, grants, awards, talks, or citations that aren't in a source.
- **Verify external facts against an authoritative source** before writing them (e.g. publication citation details — volume, pages, year, DOI — via Crossref). Never write a guessed citation.

## Always confirm — never classify on your own

- A source folder often proves *less* than it looks. **Canonical example:** a travel/expense folder proves you **traveled** somewhere, NOT that you **presented**. For every candidate item where the source is ambiguous, ask the user:
  - Did you present, or only attend?
  - If presented: which paper? what's the exact venue/seminar name to list?
  - Should it be included at all?
- Surface **every discrepancy** between a source and the current document (a changed title, a different date, a status change) and ask which is right — don't silently overwrite.

## Match historical formatting

- Follow the document's existing conventions exactly: ordering, section labels, how categories are listed. Don't reclassify or reorder entries to "improve" them without asking. (E.g. if conferences are listed year-descending and certain meetings go under "Participant in:" even when presented, preserve that.)

## Versioning

- One folder per revision (e.g. `YEAR_MM`). To revise, **copy the newest version into a new dated folder and work there** — never edit an old version in place.

## Verify

- Rebuild the document (compile LaTeX / render) and **visually check the output** before declaring done.
- Fix obvious typos when you find them, but list them so the user is aware.

## Why non-negotiable

A CV or bio is a public, citable record. A fabricated talk or a mis-stated paper status survives into grant applications, tenure files, and the historical record. The cost of asking is one question; the cost of a wrong entry is your credibility.
