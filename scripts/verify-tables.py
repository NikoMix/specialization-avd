"""Assert every Markdown table in content/ became a real <table> in public/.

Counts a source table as a header row followed by a delimiter row
(`|---|---|`), skipping fenced code blocks, then compares that count with the
number of `<table>` elements Hugo emitted for the same page.

Exit code 0 only when every page matches. Run after `hugo`.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CONTENT = Path("content")
PUBLIC = Path("public")

DELIM = re.compile(r"^\s*\|?\s*:?-{1,}:?\s*(\|\s*:?-{1,}:?\s*)+\|?\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")


def count_source_tables(md: str) -> int:
    body = md.split("+++", 2)[-1] if md.startswith("+++") else md
    lines = body.split("\n")
    in_fence = False
    total = 0
    for i, line in enumerate(lines):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if DELIM.match(line) and i and lines[i - 1].strip().startswith("|"):
            total += 1
    return total


def out_path(src: Path) -> Path:
    rel = src.relative_to(CONTENT)
    stem = rel.parent if rel.name == "_index.md" else rel.with_suffix("")
    return PUBLIC / stem / "index.html"


def main() -> int:
    if not PUBLIC.is_dir():
        print("public/ not found — run hugo first", file=sys.stderr)
        return 2

    failures, checked, tables = [], 0, 0
    for src in sorted(CONTENT.rglob("*.md")):
        expected = count_source_tables(src.read_text(encoding="utf-8"))
        html_file = out_path(src)
        if not html_file.is_file():
            failures.append(f"{src}: no rendered page at {html_file}")
            continue
        html = html_file.read_text(encoding="utf-8")
        actual = html.count("<table")
        checked += 1
        tables += expected
        if actual != expected:
            failures.append(f"{src}: {expected} Markdown tables but {actual} <table> in {html_file}")
        # A table that degraded into an indented code block shows up as a
        # pipe-prefixed line inside <pre>.
        for block in re.findall(r"<pre[^>]*>(.*?)</pre>", html, re.S):
            if re.search(r"^\s*\|.*\|", block, re.M):
                failures.append(f"{src}: table-looking content rendered inside <pre>")
                break

    for f in failures:
        print("FAIL", f)
    print(f"checked {checked} pages, {tables} Markdown tables, {len(failures)} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
