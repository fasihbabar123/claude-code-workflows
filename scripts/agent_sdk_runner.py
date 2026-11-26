#!/usr/bin/env python3
"""Reference wrapper demonstrating Claude Agent SDK query configuration."""
from typing import Any, Dict


def build_query_options() -> Dict[str, Any]:
    return {
        "allowed_tools": ["Read", "Bash"],
        "system_prompt": (
            "Follow project conventions in CLAUDE.md. "
            "Never modify or weaken assertions in tests/."
        ),
        "permission_mode": "dontAsk",
    }


if __name__ == "__main__":
    opts = build_query_options()
    print("Agent SDK query options initialized:", opts)
