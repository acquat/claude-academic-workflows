---
name: update-document
description: Refresh a maintained, versioned document (CV, bio, teaching statement, activity report) by pulling current data from its declared sources of truth, reconciling against the latest version, and producing a new dated version. Use when the user says "update my CV", "refresh my bio", "update the document from my records". Never fabricates; always confirms ambiguous items.
argument-hint: "[document name or path]"
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "WebFetch", "Task"]
---

# /update-document

Refresh a versioned administrative document from the records you already keep — most often a **CV**. Follows [`.claude/rules/document-maintenance.md`](../../rules/document-maintenance.md): pull from sources, never fabricate, always confirm, match formatting, version every revision.

## Instructions

1. **Identify the document and read its sources map.** Resolve `$ARGUMENTS` to a maintained document. Read [`.claude/references/document-sources.md`](../../references/document-sources.md) for that document's **format + build command**, **versioning convention**, and **section → source table**. If no sources map exists yet, help the user create one from the scaffold first, then proceed.
2. **Locate the newest version.** Per the versioning convention (e.g. the newest `YEAR_MM/` folder). Read the current document.
3. **Pull current data from each declared source:**
   - **folder-based** sources → list/scan the folders (e.g. one folder per refereed journal; one folder per conference/expense trip),
   - **ledger/file** sources → read them (e.g. `submissions.md` for paper status),
   - **web** sources → `WebFetch` (e.g. a research webpage's current self-listing),
   - **citation details** → verify via the authoritative API (e.g. Crossref `https://api.crossref.org/works/<DOI>`) — never a guessed citation.
4. **Reconcile.** Diff the pulled data against the current document: what's new, what changed status, what's missing, what conflicts.
5. **Confirm before changing** (per the rule). Surface **every** ambiguous item and discrepancy as a question and **wait for answers**:
   - presented-vs-attended (a travel folder proves travel, not a talk) — and if presented, which paper + exact venue name;
   - status changes (in-progress → working paper → R&R → published / rejected);
   - inclusion choices (some trips/items the user doesn't want listed);
   - any source-vs-document conflict (different title/date) — ask which is authoritative.
   Never classify or fabricate on your own.
6. **Produce a new version.** Copy the newest version folder into a new dated folder; apply **only the confirmed changes**, matching the document's existing formatting. **Never edit an old version in place.**
7. **Rebuild and verify.** Compile/render the new version; visually check it; list any typos you fixed.
8. **Report:** the new version path, what was added/changed, and the list of items still awaiting the user's decision.

## Example — refresh a CV

**User:** "Update my CV."
**Actions:** read the sources map → find the newest `YYYY_MM/` version → pull the refereed-journal folders, the conference/expense folders, the submission ledger, and the research webpage; verify any new publication via Crossref → reconcile → ask *"You have a new travel folder for `<venue>` — did you present or attend? If presented, which paper and what's the exact venue name?"* and *"Paper X shows R&R in the ledger — update its status on the CV?"* → on answers, create the next `YYYY_MM/` folder, apply the confirmed edits in the existing format, recompile, and report.

## Constraints (from `document-maintenance.md`)

- Never invent papers, talks, coauthors, dates, venues, grants, awards, or citations.
- A travel/expense folder proves travel, **not** a presentation — always ask.
- Match historical formatting; don't reclassify or reorder silently.
- Always work in a **new dated version folder**; verify the build before declaring done.

## Troubleshooting

- **No sources map** → walk the user through filling `references/document-sources.md` for this document first.
- **A source folder is offline / a path moved** → report it; update the path in the sources map; don't guess the content.
- **Crossref returns nothing for a DOI** → flag the citation as unverified and ask the user rather than writing a guess.
