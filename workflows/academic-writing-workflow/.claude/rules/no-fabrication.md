# No Fabrication — HARD RULE

**Every factual claim in prose, memos, plans, summaries, or manuscript text must be verified against the source before being written. No exceptions.**

This is the prose-side enforcement of the `rigor` skill. The rigor skill says "never fabricate parameters; always cite sources." This rule operationalizes that for the specific failure mode of describing the project's code, data, analysis, or literature.

---

## Why this rule exists

The most common — and most damaging — error in writing up empirical work is asserting a fact from *memory of what a result should look like* rather than from the source itself. A wrong predictor list, an off-by-N line citation, an "approximately N observations" that was never counted: each survives into co-author memos, into the manuscript, into a referee's reading, into the record. The cost of pausing to verify is seconds; the cost of being caught fabricating is a referee's trust in **every other claim in the paper**.

---

## What "fabrication" covers

Any prose statement that asserts a fact about the project:

- **Code claims** — what variables are defined, what predictors a model uses, what a script outputs, what a switch toggles.
- **Data claims** — sample size, variable coding, missing-data patterns, year coverage.
- **Result claims** — coefficients, standard errors, p-values, means, decile cutpoints.
- **Method claims** — what command was run with what options, what weights, what subsample.
- **File-path claims** — where a file lives, what it contains.
- **Citation claims** — what a paper found, what a coefficient was — anything attributed to a specific work.

If you can't cite a line of code, a manual page, or a paper page for a claim, you cannot make the claim.

## The forbidden moves

1. **Paraphrasing from training memory.** The *general literature* is not *our script*. Only what's in our source is the relevant fact.
2. **Filling a table to look complete.** If 4 of 6 rows are verified, the table has 4 rows — not 6 with `(similar)` or `[approx]` for the rest.
3. **"Approximately N observations"** without having run `count` / `_N` / `nrow()` for that subsample.
4. **"This script outputs X"** without having read the `save` / `export` / `graph export` line.
5. **"As stated in Author (Year)…"** when only the abstract or a search snippet was read, not the page.
6. **Recycling a claim from earlier in the session** without re-verifying when writing it into a permanent artifact.

## The required workflow

1. **Identify each claim** — every sentence asserting a fact about code/data/results/literature.
2. **Identify its source of truth** — a script line, a data variable, a manual page, a paper passage.
3. **Verify directly** — Read or grep the source *in the current turn*. Not session memory.
4. **Cite the verification path** — `[file:line]` for code, `(paper p.X)` for literature.

This adds ~30 seconds per claim. That's the price of getting it right.

## When verification is genuinely impossible

Do **not** assert the claim. Acceptable: `"Pending verification"`, `"TBD — figure not yet inspected"`, `"[UNVERIFIED — NEEDS USER CONFIRMATION]"`. Hedging ("approximately," "roughly," "consistent with") is **not** a substitute — either the number is verified (state it) or it isn't (flag it).

---

## Self-check protocol (mandatory)

Knowing the rule is not executing it. The check must be mechanical.

### Pre-write checklist (before each load-bearing claim)

- [ ] Did I run a Read/grep tool call **in this turn** that produced the value I'm about to type?
- [ ] Can I point to a tool result (not memory, not a previous turn) with the exact value?
- [ ] If it's a line number, did the grep return *that* line — not "near it"?

If any is "no," **do not type the claim.** Re-verify first.

### Pattern triggers — phrases that MUST fire verification

In prose for a permanent artifact (memo, plan, manuscript), each of these needs a fresh tool call in the current turn:

- **Code citations:** `[file:line]`, `lines X–Y`, `` `varname` ``, `gen`/`global` definitions, function names, switch names.
- **Numeric values:** sample sizes, coefficients, SEs, p-values, percentages, cutpoints, year ranges.
- **List enumerations:** "the predictors are X, Y, Z" — each item is its own verification.
- **Page citations:** "Author (Year) p.X", "Table N of paper Z".
- **Existence / negation claims:** "X is computed in script Y"; "Z is NOT a predictor" (negation needs an exhaustive grep, not a spot-check).

A sentence with three coefficients and a sample size has four verification points, not one.

### Post-draft audit (before declaring any memo/plan/draft "done")

1. Re-read the full draft for the pattern triggers above.
2. For each, ask: did I run a tool call this session that returned this value? If no → fabrication candidate → re-verify or strike.
3. Footer-flag anything that remains `[UNVERIFIED]`.

### What to do when caught

1. **Acknowledge directly** — "this was fabricated; I did not verify before writing." No hedging.
2. **Fix the instance** — re-grep, replace with the verified value or `[UNVERIFIED]`.
3. **Append a `[LEARN:rigor]` entry to `MEMORY.md`** — the sentence, the wrong value, the right value, the command that would have caught it.
4. **Look for repetition** — same class of error elsewhere in the draft/session? Audit those too.

---

## What this rule does NOT require

- Not a citation for every adjective. *"The estimates are sensible"* is fine; *"the estimate is 0.75 in the bottom decile"* is not.
- Not pre-emptive verification of non-load-bearing framing remarks in conversation. Permanent artifacts only.
- It blocks session memory as a *citation*, not as orientation. Reach for memory to know *where to look*; verify by opening.

---

## Recorded incidents (running log)

Append one entry per fabrication caught — the sentence, the wrong value, the verified value, and the command that would have caught it. Do not compress; the accumulation is the point. (Empty at template instantiation.)

— end log —
