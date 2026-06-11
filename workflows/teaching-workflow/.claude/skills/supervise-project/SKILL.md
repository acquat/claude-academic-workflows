---
name: supervise-project
description: Supervision review + tracking for student empirical projects. Reviews a project folder through three lenses (code, prose, substance) and produces a consolidated feedback memo — while maintaining a per-student tracker that logs feedback given and content reviewed, records the project stage, and holds an advisor-confirmed check-in timeline. Flags the advisor when a check-in is due. Run with a folder to review one student; run with no arguments to sweep all trackers and see who needs a check-in. Does NOT edit student work.
argument-hint: "[path to project folder — or no args for the check-in sweep]"
allowed-tools: ["Read", "Write", "Grep", "Glob", "Task"]
effort: high
---

# Supervise a Student Project

Two jobs in one skill:

- **Review** (with a folder argument): inventory what the student delivered, review it through three lenses, write a dated feedback memo — and update the student's tracker.
- **Flag** (no arguments): sweep every tracker and tell the advisor which students are due or overdue for a check-in, and whose folders contain new material awaiting review.

Student files are **never edited**. All feedback lands as memos; all state lives in the tracker.

---

## The tracker (one per student/group)

`.claude/quality_reports/supervision/<slug>_tracker.md`, created on first run from
[templates/supervision-tracker.md](../../templates/supervision-tracker.md). It records:

- **Project stage** — proposal · data collection · analysis · drafting · final.
- **Meeting history** — date, what was discussed, agreed next steps.
- **Check-in timeline** — the advisor-confirmed cadence and the **next check-in date**.
- **Feedback log** — one row per review: date, artifacts reviewed, top fixes given, memo link.
- **Inventory snapshot** — what was in the folder at last review (so new material is detectable).

The tracker is append-only for history sections: meetings and feedback rows are added, never rewritten.

---

## Mode 1 — no arguments: the check-in sweep

1. Glob `.claude/quality_reports/supervision/*_tracker.md`. If none exist, say so and suggest running the skill on a project folder first.
2. For each tracker, compare today against the **next check-in date**, and glob the project folder against the **inventory snapshot**.
3. Report a triage list:

```
=== Supervision check-ins — <today> ===
🔴 OVERDUE:   <student>  next check-in was <date> (<N> days ago) — stage: <stage>
🟡 DUE SOON:  <student>  check-in due <date> (<N> days)
📬 NEW MATERIAL: <student>  <k> new file(s) since last review → run /supervise-project <folder>
✅ ON TRACK:  <count> students
```

4. Recommend the single most urgent action. Don't run reviews unasked.

## Mode 2 — with a folder: review + track

### Step 1 — Resolve and load

Derive the `<slug>` from the folder name. Load the tracker if it exists.

### Step 2 — First run only: interview the advisor (don't guess)

If there is no tracker, ask the advisor — a handful of questions, then **wait for answers**:

1. **Previous meetings:** Have you already met with this student/group? When, and what was discussed or agreed?
2. **Project stage:** Where is the project right now — proposal, data collection, analysis, drafting, or final?
3. **Expectations:** What's the next deliverable, and by when?
4. **Check-in timeline:** Propose a stage-appropriate cadence (e.g. proposal/final stages: every 1–2 weeks; data/analysis: every 2–3 weeks) and ask the advisor to **confirm or adjust it**. Record the agreed cadence and compute the next check-in date.

Create the tracker from the template with these answers. On later runs, skip the interview — but if the advisor mentions a meeting that happened since the last review, append it to the meeting history, and re-confirm the timeline whenever the stage changes.

### Step 3 — Inventory the folder, diff against the snapshot

Classify each file by lens:

| Extension | Artifact type | Lens |
|---|---|---|
| `.pdf` (memo / draft / slides) | Prose / slides | prose + substance |
| `.tex` / `.qmd` | Draft / slides | prose + substance |
| `.docx` | Memo / draft | prose |
| `.R` / `.r` / `.Rmd` / `.do` / `.py` | Code | code |
| `.csv` / `.xlsx` / `.dta` | Data | (note presence; don't analyze unless asked) |

Mark what's **new or changed since the last review** (vs. the tracker's inventory snapshot). Report the inventory before proceeding; if the folder is sparse, confirm scope with the advisor.

### Step 4 — Review through the three lenses

- **Code lens** — reproducibility, units/identifier checks, regression-specification issues.
- **Prose lens** — structure, exposition, signposting. Review-and-propose only; never edit student work.
- **Substance lens** — identification strategy, external validity, derivation correctness.

If specialist reviewer agents are installed in this project (e.g. from a general academic kit — see *Other helpful resources* in the repo README), delegate each lens to the matching agent via `Task`, in parallel. Otherwise apply the lenses yourself. Focus on **new/changed material**; don't repeat feedback already logged in the tracker — reference it ("the parallel-trends concern from 2026-03-04 stands").

### Step 5 — Write the memo

`.claude/quality_reports/supervision/<slug>_<YYYY-MM-DD>.md`:

```markdown
# Supervision memo — <Student / Group>
**Stage:** <stage>   **Date:** <YYYY-MM-DD>   **Reviewed:** <artifacts>

## Where they are
2–3 sentences: stage, what's been delivered, what's missing vs. the agreed deliverable.

## What's working
Specific bullets — "the IV first-stage F = 24 in Table 2" beats "good empirical work."

## Most important fixes (priority order)
1. <the single thing to fix before going further>

## Lens findings (by artifact)
[code / prose / substance findings, synthesized; conflicts resolved with a position]

## For the next meeting
3–5 questions or tasks.

## Tone notes (for the advisor)
[anything tricky to deliver in person]
```

### Step 6 — Update the tracker

Append a **feedback-log row** (date · artifacts reviewed · top fixes · memo link), refresh the **inventory snapshot**, update the **stage** if it changed (confirm with the advisor), and set the **next check-in date** from the timeline. If the advisor wants a different date this cycle, record the override.

### Step 7 — Report

Print to chat: stage · top fix · next check-in date · memo + tracker paths. Don't paste the full memo.

---

## Tone

Firm but encouraging. Lead with what's working; call a fatal issue fatal — soft framing on a structural problem wastes the student's time. Match the language of the source artifacts.

## Constraints

- **Never edit student artifacts.** Feedback is always a separate memo (see [rules/no-edits-to-student-work.md](../../rules/no-edits-to-student-work.md)).
- **Never invent quotes, data, or meeting history.** Apply `/rigor`; when the tracker and the advisor's memory disagree, ask.
- **Append, don't overwrite** — memos and tracker history accumulate; a correction adds a dated entry.
- **The timeline belongs to the advisor** — propose cadences, never set one without confirmation.

## Examples

**First run, early-stage group:** `/supervise-project "Group 1 - nutrition ineq"` → no tracker → interview: one prior meeting (kickoff, 2026-02-10), stage = proposal, deliverable = revised RQ in 2 weeks, advisor confirms a 2-week cadence → inventory: one meeting memo → substance lens on the proposed RQ → memo + tracker created; next check-in 2026-02-24.

**Later run, new draft appeared:** `/supervise-project "Group 4 - SES health"` → tracker exists (stage: analysis) → diff: `draft.tex` is new → prose + substance lenses on the draft only; code feedback from last time referenced, not repeated → feedback row appended; next check-in advanced per the 3-week cadence.

**The Monday sweep:** `/supervise-project` → "🔴 Group 2 overdue (check-in was Friday); 📬 Group 4 has 2 new files; ✅ 3 on track. Suggested first move: review Group 4 while it's fresh, then schedule Group 2."
