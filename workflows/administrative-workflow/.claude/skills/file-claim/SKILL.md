---
name: file-claim
description: Add line items to a scaffolded form, run compliance-reviewer, and produce the print-ready report. Use when the user says "file the claim", "finalize the form", "make it print-ready".
argument-hint: "[folder-path]"
allowed-tools: ["Read", "Bash", "Write", "Edit", "Task"]
---

# /file-claim

Take a scaffolded submission folder, fill the form's line items, run compliance review, and produce the print-ready report.

## Instructions

1. **Validate inputs.** Confirm the folder exists, contains a scaffolded form, and contains the receipts.
2. **Inventory the receipts.** Read each; identify line items (vendor, date, amount, currency).
3. **Convert non-home-currency lines** via `/currency-convert` (date of purchase, not statement date). Record both amounts.
4. **Categorize line items by section** (mission / travel / food / other — map to your form).
5. **Invoke `form-filler`** with the line items. It writes them and hardcodes the totals.
6. **Invoke `compliance-reviewer`** with the folder path → audit report at `.claude/quality_reports/audits/YYYY-MM-DD_<folder>.md`.
7. **Read the audit, apply the quality-gates rubric → score.**
8. **Surface findings:** Critical → stop and ask; Major → list + recommend; Minor → note. If score ≥ 80 → declare PRINT-READY with the file path.
9. **Update the folder README** with finalized totals and any rates used.
10. **Update the ledger** with the home-currency total and period. Status stays `Drafting` until the user confirms print/sign/handoff.

```
=== /file-claim — <folder> ===
File to print: <path>
Score: NN/100  →  PRINT-READY / NEEDS FIXES
Line items: <count>   TOTAL: <home-ccy> <amount>
Critical: <n>  Major: <n>  Minor: <n>
Audit: .claude/quality_reports/audits/YYYY-MM-DD_<folder>.md
Next: print, sign, hand to the admin contact. After delivery, set the ledger Status to "Filed".
```

## What this skill does NOT do

- Print the form (physical step).
- Set `Status: Filed` (the user does, after handoff).
- Move the original receipts (already in the folder by this stage).

## Troubleshooting

- **Score < 80, can't lift it** — a critical rule violation (e.g. routing without prior approval, past deadline). The claim may not be filable; surface with the specific rule ID.
- **Rate unavailable for a date** — weekend/holiday. Use the prior business day (`/currency-convert` auto-falls-back); note which date was used in the README.
