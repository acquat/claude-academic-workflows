---
paths:
  - "**/*.R"
  - "**/*.r"
  - "R/**"
---

# SNDS R Portal — Provisioning Gate + Conventions

**Trigger this whenever the user asks to write, run, port, or debug ANY R for an SNDS project.**

---

## 0. PROVISIONING GATE (surface this FIRST, before writing/running R)

R is **not** provisioned automatically on the CNAM SNDS portal. A new habilitation gets **only
SAS Guide** — R/RStudio must be requested separately. **Before producing R that is meant to run on
the portal, confirm the user has RStudio Workbench provisioned.** If it is not confirmed, surface
this procedure and offer to help draft the request:

> **Request RStudio Workbench** — email **support-national@assurance-maladie.fr**, subject must
> contain **`[Création Habilitation RStudio]`**, providing: portal login id(s), portal connection
> email, and the **région + profil(s)** for R access (one request can batch several users of an
> institution; internal Assurance-Maladie users go via the S@M app). Habilitation lands in **~1–2
> weeks**; the **RStudio Workbench** icon then appears beside SASGuide 8. Use R **4.4.3**.

Authoritative source: CNAM communiqué *"Procédures d'accès à R sur le portail SNDS"* (04/03/2026).
Writing R *code* locally with Claude Code is fine before provisioning — but say plainly that it
**cannot be run on the portal** until the habilitation lands, so we don't imply it's runnable.

## 1. Packages — gated; request before you depend on one

Personal `install.packages()` is **BLOCKED** on the portal. New packages are requested via
support-national, subject **`[Création Demande de package RSTUDIO]`** (security-reviewed; NOT
installed immediately). The live list is on the portal Accueil → "Pour votre information".

Already in CNAM prod (`Packages_R_prod_17112025.xlsx`, verified 2026-06-18): **fixest**, **brglm2**
(Firth), ROracle, DBI, data.table, dplyr, dbplyr, ggplot2, sandwich, lmtest, modelsummary, broom,
glue, lubridate, haven, tidyverse. **Not** in prod (request first, or flag before using):
`marginaleffects`, `survey`, `binsreg`, `logistf`. → Don't write code that depends on an
un-provisioned package without flagging it to the user.

## 2. Operational constraints (CNAM Accès-à-R guide)

- **Per-user memory is capped** ("Cannot allocate memory" is common). CNAM's own prescription is a
  **hybrid**: **datamanagement in SAS, modélisation/graphique in R, push work to the Oracle engine
  maximally.** Keep the large claims tables server-side; pull only the small aggregated /
  cohort-level result (the analysis-ready extract) into R. Use `gc()` / data.table when tight.
- **Storage is shared SAS↔R** (sasdata1, project spaces, ORAUSER) → SAS-built ORAUSER tables can be
  read directly from R, no re-export.
- **Home RStudio is tiny / system-reserved — never save there.** RDS + outputs go to sasdata1 or a
  project space. **ORAUSER is not storage — drop any temp (`*_R`) table after use.** Max 3
  simultaneous sessions.

## 3. Conventions for R that hits Oracle (mirror the SAS discipline)

- Connect: `Sys.setenv(TZ="Europe/Paris", ORA_SDTZ="Europe/Paris"); DBI::dbConnect(DBI::dbDriver("Oracle"), dbname="IPIAMPR2.WORLD")`.
  Query with `DBI::dbGetQuery` (SQL) or `dplyr`/`dbplyr`.
- **Oracle table names UPPERCASE**, start with a letter. **Pure ASCII** in scripts (the portal is
  Latin-1).
- **Two-step date rule:** do all-Oracle filtering with translatable predicates → pull the small
  result → derive DATEPART / year / interval expressions **in R**. Never push R/SAS date functions
  into Oracle SQL (they translate to a **silent NULL**). Filter on the **partition key**
  (`FLX_DIS_DTD`); **GROUP BY raw columns only**.
- Same disclosure discipline as SAS applies to anything R exports — identifier-class variables stay
  in the enclave and every export passes the ≥ 11 gate (see cross-references below).
- If your project has a shared `R/` helpers module (connect / query / export-gate wrappers), reuse
  it rather than re-rolling these per script.

## 4. Cross-references
Security + PII: [`snds-data-security.md`](snds-data-security.md) · Export gate (≥ 11, annex):
[`export-compliance.md`](export-compliance.md) · Oracle/SQL discipline (partition key, joins,
safe-replace): [`sas-sql-conventions.md`](sas-sql-conventions.md) · Project tables / code lists /
DUA threshold: [`references/snds-data.md`](../references/snds-data.md).
CNAM bonnes pratiques R: documentation-snds.health-data-hub.fr/snds/CNAM/bonnes_pratiques_r/.
