---
name: reading-list
description: Curated reading list for a lecture topic or syllabus section. Use when user asks for a "reading list", "bibliography for", "papers on", "syllabus readings" for a topic. Lighter than a full literature-review skill (academic synthesis); this skill is syllabus-oriented and produces 3-5 core + 2-3 extension readings with one-paragraph annotations and prerequisite flags. Never fabricates citations.
argument-hint: "[topic] [course]"
allowed-tools: ["Read", "Write", "Grep", "Glob", "WebSearch", "WebFetch"]
effort: high
---

# Build a Curated Reading List

Produce a syllabus-oriented reading list for a lecture topic. Designed for quick assignment to students, not for academic-depth synthesis (for that, use a lit-review skill — e.g. the one in Pedro Sant'Anna's kit, linked under Other helpful resources in the repo README).

---

## Inputs

- `$0` — the topic (e.g., "moral hazard", "regression discontinuity", "health insurance market design").
- `$1` — the course (e.g., "Health Economics", "Applied Econometrics").

If either is missing, ask the user.

---

## Steps

### Step 1 — Anchor on existing course materials

Before searching the web, scan the course's existing material:

- Read the course's lecture `.tex` files for citations already in use (`\citet`, `\citep`).
- Read `<year>/<Course>/Literature/` if it exists.
- Glob for `.bib` files in the course folder.

These are **already-vetted** sources. Prefer them when relevant — students get coherence across lectures.

### Step 2 — Fill gaps via web search

For topics where the course material is thin, use `WebSearch` and `WebFetch` to find seminal and recent papers. Apply `/rigor`:

- **Verify each candidate exists.** Title, author, year, venue must be checkable. If unsure, fetch the paper page (Google Scholar, journal site) and confirm.
- **Mark uncertainty.** If a paper is plausible but not verified, prefix the entry with `[VERIFY]` and note what's uncertain.
- **Reject hallucinated papers.** If web search doesn't surface a candidate, drop it. Don't pad the list.

### Step 3 — Decide the mix

Target structure:

- **3-5 core readings** — students read all of them. Cover the canonical theory + one foundational empirical paper + one recent application.
- **2-3 extensions** — students read on interest. Push beyond the lecture toward a methodological frontier or a contested empirical puzzle.

### Step 4 — Annotate each entry

For each reading, write:

- **Citation** in the course's preferred style (`\citet{...}` for LaTeX users; `[Author Year]` plain otherwise).
- **One-sentence what:** what does the paper claim or show?
- **One-sentence why:** why is it on this list (vs. alternatives)?
- **Prerequisite flag:** what should the student have read or know first? (E.g., "Lecture 3 on IV; basic measure theory.")
- **Reading effort:** light (1-2 hours), medium (half day), heavy (full day).

### Step 5 — Save and report

Write to:

```
<year>/<Course>/reading_lists/<topic_slug>.md
```

Create the `reading_lists/` directory if it doesn't exist.

Report to chat:
- Path to the list
- Mix (N core, M extensions)
- Any `[VERIFY]` flags

Do NOT paste the full list into chat.

---

## Output template

```markdown
# Reading List: <Topic>
**Course:** <Course>
**Linked lecture(s):** <e.g., Health Economics Lecture 5-6>
**Date:** <YYYY-MM-DD>

## Core readings (read all)

### 1. <Author Year> — <Short Title>
**Full citation:** <author. (year). title. venue.>
**What:** <1 sentence>
**Why on this list:** <1 sentence>
**Prerequisites:** <what to read first>
**Effort:** light | medium | heavy

### 2. ...

## Extensions (read on interest)

### A. <Author Year> — <Short Title>
[same structure]

## Notes
- [VERIFY] flags, if any
- Pointers to lecture slides where each paper is referenced
```

---

## Examples

### Example 1: Moral hazard for Health Economics

**User says:** "Reading list on moral hazard for Health Economics."
**Actions:**
1. Scan `<year>/Health Economics/` for existing citations on moral hazard. Find references to canonical health-econ moral-hazard papers.
2. Web-verify candidates: e.g., Pauly's classic, a recent RAND-HIE-style paper, a methodology paper on selection vs moral hazard.
3. Propose 4 core + 2 extensions; annotate each.
4. Save to `<year>/Health Economics/reading_lists/moral_hazard.md`.

### Example 2: Topic with sparse course material

**User says:** "Reading list on machine-learning treatment-effect estimation for Applied Econometrics."
**Actions:**
1. Scan course material — likely thin (this is M1).
2. Web-search seminal papers (Athey, Imbens, Wager, etc.); verify each.
3. Propose readings calibrated to M1 level (avoid heavy ML theory; lead with intuition + applied papers).
4. Flag any unverified candidates as `[VERIFY]`.

---

## Troubleshooting

**Symptom:** Web search returns a paper that "sounds right" but you can't verify it.
**Cause:** Either a real-but-obscure paper, or a hallucination.
**Solution:** Mark `[VERIFY]` and note exactly what failed (e.g., "no DOI found"; "venue mentioned but no record on the journal's site"). Do NOT include unverified papers as core readings.

**Symptom:** Course material has 30+ candidate citations on the topic.
**Cause:** Topic is central to the course.
**Solution:** Curate ruthlessly. The reading list is for students, not a comprehensive bibliography. 3-5 core readings is the cap.

**Symptom:** Reading list reads like a full literature-review synthesis.
**Cause:** Skill drifted toward synthesis.
**Solution:** Trim. The output should be assignable in one email; if it's longer than ~2 pages, it's too much.

---

## Constraints

- Apply `/rigor`: no fabricated citations, no invented quotes from papers.
- Verify each citation; flag uncertainty as `[VERIFY]`.
- Cap core readings at 5.
- Prefer course-vetted citations (already in lecture `.bib`) when relevant.
- Match the course's citation style.
