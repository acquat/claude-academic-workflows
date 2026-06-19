#!/usr/bin/env python3
"""
Protected-files guard (PreToolUse, matcher Edit|Write).

Blocks accidental Edit/Write to protected files (basename match). Primary use:
enforce a read-only RA / co-analyst pipeline handoff (snds-data-security.md
section 4) -- mark their pipeline files protected so all your edits land in
your own writable folder, never in someone else's file in place.

Exit 2 BLOCKS the edit (reason printed to stderr); exit 0 allows it.
Customize PROTECTED_PATTERNS below for your project.
Fails open (exit 0) on any parse error.
"""

from __future__ import annotations

import json
import os
import sys

# ============================================================
# CUSTOMIZE: basenames to protect for this project (basename match).
# ============================================================
PROTECTED_PATTERNS = [
    "settings.json",
    # "Bibliography_base.bib",   # example: a shared bibliography
    # "01_extract_cohort.sas",   # example: an RA-owned pipeline file (read-only handoff)
]


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # fail open
    fp = (data.get("tool_input") or {}).get("file_path", "") or ""
    if not fp:
        return 0  # not a file operation
    if os.path.basename(fp) in PROTECTED_PATTERNS:
        sys.stderr.write(
            "Protected file: %s -- edit it manually, or remove it from "
            "PROTECTED_PATTERNS in .claude/hooks/protect-files.py.\n"
            % os.path.basename(fp)
        )
        return 2  # block the edit
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open — never block an edit due to a hook bug
