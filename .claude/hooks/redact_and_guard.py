#!/usr/bin/env python3
import json
import re
import sys

payload = json.load(sys.stdin)
tool_input = payload.get("tool_input", {})
command = tool_input.get("command", "")

# Hard block direct pushes to main
if re.search(r"\bgit\s+push\b.*\bmain\b", command):
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": "Direct pushes to main are blocked by PreToolUse hook.",
        }
    }
    print(json.dumps(output))
    sys.exit(0)

# Redact live secrets while preserving all other tool_input fields
if re.search(r"sk_live_[A-Za-z0-9_]+", command):
    updated_input = dict(tool_input)
    updated_input["command"] = re.sub(
        r"sk_live_[A-Za-z0-9_]+", "sk_live_REDACTED", command
    )
    output = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "permissionDecisionReason": "Redacted live API secret before execution.",
            "updatedInput": updated_input,
        }
    }
    print(json.dumps(output))
    sys.exit(0)

sys.exit(0)
