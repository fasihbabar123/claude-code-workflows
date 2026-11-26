# Claude Code Workflows

Reference implementation of Claude Code architectural patterns:
- **Worktree Isolation (`.worktreeinclude`):** Shares local git-ignored files across parallel agent worktrees.
- **Layered Guidance (`CLAUDE.md`):** Lean root instructions with modular `@` imports (`.claude/conventions/`) and git-ignored `CLAUDE.local.md`.
- **Verification Skills (`.claude/skills/verify-changes/`):** Automated unit test execution and `git diff` assertion auditing (`SKILL.md`, `reference.md`, `check.sh`).
- **Permission Modes & Stop Hooks (`.claude/settings.json`):** Pre-approved allowlists for unattended `dontAsk` runs paired with post-turn verification.
- **Deterministic Guardrails (`.claude/hooks/`):** `PreToolUse` secret redaction (`updatedInput`) and `main`-branch push blocking, plus `SessionStart` (`compact`) state recovery.
- **Headless CI & Agent SDK (`scripts/`):** Deterministic `--bare` JSON-schema pipelines (`ci_audit.sh`) and programmatic SDK options (`agent_sdk_runner.py`).
