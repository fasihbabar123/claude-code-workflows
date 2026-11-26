---
name: verify-changes
description: Automatically verify code changes after any refactor, bug fix, or feature implementation by running the test suite and checking git diffs for weakened tests.
---
# Post-Change Verification Procedure

1. Execute `.claude/skills/verify-changes/check.sh` to run the test suite and diff audit.
2. Check the output against the gate definitions in `reference.md`.
3. Report PASS or FAIL with the exact test count and diff summary attached.
