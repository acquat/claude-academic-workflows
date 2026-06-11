#!/usr/bin/env python3
"""PostToolUse(Write|Edit) nudge: an edited artifact isn't done until verified.

Prints a one-line reminder when a substantive artifact type is written,
per rules/verification-protocol.md. Quiet otherwise. A reminder must never
break a session, so every failure path is silent.
"""
import json
import os
import sys

ARTIFACT_SUFFIXES = (".tex", ".sas", ".do", ".R", ".r", ".qmd", ".xlsx")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        path = (payload.get("tool_input") or {}).get("file_path", "")
        if path.endswith(ARTIFACT_SUFFIXES):
            print(
                f"[verify] {os.path.basename(path)} changed — run the checklist in "
                ".claude/rules/verification-protocol.md before declaring done."
            )
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
