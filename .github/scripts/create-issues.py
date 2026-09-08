#!/usr/bin/env python3
"""Create one GitHub issue per Azure Virtual Desktop audit requirement.

The issue bodies are generated *from the audit guide itself* — the
`## Required Evidence Checklist` table on every Module A / Module B control
page, and the `## Quick Readiness Checklist` table on the pre-qualification
page. That keeps the docs and the issue checkboxes a single source of truth:
reword an evidence item and the next run of this workflow picks it up, with no
second edit to maintain here.

Existing issue titles carrying this cycle's label are skipped, so the workflow
is safe to re-run and only creates what does not already exist.

Environment:
  GH_TOKEN      token with issues:write
  REPO          owner/repo
  CYCLE_LABEL   e.g. audit-2026
  MILESTONE     milestone title, e.g. "Audit 2026"
  GRANULARITY   control (default) | requirement
  DRY_RUN       set to "true" to print instead of creating
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Windows consoles default to cp1252; the audit guide is full of en dashes and
# checkbox glyphs, so force UTF-8 rather than crashing on print().
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CONTENT = Path("content/docs")
REPO = os.environ.get("REPO", "")
CYCLE_LABEL = os.environ.get("CYCLE_LABEL", "audit-unknown")
MILESTONE = os.environ.get("MILESTONE", "")
GRANULARITY = os.environ.get("GRANULARITY", "control").strip().lower()
DRY_RUN = os.environ.get("DRY_RUN", "").lower() == "true"

MODULES = {
    "module-a": ("Module A – Azure Essentials", "module-a"),
    "module-b": ("Module B – Azure Virtual Desktop", "module-b"),
}


# --------------------------------------------------------------------------- #
# parsing
# --------------------------------------------------------------------------- #
@dataclass
class Control:
    module_dir: str
    slug: str
    control_id: str
    name: str
    evidence: list[tuple[str, str, str]] = field(default_factory=list)
    gaps: list[str] = field(default_factory=list)

    @property
    def title(self) -> str:
        return f"{self.control_id} {self.name}"


def front_matter_title(text: str) -> str:
    m = re.search(r"^title\s*=\s*'(.*)'\s*$", text, re.M)
    if not m:
        raise ValueError("no title in front matter")
    return m.group(1)


def section(text: str, heading: str) -> str:
    """Body of a `## heading` up to the next `## `."""
    m = re.search(rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s|\Z)", text, re.M | re.S)
    return m.group(1) if m else ""


def table_rows(block: str) -> list[list[str]]:
    rows = []
    for line in block.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        if not cells or all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
            continue
        rows.append(cells)
    return rows[1:] if rows else []  # drop the header row


def plain(md: str) -> str:
    """Markdown cell -> issue-safe text: in-site links become their label."""
    md = re.sub(r"\[([^\]]+)\]\((?!https?://)[^)]*\)", r"\1", md)
    return md.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&").strip()


def parse_control(path: Path) -> Control:
    text = path.read_text(encoding="utf-8")
    title = front_matter_title(text)
    control_id, _, name = title.partition("–")
    ctrl = Control(
        module_dir=path.parent.name,
        slug=path.stem,
        control_id=control_id.strip(),
        name=name.strip() or title.strip(),
    )

    for cells in table_rows(section(text, "Required Evidence Checklist")):
        if len(cells) >= 3:
            ctrl.evidence.append((cells[0], plain(cells[1]), plain(cells[2])))

    gaps_block = section(text, "Common Gaps")
    gap_rows = table_rows(gaps_block)
    if gap_rows:
        ctrl.gaps = [plain(c[0]) for c in gap_rows if c]
    else:
        ctrl.gaps = [plain(m) for m in re.findall(r"^-\s+(.*)$", gaps_block, re.M)]
    return ctrl


# --------------------------------------------------------------------------- #
# issue bodies
# --------------------------------------------------------------------------- #
def page_url(module_dir: str, slug: str) -> str:
    owner, _, repo = REPO.partition("/")
    if not owner:
        return f"/docs/{module_dir}/{slug}/"
    return f"https://{owner.lower()}.github.io/{repo}/docs/{module_dir}/{slug}/"


def control_body(c: Control) -> str:
    module_label = MODULES[c.module_dir][0]
    lines = [
        f"## {c.control_id} — {c.name}",
        "",
        f"Evidence collection for **{module_label}**, control **{c.control_id}**.",
        "",
        f"- Control page: {page_url(c.module_dir, c.slug)}",
        f"- Source: `content/docs/{c.module_dir}/{c.slug}.md`",
        "",
        f"### Required evidence ({len(c.evidence)} items)",
        "",
    ]
    for num, item, fmt in c.evidence:
        lines.append(f"- [ ] **{num}.** {item} — _accepted: {fmt}_")

    if c.module_dir == "module-b":
        lines += [
            "",
            "### Per-customer evidence",
            "",
            "Module B is evidenced from two unique customer engagements delivered in "
            "the last 12 months, at least one of which must be Native AVD.",
            "",
            "- [ ] Customer 1 (Native AVD) — all items above collected",
            "- [ ] Customer 2 — all items above collected",
        ]

    if c.gaps:
        lines += ["", "### Common gaps to avoid", ""]
        lines += [f"- {g}" for g in c.gaps[:6]]

    lines += [
        "",
        "### Sign-off",
        "",
        f"- [ ] Evidence filed in `evidence/{c.module_dir}/{c.control_id}/`",
        "- [ ] Owner assigned and status tracked in the evidence tracker",
        "- [ ] Internal peer review complete",
    ]
    return "\n".join(lines) + "\n"


def requirement_body(c: Control, num: str, item: str, fmt: str) -> str:
    done = ["- [ ] Artefact produced or located"]
    if c.module_dir == "module-b":
        done += [
            "- [ ] Customer 1 (Native AVD) copy filed",
            "- [ ] Customer 2 copy filed",
        ]
    done += [
        f"- [ ] Filed in `evidence/{c.module_dir}/{c.control_id}/`",
        "- [ ] Internal peer review complete",
    ]
    return "\n".join(
        [
            f"## {c.control_id} evidence item {num}",
            "",
            f"**{item}**",
            "",
            f"- Accepted formats: {fmt}",
            f"- Control page: {page_url(c.module_dir, c.slug)}",
            f"- Parent control: {c.control_id} — {c.name}",
            "",
            "### Done when",
            "",
            *done,
            "",
        ]
    )


def prequal_body() -> str:
    text = (CONTENT / "requirements.md").read_text(encoding="utf-8")
    rows = table_rows(section(text, "Quick Readiness Checklist"))
    lines = [
        "## Pre-Qualification Gate (AVD V2.7.1)",
        "",
        "Confirm every pre-qualification requirement is met **before** requesting "
        "the audit from Partner Center.",
        "",
        "- Source: `content/docs/requirements.md`",
        "",
        "### Readiness checklist",
        "",
    ]
    for cells in rows:
        if len(cells) >= 2:
            lines.append(f"- [ ] **{cells[0]}** {plain(cells[1])}")
    lines += [
        "",
        "### Audit scheduling",
        "",
        "- [ ] Audit requested via Partner Center",
        "- [ ] Auditor (ISSI) assignment received",
        "- [ ] Kickoff call scheduled",
        "- [ ] Module scope confirmed: Module B only (4h, $2,400) vs Module A + B (8h, $3,600)",
    ]
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# github
# --------------------------------------------------------------------------- #
def existing_titles() -> set[str]:
    out = subprocess.run(
        ["gh", "issue", "list", "--repo", REPO, "--state", "all",
         "--label", CYCLE_LABEL, "--limit", "500", "--json", "title"],
        check=True, capture_output=True, text=True,
    ).stdout
    return {i["title"] for i in json.loads(out or "[]")}


def create_issue(title: str, labels: list[str], body: str, seen: set[str]) -> bool:
    if title in seen:
        print(f"skip (exists): {title}")
        return False
    if DRY_RUN:
        print(f"--- would create: {title}\n{body}")
        seen.add(title)
        return True
    cmd = ["gh", "issue", "create", "--repo", REPO, "--title", title,
           "--label", ",".join(labels), "--body-file", "-"]
    if MILESTONE:
        cmd += ["--milestone", MILESTONE]
    subprocess.run(cmd, check=True, input=body, text=True)
    print(f"created: {title}")
    seen.add(title)
    return True


def main() -> int:
    if not REPO:
        print("REPO is required", file=sys.stderr)
        return 2
    if GRANULARITY not in ("control", "requirement"):
        print(f"GRANULARITY must be control|requirement, got {GRANULARITY!r}", file=sys.stderr)
        return 2

    controls = [
        parse_control(p)
        for module_dir in MODULES
        for p in sorted((CONTENT / module_dir).glob("*.md"))
        if p.name != "_index.md"
    ]
    if not controls:
        print("no control pages found under content/docs/module-*", file=sys.stderr)
        return 2
    missing = [c.title for c in controls if not c.evidence]
    if missing:
        print(f"control pages with no evidence checklist: {missing}", file=sys.stderr)
        return 2

    seen = set() if DRY_RUN else existing_titles()
    created = 0

    created += create_issue(
        "Pre-Qualification Gate (AVD V2.7.1)",
        ["pre-qualification", CYCLE_LABEL],
        prequal_body(),
        seen,
    )

    for c in controls:
        module_label = MODULES[c.module_dir][1]
        created += create_issue(
            c.title, [module_label, "audit-evidence", CYCLE_LABEL], control_body(c), seen
        )
        # Module B is re-audited every year against two customers, so it is the
        # section worth exploding into one issue per evidence item.
        if GRANULARITY == "requirement" and c.module_dir == "module-b":
            for num, item, fmt in c.evidence:
                short = re.sub(r"[*_`]", "", item).split(" — ")[0][:80].strip()
                created += create_issue(
                    f"{c.control_id}.{num} {short}",
                    [module_label, "audit-evidence", CYCLE_LABEL],
                    requirement_body(c, num, item, fmt),
                    seen,
                )

    total_items = sum(len(c.evidence) for c in controls)
    print(
        f"\n{len(controls)} controls, {total_items} evidence items parsed; "
        f"{created} issues created ({GRANULARITY} granularity)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
