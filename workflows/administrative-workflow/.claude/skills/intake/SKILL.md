---
name: intake
description: Classify a single new receipt (PDF, email, screenshot) and propose where it belongs. Use when the user says "intake this", "what is this receipt", "where does this go", or drops a file into pending_receipts/.
argument-hint: "[path-to-receipt]"
allowed-tools: ["Read", "Bash", "Glob", "Task"]
---

# /intake

Classify a single receipt and propose a destination folder.

## Instructions

1. **Resolve the path.** If the user gave a bare filename, look in `pending_receipts/`. If multiple match, ask.
2. **Invoke the `receipt-classifier` agent** with the path. It returns a structured classification block.
3. **Surface policy red flags.** If the classifier flagged any rule (routing-controlled category, card-receipt-only, past-deadline, family expense), pull these to the top and ask the user how to proceed.
4. **Recommend the next action:**
   - Fits an existing submission folder → suggest moving it there.
   - Needs a new folder → suggest `/new-claim <vendor> <YYYY-MM>`.
   - A policy rule blocks it → explain and stop.
5. **Wait for user approval before moving anything.** The drop zone is sacred — never move files autonomously.

## Troubleshooting

- **"File not found"** — bare filename used but file isn't in `pending_receipts/`. Provide the full path.
- **"Cannot extract date"** — receipt is a screenshot/scan with no text layer. Ask the user to confirm the date, then proceed.
