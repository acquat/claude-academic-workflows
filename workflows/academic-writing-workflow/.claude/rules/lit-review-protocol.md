# Literature Review Protocol — HARD RULE

**Every time Claude reads a paper from `literature/` (or any other source), the `lit_review.md` file at the project root MUST be updated with what was learned.**

This is a hard rule, not a suggestion. Compliance is required for the same reason fabrication is forbidden: rigor depends on a verifiable trail of what has been read and what was concluded from it.

---

## Why this rule exists

1. **Rigor.** The `rigor` skill demands that claims be grounded in primary texts, not in training memory or recall. The `lit_review.md` is the persistent record that supports this — when a future session needs to defend a citation, it can consult `lit_review.md` first.
2. **Speed.** Re-reading PDFs is expensive (especially the 10–20 page extractions for primary literature). Future sessions can consult `lit_review.md` and get the load-bearing facts in seconds rather than minutes.
3. **Continuity.** Sessions are bounded by context. A persistent lit-review file outlives any single session and accumulates project knowledge.
4. **Auditability.** Reviewers and the author can both verify which papers Claude has actually read versus which it is citing from memory.

---

## What "reads a paper" means

Any of the following triggers an entry in `lit_review.md`:

- Reading a PDF via the `Read` tool (any number of pages — even a single page counts).
- Reading the abstract on a journal website or via screenshot.
- Reading a section, theorem, or table excerpt.
- Receiving a screenshot of a paper from the user.

**It does NOT count if:** Claude only knows a paper from training data and has not actually opened the source. In that case, do NOT add an entry pretending to have read it.

---

## What goes in each entry

For each paper, record:

| Field | What to put |
|---|---|
| **Cite key** | The bib key used in `references.bib` (or "TBD" if not yet added) |
| **Venue** | Journal/working paper, volume, year, pages, DOI if available |
| **Pages read** | Specific pages opened — e.g., "1–7" or "title page only" or "abstract only" |
| **What the paper does** | 1–3 sentences summarizing the contribution |
| **Key claims/results** | Bullet list of the load-bearing claims for our manuscript |
| **How it connects** | Which of our manuscript sections, arguments, or analysis tasks the paper feeds into |
| **Status** | "Cited in body", "in bib but not cited", "deferred", etc. |
| **Watch-outs** | Any common mischaracterizations to avoid — e.g., "Theorem 1 doesn't require X" |

If a paper is briefly consulted (title page only) and a deeper read is deferred, log this in the "Future paper-reading checklist" at the bottom of `lit_review.md`.

---

## When to consult `lit_review.md`

**Before re-reading a paper:** Always check whether it has already been read in a prior session. If `lit_review.md` has the relevant facts, use those.

**Before citing a paper in the manuscript:** Verify that the entry in `lit_review.md` supports the specific characterization being made. If it doesn't, either (a) read the relevant section of the paper, OR (b) make the citation more cautious.

**Before adding a paper to the bib:** Confirm via the actual PDF (not training memory) that the bib entry's title, authors, year, and venue are accurate.

---

## Format expectations

- One entry per paper.
- Sorted by date of paper publication (most recent at the bottom of the chronological section).
- Use H2 headings (`## Author (Year) — Title`) for entries.
- Use H3 (`### Future paper-reading checklist`) for the deferred-reads list at the bottom.
- Cross-reference your project's task IDs from the plan when relevant.

---

## Example entry skeleton

```markdown
## Author (Year) — *Title in italics*

**Cite key:** `firstauthor_keyword_year`
**Venue:** *Journal*, Vol. X, No. Y (Month Year), pp. AAA–BBB
**Pages read:** 1–7

**What the paper does.** [1–3 sentences.]

**Key claims/results:**
- Bullet 1
- Bullet 2

**How it connects.** [How this feeds into the manuscript or your revision plan.]

**Status:** [Cited in body / in bib not cited / deferred / not yet in bib]

**Watch-outs.** [Optional — known mischaracterizations to avoid.]
```

---

## Cross-references

- `lit_review.md` (the file maintained per this rule) lives at the project root (`./lit_review.md`)
- `rigor` skill (installed at `~/.claude/skills/rigor/SKILL.md`; a project-local `.claude/skills/rigor/` copy also works) — depends on this protocol
- `replication-protocol.md` — the paper↔code numeric-tolerance protocol; this rule complements it for the literature dimension
