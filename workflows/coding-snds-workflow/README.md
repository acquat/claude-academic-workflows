# Coding with SNDS

Claude as an empirical coding assistant inside the **French SNDS secure enclave** (SAS on Oracle + R downstream), with confidentiality and statistical-disclosure-control as first-class constraints — outputs are export-compliant **by construction**, not checked after the fact.

> The SNDS-system conventions here (partition keys, composite join keys, the PII identifier family, the ≥ 11 safe-harbor export gate, the dico-snds sources) are **common to all SNDS work**, not personal. Only your *project* specifics (cohort, code lists, table grains, the exact disclosure threshold from your DUA) are placeholders.

## What's inside

```
.claude/
├── CLAUDE.md                       # role, data stack, PII, secure-portal constraints
├── rules/
│   ├── snds-data-security.md       # HARD RULES — PII never leaves the enclave
│   ├── export-compliance.md        # ≥11 double gate, secret secondaire, export-gate annex in every script
│   ├── sas-sql-conventions.md      # Oracle/SQL: partition keys, 9-key joins, safe-replace
│   ├── sas-code-conventions.md     # SAS standards (header, macros, paths, sample audits)
│   ├── snds-r-portal.md            # R provisioning gate: request RStudio, package status, Oracle-from-R — auto-injected on .R edits
│   ├── r-code-conventions.md       # R standards (reproducibility, Oracle-from-R, figures, export discipline)
│   ├── quality-gates.md · verification-protocol.md · replication-protocol.md
│   └── plan-first-workflow.md · orchestrator-protocol.md · session-logging.md
├── agents/  sas-reviewer · sas-extraction-reviewer · r-reviewer   # SAS + R review; deep portal-extraction gate (read-only)
├── skills/  review-sas/ · review-r/ · sds-doc/ # SAS + R review; never-guess SNDS documentation lookup
├── references/
│   ├── snds-data.md                # your project lookup: tables, code lists, PII, DUA threshold
│   ├── snds-export-rules.md        # cited legal basis (arrêté 2024, MR-005, CGU) + référent questions
│   └── snds-export-checklist.md    # mechanical pre-export gate
├── templates/ · hooks/ (rigor-inject · verify-reminder · snds-r-rules · sas-rules · protect-files · skill-website-reminder) · settings.json
```

Plus `/rigor` and `/empirical-coding-discipline` from this repo's `skills/` library. For full downstream R-analysis *pipelines* (end-to-end data-analysis, paper review), see **[Other helpful resources](../../ATTRIBUTIONS.md)**.

## How to use it

1. **Copy** `.claude/` into your project.
2. **Fill** `CLAUDE.md` placeholders (name, institution, project, DUA reference).
3. **Populate `references/snds-data.md`** — your tables, code lists, PII variables, and the **exact disclosure threshold from your data-access agreement** (don't assume a number).
4. If a co-analyst owns part of the pipeline, mark their folder read-only; your writable work goes in `analysis/scripts/claude/`.

## The loop

Write SAS carefully (you can't cheaply debug on the portal) → `proc contents` + count after every table → `/review-sas` before incorporating output → `/sds-doc` whenever a variable is uncertain → outputs export-compliant by construction → the pre-export checklist before any demande de sortie.
