# Hugo content authoring rules

**Scope:** `content/**/*.md`

The site is built with **Hugo (extended)** and the
[`NikoMix/ms-hugo-theme`](https://github.com/NikoMix/ms-hugo-theme) template,
pinned as a git submodule at `themes/ms-hugo-theme`. Control pages follow a
**strict template** so the Engagement Agent and the auto-generated GitHub
Issues stay synchronised.

## ⚠️ Tables are load-bearing

Every control page is a set of evidence tables, and they are the single most
common thing to break. Two rules:

1. **A Markdown table row must start at column 0.** Four or more leading spaces
   turns the whole table into a code block; even a 1–3 space indent inside a
   list item is fragile. Never nest a table inside a numbered list — use a
   heading instead.
2. **Inside a shortcode, use the `{{%` form, not `{{<`.** `{{% ... %}}` renders
   its body as Markdown, so tables work. `{{< ... >}}` passes the body through
   as raw HTML and the table stays literal pipes.

`scripts/verify-tables.py` enforces both: it counts Markdown tables per page,
compares that with the number of `<table>` elements Hugo emitted, and fails the
build on any mismatch. It runs on every push and pull request.

## Theme shortcodes

The template offers `alert`, `cards`, `card`, `tabs`, `tab`, `accordion`,
`badge`, `button`, `columns`, `icon`, `figure` and `video`.

```md
{{%/* alert type="tip" title="Optional heading" */%}}
Markdown **body**. `type` is note | tip | important | warning | caution.
{{%/* /alert */%}}

{{</* tabs */>}}
{{%/* tab title="Pooled multi-session" */%}}
Markdown body, tables allowed.
{{%/* /tab */%}}
{{</* /tabs */>}}
```

Links to files under `static/` must go through the project's `download`
shortcode, never a plain Markdown link:

```md
{{</* download href="/templates/engagement/waf-assessment.xlsx" */>}}WAF workbook (XLSX){{</* /download */>}}
```

It runs the href through `relURL`, so the link survives the
`/specialization-avd/` sub-path that GitHub Pages serves the site from. A plain
root-relative Markdown link does not, and `scripts/verify-links.py` fails the
build when one appears.

Do **not** use the theme's `button` shortcode for this: it emits a multi-line
`<a>` tag containing a blank line, which terminates the surrounding Markdown
paragraph and mangles the anchor.

## Control page template (Module A / Module B)

Every file in `content/docs/module-a/` and `content/docs/module-b/` must follow
this exact structure:

```md
+++
title = '<MODULE>.<SECTION>.<ITEM> – <Short Title>'
linkTitle = '<SECTION>.<ITEM> <Short Title>'
description = '<One-sentence summary used by the theme and search engines>'
weight = <integer, 10 per position>
toc = true
modules = ['Module A']
+++

## What the Auditor Checks

<Short prose paragraph>

**Typical questions:**
- <Q1>

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **<Item name>** | PDF, Word, Excel | ⬜ |

---

## Evidence Guidance

### <Item 1 name>

---

## Evidence Status

| Item | Owner | Status | Last Updated | Notes |
|---|---|---|---|---|

---

## Common Gaps

| Gap | Remediation |
|---|---|
```

## Status icons (mandatory)

| Icon | Meaning |
|---|---|
| `⬜` | Not started |
| `🟡` | In progress |
| `✅` | Complete |

## Cross-references

- Control numbers in prose always use dots: `A.2.1`, `B.3.1`. Never `A2.1`.
- Cross-link pages with **absolute logical paths without a trailing slash**:
  `/docs/module-a/2-1-security-governance-tooling`. The theme's link render
  hook resolves these through `.Page.GetPage` and rewrites them to a
  `RelPermalink` that includes the Pages sub-path. Relative `../` links resolve
  against the page's *directory*, not its URL, and silently break.
- **Filenames must not contain dots.** Use `2-1-foo.md`, not `2.1-foo.md`.
- Never link to GitHub Issues by hard-coded number — they vary per fork.

## The leading-slash trap

Hugo's `relURL` returns a **leading-slash path unchanged**, so it does *not*
prepend the site sub-path. Anywhere a theme template pipes a configured value
through `relURL` — `params.banner.linkUrl`, the home page's `[[actions]]` URLs,
the `card` shortcode's `href` — write the path **without** a leading slash:

| ❌ `/docs/overview/` | ✅ `docs/overview/` |
|---|---|

Markdown links are the opposite: those go through the theme's link render hook,
which resolves them with `.Page.GetPage`, so they **must** be absolute
(`/docs/module-b/2-1-solution-design`). `scripts/verify-links.py` catches both
mistakes.

## When evidence requirements change

Edit the control page and stop there. The `Create Audit Engagement Issues`
workflow parses the `## Required Evidence Checklist` table at run time via
`.github/scripts/create-issues.py`, so the issue checkboxes follow the doc
automatically. The workflow fails if a control page has no such table.

## Headings

`## ` and `### ` only in body content; the page title comes from front matter
and is rendered as the `<h1>`. The table of contents is built from `h2`–`h3`.
