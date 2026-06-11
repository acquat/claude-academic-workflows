---
name: sds-doc
description: Fetch SNDS (Système National des Données de Santé) documentation for a variable, table, code, or concept. Queries the authoritative sources (dico-snds, Health Data Hub training repo, kwikly) and returns a synthesized answer with citations. Use when uncertain about an SNDS variable name, table relationship, code list, or convention.
argument-hint: "<variable_or_table_or_concept>  (e.g. BEN_NIR_PSA, ER_PRS_F, PSP_SPE_COD, CCAM)"
allowed-tools: ["Read", "WebFetch", "Grep"]
---

# /sds-doc — SNDS documentation lookup

Fetch authoritative documentation for an SNDS variable, table, code list, or concept.

## Steps

1. **Read the local reference first.** Open `.claude/references/snds-data.md` and grep for `$ARGUMENTS`. If documented locally, return that answer (with the project convention noted) and stop.
2. **Else query the dico-snds** (authoritative variable dictionary): <https://health-data-hub.shinyapps.io/dico-snds/>. WebFetch with: *"Look up `$ARGUMENTS` in the SNDS data dictionary. Return: (a) exact definition, (b) table(s) it appears in, (c) nomenclature reference (CCAM/NABM/CIM-10/…), (d) whether it is a beneficiary identifier (PII), (e) modality codes / value lists."*
3. **For workflow/pattern questions**, consult the Health Data Hub training repo: <https://gitlab.com/healthdatahub/se-former-au-snds>.
4. **For structural questions** (e.g. DCIR/PMSI linkage), consult kwikly: <https://documentation-snds.health-data-hub.fr/snds/cnam/formations/kwikly/>.
5. **Synthesize and return:**
   ```markdown
   ### `[VARIABLE_OR_TABLE]`
   **Definition:** …
   **Table(s):** …
   **Type / format:** …
   **PII status:** identifier / non-identifier — flag if it cannot be exported
   **Project convention:** from snds-data.md if applicable, else "none"
   **Source(s):** URL(s) consulted, with access date
   ```
6. **Update the local reference** if the answer is reusable — *propose* (don't silently apply) an addition to `.claude/references/snds-data.md`. The user approves.

## Important rules

1. **Never guess.** If no authoritative source answers, return "Unable to confirm; recommend consulting your CNAM/data-provider contact" rather than fabricating.
2. **Cite every fact** — trace each to a URL or to `snds-data.md`.
3. **Flag PII identifiers** — anything in the `BEN_NIR_*` / `BEN_IDT_ANO` family is identifier-status: "do not export outside the secured environment."
