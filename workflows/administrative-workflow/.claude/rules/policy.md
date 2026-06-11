# Institution Reimbursement Policy (encoded)

> **This is the source of truth for `compliance-reviewer`.** It encodes your institution's
> reimbursement policy as **numbered rules grouped by category**, each with a **severity** and
> (where relevant) an **exception/waiver** clause. The reviewer cites these IDs (e.g. `[A4]`, `[D1]`)
> so you can look them up. Re-read this file on every review — do not trust memory.
>
> **Two ways to populate it:**
> 1. **Recommended — auto-generate:** drop your institution's policy document (PDF/Word) in and run
>    [`/ingest-policy <doc>`](../skills/ingest-policy/SKILL.md). The `policy-parser` agent reads it and
>    fills this schema, citing the source for each rule and flagging anything ambiguous for you to confirm.
>    Re-run it whenever the policy is revised.
> 2. **By hand:** replace every `[...]` below with your policy's real values.
>
> Either way, the **structure** (rule IDs + severity + auto-flag conditions + exceptions) is what makes
> the reviewer reliable — keep it. The template below is the schema `/ingest-policy` targets and the
> fallback you fill manually.

**Severity legend:** `CRITICAL` (blocks the claim / unrecoverable) · `MAJOR` (must fix before handoff) · `MINOR` (note for awareness).

---

## A. Universal rules (apply to every claim)

| ID | Rule | Severity | Notes / exceptions |
|---|---|---|---|
| A1 | A claimed expense must have a professional purpose | CRITICAL | — |
| A2 | Original receipt/invoice required (no card-statement-only, no photos of screens) | CRITICAL | [your exceptions, if any] |
| A3 | Invoice must be in [the claimant's name / the institution's name] | MAJOR | [exceptions] |
| A4 | Filing deadline: within **[N months]** of the expense date | CRITICAL | — |
| A5 | Hard cap: no filing after **[end-of-fiscal-year date]** | CRITICAL | Past this = unrecoverable |
| A6 | Non-home-currency amounts must show both currencies at the reference rate **on the date of purchase** | MAJOR | use `/currency-convert` |
| A7 | No family / third-party expenses | CRITICAL | block those line items |

## B. Travel (plane / train)

| ID | Rule | Severity | Notes / exceptions |
|---|---|---|---|
| B1 | Book through **[required channel, e.g. agency / procurement portal]** | MAJOR | Waivers: [force majeure, low-cost carrier, abroad, family, >X% cheaper than channel — list yours] |
| B2 | Standard/economy class only | MAJOR | [over-threshold needs prior approval] |
| B3 | Fares above **[amount]** require prior approval | CRITICAL | — |

## C. Local transport (taxi / car / parking)

| ID | Rule | Severity | Notes |
|---|---|---|---|
| C1 | [mileage rate / taxi justification rules] | MINOR | — |

## D. Accommodation

| ID | Rule | Severity | Notes |
|---|---|---|---|
| D1 | Nightly ceiling by region: [Paris X · rest-of-country Y · USA Z · …] | MAJOR | over ceiling → prior validation |

## E. Food

| ID | Rule | Severity | Notes |
|---|---|---|---|
| E1 | Per-meal ceilings: lunch [X] · dinner [Y] (per person) | MAJOR | working meals need guest names + purpose |
| E2 | Snacks / alcohol [not] reimbursable | MINOR | [your rule] |

## F. IT / software / subscriptions

| ID | Rule | Severity | Notes |
|---|---|---|---|
| F1 | IT/software should route through **[procurement / IT dept]**, OR have prior approval before purchase | CRITICAL | surface BEFORE filing a personal claim |
| F2 | AI-assistant subscriptions reimbursable up to **[cap]/month** | MAJOR | [eligibility exceptions] |

## (add sections as needed)

- J. Publication / open-access fees — [rules]
- K. Conference registration — [rules]

---

## Never reimbursable

[List your institution's hard exclusions: e.g. spouse/family, bank fees, insurance, visa/passport, fines, moving expenses, …]

## Category taxonomy (for `receipt-classifier`)

Use the section letters above as the category IDs the classifier assigns (B = travel, D = accommodation, E = food, F = IT/software, …).
