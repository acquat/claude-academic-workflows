---
name: reconcile
description: Sweep pending_receipts/ and submission folders, list items by urgency against the filing deadline, flag stale filings and missing ledger rows. Use when the user says "reconcile", "what's pending", "what do I need to file", "weekly check".
argument-hint: "[no args]"
allowed-tools: ["Read", "Bash", "Glob", "Task"]
---

# /reconcile

Weekly reconciliation. Tells the user what to do next, in order of urgency.

## Instructions

1. **Invoke the `deadline-watcher` agent.** It returns categorized lists (LOST / URGENT / SOON / OK / STALE_FILED / MISSING_LEDGER_ROW / UNKNOWN_DATE).
2. **For each pending receipt, run a quick classification** (or invoke `receipt-classifier` if unclear).
3. **Format the report** as an actionable checklist:

```
=== Reconciliation — <today> ===
🚨 LOST (cannot recover): <file>  expense YYYY-MM-DD  (past cap)
⚠️  URGENT — within ~14 days of the deadline: <file>  deadline YYYY-MM-DD (<N> days)  → /new-claim <vendor> <YYYY-MM>
🟡 SOON — within 2 weeks: <file> ...
✅ OK — no rush: <count> items
🔍 STALE FILED (chase admin contact, >60 days): <folder>  filed YYYY-MM-DD
📒 LEDGER GAPS: <folder> not in submissions.md → backfill
❓ UNKNOWN DATE (manual review): <file>
```

4. **Recommend the single most urgent next action** as a one-liner.
5. **Wait for user direction.** Don't auto-execute new claims.

## Troubleshooting

- **Drop zone empty** — "✅ all clear, or you may have unfiled receipts in your inbox."
- **Many UNKNOWN_DATE** — receipts without a text layer. Open each, ask the user to confirm the date, re-run.
