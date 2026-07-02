#!/usr/bin/env python3
"""
SNDS R-portal gate hook (PreToolUse, matcher Edit|Write).

Fires whenever a .R/.r file is about to be edited/written and injects the SNDS
R-portal provisioning gate + conventions into context, so the user is
AUTOMATICALLY prompted through the RStudio access procedure
(rules/snds-r-portal.md) instead of it just being documented.

Output: JSON with hookSpecificOutput.additionalContext on a .R/.r target;
nothing otherwise. Fails open — never blocks an edit if the hook errors.
"""

from __future__ import annotations

import json
import sys

GATE = """SNDS R-PORTAL GATE -- surface to the user BEFORE producing runnable R (rules/snds-r-portal.md):
(0) PROVISIONING: R is NOT auto-provisioned on the CNAM portal -- a new habilitation has SAS Guide ONLY. Before writing/running R meant for the portal, CONFIRM the user has RStudio Workbench. If not: email support-national@assurance-maladie.fr, subject must contain [Création Habilitation RStudio], with portal login id(s) + portal connection email + région/profil(s); ~1-2 weeks; then the RStudio Workbench icon appears beside SASGuide 8; use R 4.4.3. (CNAM "Procedures d'acces a R sur le portail SNDS", 04/03/2026.) R can be AUTHORED locally now, but say plainly it cannot RUN on the portal until habilitation lands.
(1) PACKAGES: personal install.packages() is BLOCKED; request via subject [Création Demande de package RSTUDIO] (not immediate). Already in prod: fixest, brglm2, ROracle, DBI, data.table, dplyr, dbplyr, ggplot2, sandwich, lmtest, modelsummary, broom, glue, lubridate, haven, tidyverse. NOT in prod (flag if used): marginaleffects, survey, binsreg, logistf.
(2) MEMORY capped per user -> CNAM prescribes the hybrid: datamanagement in SAS, modelisation/graphique in R, push to the Oracle engine maximally; keep large claims tables server-side, pull only the small aggregated/cohort-level result into R; gc()/data.table when tight.
(3) STORAGE shared SAS<->R (ORAUSER/sasdata1/project) -> read SAS-built ORAUSER tables directly. Home RStudio tiny: NEVER save there (use sasdata1/project). ORAUSER is not storage: drop *_R tables after use. Max 3 sessions.
(4) ORACLE-from-R: connect dbname="IPIAMPR2.WORLD" (TZ/ORA_SDTZ=Europe/Paris); UPPERCASE Oracle names; pure ASCII; two-step date rule (all-Oracle filter -> pull small -> DATEPART in R, never push date funcs into Oracle); filter FLX_DIS_DTD; GROUP BY raw cols only. Same disclosure discipline as SAS on anything R exports. Reuse a shared R/ helpers module if the project has one."""


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # fail open
    fp = (data.get("tool_input") or {}).get("file_path", "") or ""
    if not fp.endswith((".R", ".r")):
        return 0
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": GATE,
        }
    }
    print(json.dumps(output))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open — never block an edit due to a hook bug
