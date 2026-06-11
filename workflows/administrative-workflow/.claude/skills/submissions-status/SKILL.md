---
name: submissions-status
description: Read submissions.md and report what's drafting, filed-awaiting-payment, paid, and stale. Use when the user says "status", "what's the state of submissions", "anything outstanding".
argument-hint: "[no args]"
allowed-tools: ["Read", "Bash"]
---

# /submissions-status

Quick read of the ledger with summary statistics and a flag list.

## Instructions

1. **Read `submissions.md`.**
2. **Tally by status:** Drafting / Filed / Paid / Rejected / Historical.
3. **Flag stale rows:** `Status: Filed` AND no `Date paid` AND filed > 60 days ago.
4. **Sum unpaid** (home currency) across all `Filed` rows with no `Date paid`.
5. **Output:**

```
=== Submissions status — <today> ===
Drafting: <count>  - <vendor> (folder)
Filed (awaiting payment): <count>  total: <ccy> <sum>
  - <vendor>  filed YYYY-MM-DD  <amount>  <"STALE" if >60d>
Paid this year: <count>  total: <ccy> <sum>
Historical: <count>
🚨 Stale (chase admin contact): <count>
Next action: <suggestion>
```

## Troubleshooting

- **`submissions.md` not found** — recreate from the existing submission folders (read each form, rebuild rows).
- **Many `?` in Date paid** — the ledger isn't being updated when reimbursements arrive. Suggest cross-checking bank statements for institution transfers.
