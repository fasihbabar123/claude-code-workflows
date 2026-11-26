#!/usr/bin/env python3
import ast
import json
import py_compile
import sys
from pathlib import Path

payload = json.load(sys.stdin)
tool_input = payload.get("tool_input", {})
file_path = tool_input.get("file_path", "")

if not file_path or not file_path.endswith(".py"):
    sys.exit(0)

path = Path(file_path)
if not path.exists():
    sys.exit(0)

try:
    py_compile.compile(str(path), doraise=True)
except py_compile.PyCompileError as exc:
    print(f"Syntax error in {file_path}: {exc}", file=sys.stderr)
    sys.exit(2)

# Enforce type annotations on functions in src/ per CLAUDE.md
if "src" in path.parts:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            missing_args = [
                arg.arg for arg in node.args.args if arg.annotation is None
            ]
            if missing_args or node.returns is None:
                print(
                    f"Type annotation check failed in {file_path}:{node.lineno} "
                    f"for function '{node.name}'. Add parameter and return type hints.",
                    file=sys.stderr,
                )
                sys.exit(2)

sys.exit(0)
