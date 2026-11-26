# Claude Code Workflows

Reference implementation and distributable Claude Code plugin covering end-to-end agentic engineering patterns:
- **Worktree Isolation (`.worktreeinclude`):** Shares local git-ignored files across parallel agent worktrees.
- **Layered Guidance (`CLAUDE.md`):** Lean root instructions with modular `@` imports (`.claude/conventions/`) and git-ignored `CLAUDE.local.md`.
- **Verification Skills (`.claude/skills/verify-changes/`):** Automated unit test execution and `git diff` assertion auditing (`SKILL.md`, `reference.md`, `check.sh`).
- **Permission Modes & Stop Hooks (`.claude/settings.json`):** Pre-approved allowlists for unattended `dontAsk` runs paired with `exit 2` post-turn verification.
- **Deterministic Guardrails (`.claude/hooks/`):** `PreToolUse` secret redaction (`updatedInput`) and `main`-branch push blocking, `PostToolUse` syntax/type enforcement (`exit 2`), and `SessionStart` (`compact`) state recovery.
- **Headless CI, Cold Review & Agent SDK (`scripts/`):** Deterministic `--bare` JSON-schema pipelines (`ci_audit.sh`), stateless diff review (`cold_review.sh`), and programmatic SDK options (`agent_sdk_runner.py`).
- **GitHub Actions (`.github/workflows/`):** `@claude` comment-driven PR automation (`claude.yaml`) and scheduled read-only audits (`claude-daily-audit.yaml`).
- **Distributable Plugin Packaging (`.claude-plugin/plugin.json`):** Versioned manifest, namespaced skills (`/claude-code-workflows:verify-changes`), `agents/cold-reviewer.md`, and `hooks/hooks.json`.
