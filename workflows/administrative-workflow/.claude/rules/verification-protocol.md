---
paths:
  - "**/*.xlsx"
  - "submissions.md"
---

# Verification Protocol

**At the end of every claim-filling task, run this checklist before declaring done.**

## For a filled form

1. **Identity / budget block** — name, email, entity, department, researcher ID present; budget/activity code correct (unless explicitly overridden); any derived/formula cells resolve without errors.
2. **Mission purpose** — non-empty and specific enough to be auditable (e.g. "Conference registration — <event> <month year>", not "expenses").
3. **Line items** — each has date, description, currency, amount-in-currency, amount-in-home-currency. For non-home-currency lines, the converted amount uses the reference rate **on the date of purchase**.
4. **Subtotals and TOTAL — hardcoded numeric values (NEVER trust formulas).** Re-open with openpyxl (no `data_only`) and confirm each subtotal and the grand total is a Python `int`/`float` — not a string starting with `=`, not `None`. Write `0` for unused sections. *(Reason: openpyxl writes `=SUM()` with a cached value of `None`, which prints blank in many viewers.)*
5. **Deadline** — the oldest line-item date is within the filing window; if within ~2 weeks of the deadline, flag urgent.
6. **Supporting docs** — each line item has a matching receipt in the same folder; receipts are originals (not card statements / photos, unless policy allows); filenames are readable (vendor + date), not opaque UUIDs.
7. **Folder hygiene** — folder name follows `YYYY_<descriptor>`; folder holds the filled form + every receipt + (optional) README.

## For the ledger (`submissions.md`)

1. A row is drafted for the claim (Status `Drafting` or `Filed`).
2. The folder column matches the actual folder path.
3. Both currency columns populated for non-home-currency claims.

## Reporting

```
VERIFICATION — <folder-name>
[ ] Identity / budget block   PASS / FAIL: <details>
[ ] Mission purpose           PASS / FAIL: <details>
[ ] Line items                PASS / FAIL: <details>
[ ] Subtotals / TOTAL         PASS / FAIL: <values>  (must all be numeric)
[ ] Deadline                  PASS / FAIL: <days remaining>
[ ] Receipts attached         PASS / FAIL: <count>
[ ] Folder hygiene            PASS / FAIL: <details>
[ ] Ledger row                PASS / FAIL: <details>

Score: NN/100  →  PRINT-READY / NEEDS FIXES
```
