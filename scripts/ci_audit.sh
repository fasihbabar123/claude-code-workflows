#!/usr/bin/env bash
set -euo pipefail

SCHEMA='{"type":"object","properties":{"status":{"type":"string","enum":["pass","fail"]},"issues":{"type":"array","items":{"type":"string"}}},"required":["status","issues"]}'

if [[ "${1:-}" == "--dry-run" ]]; then
  echo "Headless CI command configured:"
  echo "claude -p \"Audit src/ for missing type hints or domain validation\" --bare --settings .claude/settings.json --output-format json --json-schema '$SCHEMA'"
  exit 0
fi

if [[ -z "${ANTHROPIC_API_KEY:-}" ]]; then
  echo "ERROR: ANTHROPIC_API_KEY must be set when running claude --bare in CI." >&2
  exit 1
fi

RESULT=$(claude -p "Audit src/ for missing type hints or domain validation" \
  --bare \
  --settings .claude/settings.json \
  --output-format json \
  --json-schema "$SCHEMA")

echo "$RESULT" | jq '.structured_output'
