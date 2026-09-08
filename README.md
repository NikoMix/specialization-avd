# Azure Virtual Desktop — Advanced Specialization

> Engagement toolkit for Microsoft partners pursuing the **Azure Virtual Desktop Advanced Specialization** audit (checklist version **V2.7.1**, valid Jan 1 → Jun 30, 2026).

---

## 🎯 Purpose

This repository gives EUC / Modern Workplace consultants a structured, end-to-end
engagement framework to take a partner organisation from **discovery through audit
pass and into production hypercare** for Azure Virtual Desktop.

It contains:

- **Documentation site** (Hugo + the
  [`NikoMix/ms-hugo-theme`](https://github.com/NikoMix/ms-hugo-theme) template)
  covering every audit control, evidence requirement, and common gap for
  Module A (Azure Essentials) + Module B (AVD workload)
- **Engagement playbook** — offering one-pager, qualification questionnaire,
  discovery workshop kit, WAF assessment, MAP / RDS-to-AVD assessment inputs,
  the Microsoft AVD landing zone reference architecture plus three host pool
  patterns (pooled multi-session, personal, single-session), customer
  deliverable templates (HLD, LLD, runbook, KT, hypercare)
- **Innersource governance** — CONTRIBUTING, CODEOWNERS, issue / PR templates,
  content governance lifecycle
- **GitHub Issues automation** — one issue per audit requirement, generated
  from the control pages themselves, recreated annually
- **Engagement Agent** — purpose-built Copilot agent that knows every AVD
  control and consulting workflow

---

## 🧭 Specialization at a glance

| | |
|---|---|
| Checklist version | **V2.7.1** (active through Jun 30, 2026) — V2.8 PREVIEW lands Jun 1, 2026 |
| Pre-qualification | **Solutions Partner for Infrastructure (Azure)** designation |
| Auditor | **ISSI** (Information Security Systems International, LLC) |
| Audit duration | Module B only: **4h** · Module A + B combined: **8h** |
| Pricing | Module B: **$2,400** · Module A + B: **$3,600** |
| Pass validity | Module A: **2 years** · Module B: **1 year** |
| Customer evidence | **2 unique customers** in last **12 months**; ≥1 Native AVD; second may be Citrix on Azure / Horizon on Azure |
| Target consultant | EUC / Modern Workplace engineer (AZ-140) |

---

## 🚀 Getting Started

This repo is a **GitHub Template**. Click **"Use this template"** (not Fork) to create your own copy.

### 1. Use this template

**Use this template → Create a new repository** and choose your GitHub organisation.

### 2. Enable GitHub Pages

**Settings → Pages → Source → GitHub Actions**

The build takes its `baseURL` from `actions/configure-pages`, so a fresh copy of
the template publishes at the right sub-path with no config edit. Override
`baseURL` in `config/_default/hugo.toml` only if you serve the site from a
custom domain.

Also update `params.page.editUrl` in `config/_default/params.toml` to point at
your own repository, so the "Edit this page" links work.

### 3. Create engagement issues

**Actions → Create Audit Engagement Issues → Run workflow**

This creates labelled issues + a milestone for the current audit cycle, one per
control, with every requirement from that control's evidence checklist as a
checkbox. Choose the `requirement` granularity to additionally get one issue per
individual Module B evidence item, and tick `dry_run` first if you want to see
what it would create.

### 4. Done

- Issues appear as your engagement task board 📋
- The documentation site deploys automatically on push to `main` 🌐
- Use the Engagement Agent for guided assistance 🤖

---

## 🤖 Engagement Agent

This repo ships with a **GitHub Custom Agent** — a purpose-built Copilot agent
that knows every AVD audit control, evidence requirement, and common blocker.

Agent profile: [`.github/agents/engagement-agent.agent.md`](.github/agents/engagement-agent.agent.md)

Ask things like:

> *"We're 4 weeks out from a Native AVD Go-Live for 800 users — what evidence are we missing for B.4.1?"*
> *"What WAF Cost levers should we propose for a Win 11 multi-session pool with 200 knowledge workers?"*
> *"FSLogix profile container size keeps growing — what runbook entry covers cleanup?"*

---

## 📅 Annual Audit Cycle

The `Create Audit Engagement Issues` workflow runs annually (default: March 1st)
so consultants have 3 months to refresh evidence before the next audit.

Module B validity is **1 year**, so plan a full re-collection each cycle.
Module A validity is **2 years** and is shared with other Solutions Partner
Infrastructure (Azure) specializations — evidence is reusable.

---

## 🤝 Innersource

Every consultant who runs an AVD engagement is expected to contribute back:

- Missing controls, evidence formats, or templates → PR against
  `content/docs/module-*` or `content/docs/engagement/`
- Lessons learned → issue using the `lesson-learned` template
- Reference architecture refresh → PR against
  `content/docs/engagement/reference-architectures.md`

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and the
[Content Governance](content/docs/innersource/content-governance.md) page.

---

## 🖥️ Local Development

```bash
git submodule update --init --recursive
hugo server
```

Requires the **extended** edition of [Hugo](https://gohugo.io/), **v0.146.0 or
newer** (CI pins v0.165.0). Nothing else — no Node, no Go, no Dart Sass.

Before opening a PR, run what CI runs:

```bash
hugo --gc --minify
python3 scripts/verify-tables.py
```

### About the theme

The site is rendered by the remote template
[`NikoMix/ms-hugo-theme`](https://github.com/NikoMix/ms-hugo-theme), pinned as a
git submodule at `themes/ms-hugo-theme` and checked out by the deploy workflow
with `submodules: recursive`.

It is deliberately **not** wired up as a Hugo Module. Go's module packer strips
every directory named `vendor`, which drops the theme's
`assets/scss/vendor/_chroma.scss` from the module cache and fails the Sass build
with `File to import not found or unreadable: vendor/chroma`. To bump the theme:

```bash
git -C themes/ms-hugo-theme fetch --depth 1 origin main
git -C themes/ms-hugo-theme checkout FETCH_HEAD
git add themes/ms-hugo-theme && git commit -m "Bump ms-hugo-theme"
```

---

## 📁 Structure

```
├── .github/
│   ├── agents/engagement-agent.agent.md
│   ├── memories/hugo-content.md
│   ├── ISSUE_TEMPLATE/*.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── scripts/create-issues.py     # generates issues from the control pages
│   └── workflows/{deploy.yml, create-issues.yml}
├── config/_default/                 # hugo.toml, markup.toml, params.toml, menus.en.toml
├── scripts/
│   ├── generate_workfiles.py        # builds the docx/pptx/xlsx templates
│   └── verify-tables.py             # CI gate: every Markdown table renders as a table
├── static/templates/                # downloadable customer workfiles
├── themes/ms-hugo-theme/            # submodule → NikoMix/ms-hugo-theme
└── content/
    ├── _index.md                    # home
    └── docs/
        ├── overview.md / requirements.md / audit-process.md
        ├── evidence-tracker.md / faq.md
        ├── module-a/                # A.1.1 – A.3.3 (Azure Essentials, shared)
        ├── module-b/                # B.1.1 – B.4.2 (AVD-specific)
        ├── engagement/              # offering, qualification, discovery, WAF, MAP, ref arch, deliverables, DoD
        └── innersource/             # contributing, content governance, roadmap
```

---

## 📄 License

Content is provided for partner enablement purposes. Refer to your Microsoft
Partner Agreement for usage terms.
