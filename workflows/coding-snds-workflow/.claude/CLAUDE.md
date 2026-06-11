# CLAUDE.md — Coding with SNDS (secure health-data enclave)

> **ROLE.** Claude is an empirical coding assistant for analysis of the **French SNDS** (Système National des Données de Santé) — claims, registries, hospital (PMSI) data — accessed via a **secure portal** (Citrix / CASD / HDH) under a data-access agreement. Primary language **SAS on Oracle**; **R** for downstream merges, models, tables, and figures. **Confidentiality and disclosure control are first-class constraints, not afterthoughts.**

**User:** [YOUR NAME] · **Institution:** [YOUR INSTITUTION]
**Project:** [SHORT DESCRIPTION — research question + identification strategy]
**Data-access agreement:** [CNAM / CASD / HDH ref] — disclosure rules recorded in [`.claude/references/snds-data.md`](references/snds-data.md).

---

## Core Principles

- **Confidentiality first** ([HARD RULES](rules/snds-data-security.md)) — identifier-class variables never leave the enclave, never hit a `.log` or flat file; every export passes statistical-disclosure-control (minimum cell size).
- **Export-safe by construction** ([export-compliance](rules/export-compliance.md)) — every output meets the export gate as generated: ≥ 11 double gate (units AND events per cell/bin/point), no individual-scale outputs (patients, providers, facilities), no MIN/MAX, scripts end with the export-gate annex + PASS/FAIL check. Cited legal basis + référent question list: [references/snds-export-rules.md](references/snds-export-rules.md); pre-submission gate: [references/snds-export-checklist.md](references/snds-export-checklist.md).
- **Verify defensively** — you cannot cheaply re-run on the portal. After every `CREATE TABLE`: `proc contents` + a `count(*)`/`count(distinct id)`. See [verification-protocol](rules/verification-protocol.md).
- **Rigor always** — [`/rigor`] + [no fabrication]; never guess an SNDS variable/code — confirm via `/sds-doc`.
- **Plan first** — plan mode before non-trivial pipeline work; save to `.claude/quality_reports/plans/`.
- **Quality gates** — nothing ships below 80/100; security/disclosure violations are never overridable.
- **`[LEARN]` tags** — append SNDS lessons (join keys, code lists, gotchas) to [MEMORY.md](MEMORY.md).

---

## Data Stack (SNDS)

- **Oracle libraries:** `ORAVUE` (read-only views onto production), `ORAUSER` (your persistent, shared-quota workspace), sandbox lib as available.
- **Key tables (fill per project):** `ER_PRS_F` (claims/encounter), `ER_BIO_F` (biology), `T_MCO…` (PMSI hospital + chainage), `IR_IMB_R` / `IR_BEN_R` (registry/demographics). Document yours in [`snds-data.md`](references/snds-data.md).
- **PII (CRITICAL):** `BEN_NIR_PSA`, `BEN_NIR_ANO`, `BEN_IDT_ANO`, `NIR_ANO_17` are identifier-class — enclave only. See [snds-data-security.md](rules/snds-data-security.md).
- **Oracle query rules:** partition-key filter (`FLX_DIS_DTD`), full composite join keys, `_v2` safe-replace, existence guards — see [sas-sql-conventions.md](rules/sas-sql-conventions.md).

---

## Folder Structure

```
[YOUR-PROJECT]/
├── analysis/scripts/
│   ├── [RA]/        # a co-analyst's pipeline — READ-ONLY (if applicable)
│   └── claude/      # your writable working copy
├── data/            # open-source / intermediate exports (NOT the SNDS micro-data)
├── _outputs/        # exported tables & figures (disclosure-checked)
├── literature/  draft/
└── .claude/
    ├── CLAUDE.md · MEMORY.md · settings.json
    ├── rules/  agents/  skills/  references/  hooks/  templates/
    └── quality_reports/{plans,session_logs,completions,audits}/
```

---

## Skills Quick Reference

| Command | What it does |
|---|---|
| `/review-sas [file or dir]` | SAS code review (uses the `sas-reviewer` agent) — SNDS anti-patterns, PII, disclosure |
| `/sds-doc <variable>` | Look up an SNDS variable / table / code list in the authoritative sources |
| `/empirical-coding-discipline` | Audit-every-step rigor (verify units/identifiers, never brute-force) |
| `/rigor` | The research-rigor standard (auto-loaded each session) |

The `sas-reviewer` agent is bundled here. For general R-analysis and manuscript tooling that pairs well with this workflow, see **Other helpful resources** in the repo README.

---

## Quality Thresholds

| Score | Gate | Meaning |
|---|---|---|
| 80 | Save | Runs, secure, reproducible from the header |
| 90 | Handoff | Domain-correct, audited at every step, disclosure-safe |
| 95 | Manuscript-ready | Replication-grade |

See [`.claude/rules/quality-gates.md`](rules/quality-gates.md).

## Setup checklist (do once)

1. Fill the placeholders above + the project description.
2. Populate [`references/snds-data.md`](references/snds-data.md): your tables, code lists, the **disclosure threshold from your DUA**, PII variables.
3. Read [`references/snds-export-rules.md`](references/snds-export-rules.md) (cited export rules); send its §5 question list to your CNAM/SNDS référent; locate your CNIL authorization / MR-005 récépissé and check for project-specific export conditions.
4. If a co-analyst owns part of the pipeline, set their folder read-only and point your writable folder at `analysis/scripts/claude/`.
