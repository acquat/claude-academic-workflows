---
name: new-claim
description: Scaffold a new submission subfolder, copy the blank expense form, and pre-fill identity/budget defaults. Use when the user says "new claim", "scaffold a claim", "start a submission for [vendor]".
argument-hint: "[vendor-or-purpose] [YYYY-MM]"
allowed-tools: ["Read", "Bash", "Write", "Task"]
---

# /new-claim

Scaffold a new submission folder and produce a pre-filled form ready for line items.

## Instructions

1. **Determine the parent category** (ask if not obvious): `conference_expenses/` · `travel/` · `software_subscriptions/` · `publication_fees/` · other (propose a name).
2. **Compose the folder name.** Convention: `YYYY_<short-descriptor>` (lowercase, snake_case). E.g. `2026_example_conf`.
3. **Check for collision.** If the folder exists, stop and ask whether to add to it or pick a different name.
4. **Run the policy pre-check.** Read `.claude/rules/policy.md`. For routing-controlled categories (IT/software, travel), surface the relevant rule (e.g. prior-approval needed) BEFORE creating the folder. Confirm with the user.
5. **Create the folder** (`mkdir -p <category>/<folder-name>/`).
6. **Invoke `form-filler`** to copy the blank template into the folder and apply identity/budget defaults.
7. **Drop a folder README** from `.claude/templates/submission-folder-readme.md`, pre-filling what you know.
8. **Move the receipt(s)** from `pending_receipts/` into the folder — only after user confirmation.
9. **Draft a ledger row** in `submissions.md` with `Status: Drafting`.
10. **Report the next step:** "Form scaffolded. Run `/file-claim <folder>` to add line items and finalize."

## Troubleshooting

- **"Folder already exists"** — naming collision or duplicate. Ask: add to existing, or pick a different descriptor.
- **"Blank template not found"** — the institution's blank form was renamed/moved. Locate it (`find . -iname "*claim*form*.xlsx"`), or ask.
