#!/usr/bin/env python3
"""
New-skill -> website-update reminder (PostToolUse, matcher Write).

Fires when a new skill's SKILL.md is written under a skills/ directory
(.../skills/<name>/SKILL.md) and reminds the user to update her public-facing
website materials so the new skill is documented. Per a standing request:
developing a new skill should prompt a website-materials update.

A hook cannot open a new app window, so it (1) shows a direct systemMessage to
the user and (2) injects additionalContext telling Claude to offer either to do
the update now or to spawn a separate background task (its own session) for it.

Detection note: keys on a Write of SKILL.md (a new skill is created with Write;
editing an existing skill uses Edit, which this matcher excludes). A Write that
overwrites an existing SKILL.md will also fire — an acceptable, cheap over-trigger.

Fails open; silent for any write that is not a skill's SKILL.md.
"""

from __future__ import annotations

import json
import os
import sys


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # fail open

    fp = (data.get("tool_input") or {}).get("file_path", "") or ""
    if os.path.basename(fp) != "SKILL.md":
        return 0
    parts = fp.replace("\\", "/").rstrip("/").split("/")
    # expect .../skills/<name>/SKILL.md  -> parts[-3] == "skills"
    if len(parts) < 3 or parts[-3] != "skills":
        return 0
    skill = parts[-2]

    message = (
        f"New skill '{skill}' created. Reminder: update your public-facing website "
        f"materials so it's documented (repo README + your site)."
    )
    context = (
        f"NEW SKILL CREATED: '{skill}' ({fp}). Per the user's standing request, a new skill "
        f"should prompt a website-materials update. Surface this to the user now and OFFER to "
        f"either (a) update the public-facing materials in this session (the repo README's "
        f"workflow/skill description and her website), or (b) spawn a separate background task "
        f"(its own session) so it does not derail the current work. Any public-facing copy is in "
        f"her name: apply /writing-style-guide first and show the draft before applying."
    )
    output = {
        "systemMessage": message,
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": context,
        },
    }
    print(json.dumps(output))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open — never disrupt an edit due to a hook bug
