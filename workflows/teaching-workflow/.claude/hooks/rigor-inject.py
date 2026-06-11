#!/usr/bin/env python3
"""
Rigor Injection Hook

Fires on SessionStart (startup, resume, compact, clear) and injects the
research-rigor standard into context, so every session is rigorous by default
without the user having to invoke /rigor.

The standard is read from the rigor skill's SKILL.md — looked up first in the
project (.claude/skills/rigor/, relative to this script, so a project-local
copy wins as the single source of truth), then in Claude Code's personal
skills directory (~/.claude/skills/rigor/, where this repo's INSTALL step
puts it). Either location works with no edits.

Hook Event: SessionStart
Output: JSON with hookSpecificOutput.additionalContext
Fails open — never blocks a session if the rigor skill is missing or unreadable.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def load_rigor_standard() -> str | None:
    """Read the rigor skill body: project-local copy first, then the
    personal skills directory."""
    candidates = [
        Path(__file__).resolve().parent.parent / "skills" / "rigor" / "SKILL.md",
        Path.home() / ".claude" / "skills" / "rigor" / "SKILL.md",
    ]
    skill_path = next((p for p in candidates if p.exists()), None)
    if skill_path is None:
        return None
    try:
        text = skill_path.read_text(encoding="utf-8")
    except OSError:
        return None

    # Strip YAML frontmatter (--- ... ---) if present; keep the body.
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            text = parts[2]
    return text.strip()


def main() -> int:
    # Drain stdin (SessionStart delivers JSON there); we don't need it.
    try:
        sys.stdin.read()
    except Exception:
        pass

    standard = load_rigor_standard()
    if not standard:
        return 0  # fail open — no rigor skill present, nothing to inject

    context = (
        "ACTIVE STANDARD — Research Rigor applies to ALL analytical and "
        "quantitative work this session, as if /rigor were already invoked. "
        "Follow it without waiting to be asked:\n\n"
        + standard
    )

    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
        }
    }
    print(json.dumps(output))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # Fail open — never block session start due to a hook bug.
        sys.exit(0)
