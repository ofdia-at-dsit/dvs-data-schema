#!/usr/bin/env python3
"""
KI-1 — Convert GOV.UK publishing ``$E ... $E`` fenced blocks to HTML
``<pre class="schema-example">`` elements.

Inside each block:

* ``&nbsp;`` entities are converted to regular spaces (GOV.UK renders each
  ``&nbsp;`` as a visible non-breaking space, so a direct space replacement
  preserves the visual indentation).
* Blank lines between schema fields are dropped. The source inserts a blank
  line after each field — a GOV.UK export artefact. Left in place they
  render as visible vertical gaps inside ``<pre>``.
* Markdown inline links ``[text](href)`` become ``<a href="href">text</a>``
  so cross-references between schema elements remain clickable.
* Trailing whitespace per line is stripped.

Deterministic and idempotent: after the first run the file contains no
``$E`` markers, so a second run finds nothing to convert.

Usage::

    python3 supporting-material/scripts/convert_schema_examples.py
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parents[2]

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

DOLLAR_E_BLOCK = re.compile(
    r"^\$E[ \t]*\n(.*?)^\$E[ \t]*$",
    re.MULTILINE | re.DOTALL,
)


def convert_block(content: str) -> str:
    """Convert the body of a single ``$E ... $E`` block to HTML-safe text."""
    # Drop blank lines (export-artefact gaps between each field).
    lines = [ln for ln in content.split("\n") if ln.strip() != ""]
    # Convert &nbsp; entities to regular spaces.
    lines = [ln.replace("&nbsp;", " ") for ln in lines]
    # Strip trailing whitespace per line.
    lines = [ln.rstrip() for ln in lines]
    body = "\n".join(lines)
    # Convert Markdown links to HTML <a> elements.
    def link_sub(m: re.Match) -> str:
        text = m.group(1)
        href = m.group(2)
        return f'<a href="{href}">{text}</a>'

    return LINK_RE.sub(link_sub, body)


def convert_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    count = 0

    def sub(m: re.Match) -> str:
        nonlocal count
        count += 1
        body = convert_block(m.group(1))
        return f'<pre class="schema-example">\n{body}\n</pre>'

    new_text = DOLLAR_E_BLOCK.sub(sub, text)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return count


def main() -> int:
    total = 0
    for guide in ("gpg-45", "gpg-44"):
        for p in sorted((REPO / "schema-1.0" / guide).glob("*.md")):
            n = convert_file(p)
            if n:
                print(f"  {p.relative_to(REPO)}: {n} $E blocks converted")
                total += n
    print(f"Total blocks converted: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
