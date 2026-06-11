---
name: tf-builder
description: Generate a TF (teaching-fellow) problem-set handout — a tutorial sheet with a separate solutions document — for a given lecture topic. Use when user asks to "build a problem set", "make a TF sheet", "create exercises", "generate a tutorial sheet", or specifies a topic and target lecture. Produces two LaTeX files — a student handout and an instructor solutions document — using the lecture's preamble conventions for visual consistency.
argument-hint: "[topic] [target lecture path]"
allowed-tools: ["Read", "Write", "Edit", "Grep", "Glob", "Bash"]
effort: high
---

# Build a TF Problem Set (teaching-fellow tutorial sheet)

Generate a problem set tied to a specific lecture, with a clean student handout and a separate instructor solutions document. The mix is calibrated for ~90 minutes of student work: 1 warm-up (recall), 2-3 core exercises (applying methods from the lecture), and 1 extension (stretches the student beyond the lecture).

---

## Inputs

- `$0` — the topic (e.g., "IV estimation", "moral hazard", "regression discontinuity").
- `$1` — path to the target lecture file or folder (e.g., `<year>/Health Economics/Lectures 5-6/`).

If either is missing, ask the user. If only the lecture path is given, propose a topic from the lecture's title/section structure.

---

## Steps

### Step 1 — Read the target lecture

- Locate the lecture's main `.tex` (or `.qmd`) file.
- Identify: methods taught, notation conventions, running empirical applications, citations used.
- Read the lecture's preamble (or the per-course `Preambles/` directory if one exists). The handout will reuse those preamble conventions so the handout matches the lecture's visual style.

### Step 2 — Propose the exercise mix

Before writing LaTeX, present the proposed mix to the user for sign-off:

```
Warm-up:    <one-line description, ~10 min>
Core 1:     <one-line description, ~20 min>
Core 2:     <one-line description, ~20 min>
Core 3:     <one-line description, ~20 min, optional>
Extension:  <one-line description, ~20 min>
```

Each exercise must:
- Use notation consistent with the lecture.
- Reference at least one paper or method explicitly taught in the lecture (no novel methods).
- Have a defensible learning objective (recall / application / synthesis).

Wait for user approval before drafting.

### Step 3 — Write the student handout

Output: `<lecture_dir>/TF_<n>.tex` (or co-located with the lecture).

Structure:

```latex
\documentclass[11pt]{article}
% reuse lecture preamble conventions
\usepackage{...}                  % match the lecture
\title{TF <n> — <Topic>}
\author{<Course> — <Year>}
\date{}

\begin{document}
\maketitle

\section*{Warm-up}
<exercise text, no solution>

\section*{Exercise 1 — <subtitle>}
<exercise text>

% ... etc

\section*{Extension (optional)}
<exercise text>

\end{document}
```

Conventions:
- No solutions or hints in the handout.
- Number sub-questions (a), (b), (c) for graders.
- Cite papers via `\citep{...}` matching the lecture's `.bib`.
- If the lecture uses a course logo / title slide style, mirror it on the handout cover.

### Step 4 — Write the instructor solutions document

Output: `<lecture_dir>/TF_<n>_solutions.tex`.

For each exercise:
- Restate the question.
- Provide a worked solution (full derivation for theoretical questions; full code + interpretation for empirical ones).
- Include 2-3 common student mistakes and how to address them in the TF session.
- For empirical exercises with code: include an `R` (or Stata/Python) chunk that students can run; verify the code is syntactically valid (compile-check via `Rscript -e 'parse(file=...)'` for R).

### Step 5 — Compile both documents

Run the 3-pass XeLaTeX compile from inside the lecture folder. If the handout depends on a per-course preamble, set `TEXINPUTS` accordingly.

Verify:
- No compilation errors.
- No `Overfull \hbox` warnings > 10pt.
- All citations resolve.

### Step 6 — Report to the user

Print to chat:
- Path to handout, path to solutions
- Compile status
- Estimated total time (sum of per-exercise estimates)

---

## Examples

### Example 1: TF sheet on IV estimation, Health Economics Lectures 5-6

**User says:** "Build a TF sheet on IV estimation for Health Economics Lectures 5-6."
**Actions:**
1. Read `<year>/Health Economics/Lectures 5-6/<lecture>.tex`.
2. Identify methods: 2SLS, weak-instrument tests, LATE interpretation; running app: a published health-econ IV paper (e.g., Card 1995 or similar).
3. Propose: warm-up (recall: rank/exclusion), core 1 (mechanical 2SLS by hand), core 2 (interpret a first-stage F = 6 case), core 3 (LATE vs ATE in a heterogeneous-effects setting), extension (Imbens-Angrist monotonicity).
4. After approval, write `TF_5-6.tex` and `TF_5-6_solutions.tex`.
5. Compile, verify, report.

### Example 2: TF sheet requested without a lecture path

**User says:** "Build a TF sheet on parallel trends."
**Actions:**
1. Search `<year>/` for lectures mentioning parallel trends or DiD.
2. Propose: "I see DiD covered in Health Economics Lectures 7-8. Use that as the anchor?"
3. After confirmation, proceed to Step 1 with `Lectures 7-8/` as the target.

---

## Troubleshooting

**Symptom:** Compile fails with `! LaTeX Error: File '...sty' not found`.
**Cause:** The handout's preamble references a package only available via the lecture's `TEXINPUTS`.
**Solution:** Set `TEXINPUTS` to point at the lecture's preamble dir, or copy the relevant `.sty` to the handout's folder. Document the chosen approach in `MEMORY.md` for next time.

**Symptom:** Notation in the TF sheet doesn't match the lecture.
**Cause:** Skipped Step 1 — didn't read the lecture's notation registry.
**Solution:** Re-read the lecture; rewrite affected exercises. Add a `[LEARN:tutorials]` note to `MEMORY.md` if a particular symbol is course-canonical.

**Symptom:** Solutions document leaks into the handout (e.g., student gets the answers).
**Cause:** Wrong file written.
**Solution:** The two outputs MUST be separate files. The handout has zero solution content. Verify by grepping the handout for words like "solution", "answer", "we have" — if present, fix.

---

## Constraints

- No fabricated methods. Every exercise must apply a method explicitly covered in the target lecture (the extension may stretch slightly, but stretches must be flagged as such in the solutions).
- No fabricated citations. If an exercise references a paper, the citation must resolve in the lecture's `.bib`.
- Match the lecture's notation exactly. Inconsistent notation in a TF sheet is a pedagogy failure.
- The handout never contains solutions, hints, or answer-key material.
