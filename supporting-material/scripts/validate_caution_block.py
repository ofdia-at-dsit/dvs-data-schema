#!/usr/bin/env python3
"""
Run the same check that .github/workflows/caution-block.yml runs in CI.

Exit 0 if every workspace Markdown file starts with the exact caution block.
Exit 1 otherwise and print the failing file paths.
"""
from pathlib import Path
import sys

REPO = Path(__file__).resolve().parents[2]

EXPECTED_LINE_1 = "> [!CAUTION]"
EXPECTED_LINE_2_PREFIX = "> This repository is a workspace copy"

EXCLUDE_PREFIXES = (
    ".github/",
    "docs-site/README.md",
    "docs-site/node_modules/",
    "node_modules/",
)


def is_excluded(rel: str) -> bool:
    return any(rel.startswith(pfx) for pfx in EXCLUDE_PREFIXES)


def main() -> int:
    fails: list[str] = []
    total = 0
    for path in sorted(REPO.rglob("*.md")):
        rel = path.relative_to(REPO).as_posix()
        if is_excluded(rel):
            continue
        total += 1
        lines = path.read_text(encoding="utf-8").splitlines()
        if len(lines) < 3:
            fails.append(rel + "  (file has fewer than 3 lines)")
            continue
        if lines[0] != EXPECTED_LINE_1:
            fails.append(rel + "  (line 1 mismatch)")
            continue
        if not lines[1].startswith(EXPECTED_LINE_2_PREFIX):
            fails.append(rel + "  (line 2 mismatch)")
            continue
        if lines[2] != "":
            fails.append(rel + "  (line 3 not blank)")
            continue
    print(f"{total} workspace Markdown files scanned.")
    if fails:
        print("FAIL:")
        for f in fails:
            print(f"  {f}")
        return 1
    print("OK: all files start with the expected caution block.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
