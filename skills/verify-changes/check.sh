#!/usr/bin/env bash
set -euo pipefail

echo "=== Gate 1: Running Unit Test Suite ==="
if ! python3 -m unittest discover -s tests -v; then
  echo "FAIL: Unit test suite failed." >&2
  exit 2
fi

echo ""
echo "=== Gate 2 & 3: Auditing Git Diff for Weakened or Skipped Tests ==="
if git rev-parse --verify HEAD >/dev/null 2>&1; then
  DIFF_OUTPUT=$(git diff -- tests/ || true)
  if echo "$DIFF_OUTPUT" | grep -E '^-.*assert|^\+.*(skipTest|unittest\.skip)' >/dev/null; then
    echo "FAIL: Detected removed assertion or skipped test in tests/." >&2
    exit 2
  fi
  git diff --stat
fi

echo ""
echo "PASS: All verification gates succeeded."
