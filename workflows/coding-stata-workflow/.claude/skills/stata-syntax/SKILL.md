---
name: stata-syntax
description: Reference + protocol for writing correct Stata syntax. Invoke whenever about to write or edit Stata code (.do, .ado, or Stata commands embedded in R/Python/shell wrappers). First consults the internal reference `syntax-reference.md`; for uncharted territory, reads the official Stata manuals and APPENDS what was learned back to the reference. Never guesses — when a manual page is unclear, stops and asks the user.
---

# Stata Syntax — Reference Skill

Governs all Stata code Claude writes. It exists because syntax cannot be cheaply trial-and-errored — a syntax error wastes a run. The cheapest insurance is to verify before writing.

Three sources of truth, consulted in order:

1. **Internal reference** — [`syntax-reference.md`](syntax-reference.md) in this folder. Curated notes accumulated across sessions, organized by command. **Read first.**
2. **Official Stata manuals** — the PDF docs shipped with your Stata install. Read second, *only if the internal reference doesn't cover the question*.
3. **The user** — if a manual is ambiguous, or a user-written command's help isn't in the docs, **stop and ask**. Never guess.

## When invoked

Whenever about to: create/edit a `.do` or `.ado`; suggest a Stata command in chat (even a one-liner); write Stata embedded in an R/Python/shell wrapper (`system("stata -b do …")`, `subprocess.run([...])`); or resolve a reported Stata error. Not needed for: reading existing `.do` files, summarizing output, or discussion that yields no code.

## Protocol

### Step 1 — Consult the internal reference
Read `syntax-reference.md`. Look for the command(s) you intend to use, plus relevant postestimation (e.g. `predict` after `stcox` is documented under `stcox`). If everything is covered → write the code, citing the reference section in an inline `* Ref:` comment.

### Step 2 — Fall back to the manuals (only if needed)
Locate your Stata docs folder (commonly `/Applications/StataNow/docs/` on macOS, or under your Stata install dir — **adjust to your machine**; verify with `ls`). Use `pdftotext -layout <pdf> - | grep -n` to find the section, then Read the targeted page range. **Do not read whole manuals** (1000+ pages — they'll exhaust context).

Standard manual map (filenames are consistent across Stata installs):

| Manual | File | Topics |
|---|---|---|
| User's Guide | `u.pdf` | factor variables (`i.`,`c.`,`#`,`##`), missing values, locals/globals, syntax fundamentals |
| Base Reference | `r.pdf` | `regress`, `logit`, `probit`, `glm`, `margins`, `marginsplot`, `summarize`, `correlate` |
| Data Management | `d.pdf` | `merge`, `reshape`, `collapse`, `egen` |
| Programming | `p.pdf` | locals, scalars, matrices, `forvalues`, `foreach`, `while` |
| Survival | `st.pdf` | `stset`, `stcox`, `streg`, `predict` variants |
| Survey | `svy.pdf` | `svyset`, `svy:` prefix, `subpop()` |
| Graphics | `g.pdf` | `twoway`, `graph export`, axis options |
| Index | `i.pdf` | cross-reference of every command |

### Step 3 — Append back to the internal reference
If Step 2 was needed, **before writing the code**, Edit `syntax-reference.md` and append an entry under the relevant section: command · manual citation · verified syntax (one minimal example) · gotchas · date. Non-negotiable — the reference is only useful if it grows.

### Step 4 — When in doubt, stop and ask
For an ambiguous manual section or a user-written command (`reghdfe`, `ivreghdfe`, `coefplot`, `esttab`, `outreg2`, `stpm2`, …) whose help isn't in the docs, **do not guess**. Summarize the question in one sentence and ask the user to paste the `help <command>` output; then proceed and append the answer.

## Constraints

- **Read-only on the manuals.** `syntax-reference.md` is the only file this skill writes to (besides the user's own code).
- **Claude does not run Stata to verify syntax** — verification is text-based against the manuals. Any execution follows the project's mixed-workflow protocol (you run major jobs; small self-contained batch runs may be permitted). If a runtime error reveals the reference was wrong, fix the reference immediately, same session.
- **Keep entries short** — the reference should fit in one Read call. Curate, don't dump.

## Checklist (before writing any Stata block)

- [ ] Read `syntax-reference.md` for the relevant commands
- [ ] Gap? → read the targeted manual page, then APPEND to `syntax-reference.md`
- [ ] Still unclear? → ask the user for the help-file output
- [ ] Cite the reference section in an inline `* Ref:` comment
- [ ] Never use syntax that hasn't been verified
