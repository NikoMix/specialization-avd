#!/usr/bin/env python3
"""Assert every internal link in the built site resolves to a real file.

The theme's link render hook only warns about *broken relative* links — it
treats any absolute path as intentional — and this site links between pages
with absolute logical paths. That leaves absolute links, menu entries,
shortcode hrefs and static downloads unchecked, which is exactly where a
GitHub Pages sub-path (`/<repo>/`) goes wrong. This checks them all against
what Hugo actually wrote to public/.

Run after `hugo`. Exit code 0 only when every internal link resolves.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

PUBLIC = Path("public")
# `hugo --minify` drops quotes around attribute values wherever HTML5 allows
# it, so an href-must-be-quoted regex silently matches almost nothing.
HREF = re.compile(
    r"""(?:href|src)\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>"'`=]+))""",
    re.I,
)
SKIP_SCHEMES = ("http:", "https:", "mailto:", "tel:", "data:", "javascript:")


def base_path() -> str:
    """Site sub-path, taken from the shortest URL Hugo put in the sitemap."""
    sitemap = PUBLIC / "sitemap.xml"
    if not sitemap.is_file():
        return "/"
    locs = re.findall(r"<loc>([^<]+)</loc>", sitemap.read_text(encoding="utf-8"))
    if not locs:
        return "/"
    root = min(locs, key=len)
    path = urlparse(root).path
    return path if path.endswith("/") else path.rsplit("/", 1)[0] + "/"


def resolves(target: Path) -> bool:
    if target.is_file():
        return True
    if (target / "index.html").is_file():
        return True
    return target.with_suffix(".html").is_file()


def main() -> int:
    if not PUBLIC.is_dir():
        print("public/ not found — run hugo first", file=sys.stderr)
        return 2

    base = base_path()
    failures: list[str] = []
    checked = 0

    for html_file in sorted(PUBLIC.rglob("*.html")):
        for raw in HREF.findall(html_file.read_text(encoding="utf-8")):
            link = next((g for g in raw if g), "").strip()
            if not link or link.startswith("#") or link.startswith("//"):
                continue
            if link.lower().startswith(SKIP_SCHEMES):
                continue
            path = unquote(urlparse(link).path)
            if not path:
                continue

            if path.startswith("/"):
                if base != "/" and not path.startswith(base):
                    failures.append(
                        f"{html_file.relative_to(PUBLIC)}: {link!r} is missing the "
                        f"site base path {base!r} and will 404 on GitHub Pages"
                    )
                    continue
                target = PUBLIC / path[len(base):].lstrip("/")
            else:
                target = (html_file.parent / path).resolve()
                try:
                    target.relative_to(PUBLIC.resolve())
                except ValueError:
                    failures.append(f"{html_file.relative_to(PUBLIC)}: {link!r} escapes the site root")
                    continue

            checked += 1
            if not resolves(target):
                failures.append(f"{html_file.relative_to(PUBLIC)}: {link!r} -> missing {target}")

    for f in sorted(set(failures)):
        print("FAIL", f)
    print(f"base path {base!r}; checked {checked} internal links, {len(set(failures))} failures")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
