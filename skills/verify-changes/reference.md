# Verification Gate Criteria

- **Gate 1 — Unit Test Execution:** All tests under `tests/` must pass with exit code `0`.
- **Gate 2 — Assertion Integrity:** Existing `assert*` calls in `tests/` must not be deleted or loosened to force a green build.
- **Gate 3 — No Skipped Tests:** Adding `@unittest.skip` or `skipTest` to bypass failures is prohibited.
