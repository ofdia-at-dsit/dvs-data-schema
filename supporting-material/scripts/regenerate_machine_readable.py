#!/usr/bin/env python3
"""
Regenerate machine-readable exports under
`supporting-material/machine-readable/gpg-45/` and `.../gpg-44/`.

At launch this script is a thin wrapper that re-runs the generator used to
seed the repository. The canonical source for the derived artefacts is the
published Markdown under `schema-1.0/` — a future iteration will parse those
files directly rather than hard-coding the tables here.

Usage:
    python3 supporting-material/scripts/regenerate_machine_readable.py
"""
from pathlib import Path
import subprocess
import sys

REPO = Path(__file__).resolve().parents[2]


def main() -> int:
    print("regenerate_machine_readable.py")
    print("  REPO:", REPO)
    print("  This script is a placeholder that will, in a future iteration,")
    print("  parse the published Markdown under schema-1.0/ and rewrite the")
    print("  files in supporting-material/machine-readable/ deterministically.")
    print()
    print("  For now, the derived artefacts are hand-seeded and kept in sync")
    print("  by reviewers at PR time. See KNOWN-ISSUES.md (KI-1) for the")
    print("  broader cleanup work that precedes automated regeneration.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
