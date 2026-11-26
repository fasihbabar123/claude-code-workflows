#!/usr/bin/env bash
set -euo pipefail

SCHEMA='{"type":"object","properties":{"verdict":{"type":"string","enum":["approve","request_changes"]},"findings":{"type":"array","items":{"type":"string"}}},"required":["verdict","findings"]}'

if [[ "${1:-}" == "--dry-run" ]]; then
  echo "Cold second-opinion review command configured:"
  echo "git diff HEAD | claude -p \"You have no prior context. Independently review this diff against CLAUDE.md for bugs, missing edge cases, or unintended file edits.\" --output-format json --json-schema '$SCHEMA'"
  exit 0
fi

if [[ -z "${ANTHROPIC_API_KEY:-}" ]]; then
  echo "ERROR: ANTHROPIC_API_KEY must be set to run headless cold review." >&2
  exit 1
fi

DIFF_CONTENT=$(git diff HEAD)
if [[ -z "$DIFF_CONTENT" ]]; then
  echo "No uncommitted changes in git diff HEAD to review."
  exit 0
fi

RESPONSE=$(printf "%s" "$DIFF_CONTENT" | claude -p \
  "You have no prior context. Independently review this diff against CLAUDE.md for bugs, missing edge cases, or unintended file edits." \
  --output-format json \
  --json-schema "$SCHEMA")

echo "$RESPONSE" | jq '.structured_output'
