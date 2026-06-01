#!/usr/bin/env python3
"""
KI-4 — Rewrite cross-file fragment anchors in schema-1.0/ Markdown files.

Same-file anchor links (for example ``[claims](#claims)`` inside
``03-data-model.md`` where ``### Claims`` lives) are left alone.

Cross-file anchor links (for example ``[language](#language)`` inside
``03-data-model.md`` where ``#### Language`` now lives in
``04-data-dictionary.md``) are rewritten to point at the target file.

Deterministic and idempotent — only rewrites bare ``#anchor`` links that
map to a different file within the same guide folder. Links that already
have a file prefix are left alone, so a second run is a no-op.

Usage::

    python3 supporting-material/scripts/apply_cross_file_links.py
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[2]

# Anchor → target file within the same guide folder. Anchors not listed
# here are assumed to live in the same file as the link and are left alone.
GPG45_CROSS_FILE = {
    "language": "04-data-dictionary.md",
    "date": "04-data-dictionary.md",
    "timestamp": "04-data-dictionary.md",
    "country-code": "04-data-dictionary.md",
    "encoding": "04-data-dictionary.md",
    "nationality": "04-data-dictionary.md",
    "predefined-lists": "06-predefined-lists.md",
    "predefined-values": "05-predefined-values.md",
}

# GPG 44 source has no internal #anchor links, so no map needed.
GPG44_CROSS_FILE: dict[str, str] = {}

LINK_RE = re.compile(r"\[([^\]]+)\]\(#([^)]+)\)")


def rewrite_file(path: Path, cross_map: dict[str, str]) -> int:
    """Rewrite bare ``#anchor`` links in *path* whose anchor maps to a
    different file. Returns the number of rewrites."""
    text = path.read_text(encoding="utf-8")
    current_file = path.name
    count = 0

    def sub(m: re.Match) -> str:
        nonlocal count
        link_text = m.group(1)
        anchor = m.group(2)
        target = cross_map.get(anchor)
        if target is None or target == current_file:
            return m.group(0)
        count += 1
        return f"[{link_text}]({target}#{anchor})"

    new_text = LINK_RE.sub(sub, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return count


def main() -> int:
    total = 0
    for p in sorted((REPO / "schema-1.0" / "gpg-45").glob("*.md")):
        n = rewrite_file(p, GPG45_CROSS_FILE)
        if n:
            print(f"  {p.relative_to(REPO)}: {n} rewrites")
            total += n
    for p in sorted((REPO / "schema-1.0" / "gpg-44").glob("*.md")):
        n = rewrite_file(p, GPG44_CROSS_FILE)
        if n:
            print(f"  {p.relative_to(REPO)}: {n} rewrites")
            total += n
    print(f"Total rewrites: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
