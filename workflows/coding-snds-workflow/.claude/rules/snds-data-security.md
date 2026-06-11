---
paths:
  - "**/*.sas"
  - "**/*.R"
---

# SNDS Data Security & Disclosure Control — HARD RULES

Working in the SNDS secure environment is governed by a data-access agreement (CNAM / CASD / HDH or equivalent). These rules are non-negotiable; violating them is a confidentiality breach, not a style issue.

## 1. PII / identifier-class variables

The beneficiary-identifier family — `BEN_NIR_PSA`, `BEN_NIR_ANO`, `BEN_IDT_ANO`, `NIR_ANO_17`, and any pseudonymised individual ID — is **identifier-class**. For these variables:

- **MUST NOT** be written to a flat file (`.csv`, `.txt`, `.rds`, `.dta`) outside the secured environment.
- **MUST NOT** appear in a `.log` file (no `proc print` of beneficiary-level rows; use `obs=0` / `proc contents` to inspect structure).
- **MUST NOT** be committed to any repository or copied to a shared/unsecured mount.
- **MUST NOT** leave the enclave in any form. Only aggregate outputs that pass disclosure control (below) may be exported.

Keep identifier-keyed tables inside `ORAUSER` / secured `WORK`. When in doubt whether a variable is an identifier, treat it as one and check with `/sds-doc`.

## 2. Statistical disclosure control (export gate)

**Nothing leaves the enclave without passing the data provider's disclosure-control rules.**
Full coding rules: [`export-compliance.md`](export-compliance.md) (the ≥ 11 double gate, secret
secondaire, dominance on € cells, figure/map/log rules, the mandatory export-gate annex block).
Cited legal basis: [`references/snds-export-rules.md`](../references/snds-export-rules.md).
Pre-submission gate: [`references/snds-export-checklist.md`](../references/snds-export-checklist.md).

- **Minimum cell size** — small cells must be masked/suppressed. The verified French
  health-data norm is **counts < 11 masked** (ATIH/ScanSanté; CASD PMSI rule — verbatim
  citations in `snds-export-rules.md` §3.1). On the CNAM portal the binding standard is
  qualitative (anonymous results, case-by-case expert review) with **no published number** —
  use ≥ 11 as the safe-harbor default, **confirm the exact threshold for your channel/DUA, and
  record it in `snds-data.md`**.
- **No individual re-identification** — no output (or combination of outputs) may allow a
  single beneficiary **or health professional** to be singled out. Watch complementary
  suppression / secret secondaire (a suppressed cell recoverable from margins — within a table
  or across exported tables — must also be protected).
- **Establishment-level / aggregate tables** (e.g. FICHSUP-type tables) are aggregates by
  construction — do not attempt to attribute an aggregate back to an individual.
- Document, for every exported artifact, which disclosure checks were applied (the export-gate
  annex in `export-compliance.md` §8 does this mechanically).

## 3. Secure-portal working constraints

- **Code must be correct before submission** — you cannot iteratively debug cheaply on the portal (queue time, shared DB). Develop logic carefully off-data, use defensive patterns (existence guards, `_v2` safe-replace), and verify with row counts.
- **Shared-quota discipline** — `ORAUSER` is shared and quota-limited; drop intermediary tables when a step is done; never leave large scratch tables behind.
- **Existence guards** — wrap year-/version-variant tables in `%sysfunc(exist(...))` checks (a missing table is a hard `proc sql` error). See `sas-sql-conventions.md` §5, §9.

## 4. Collaboration / RA handoff (if applicable)

When a co-analyst or RA owns part of the pipeline:

- Designate their scripts **read-only** (e.g. `analysis/scripts/[RA]/`); all your modifications live in a separate writable folder (e.g. `analysis/scripts/claude/`). Never edit someone else's pipeline file in place.
- Treat their outputs as inputs with a documented I/O contract (row counts + keys).

## Enforcement

- The `sas-reviewer` agent flags PII-in-logs, identifiers-on-shared-mounts, missing partition filters, and missing disclosure checks as **Critical**.
- Any export step must state, in a comment, the disclosure rule it satisfies.
