# Azure Virtual Desktop — Advanced Specialization

> Engagement toolkit for Microsoft partners pursuing the **Azure Virtual Desktop Advanced Specialization** audit (checklist version **V2.7.1**, valid Jan 1 → Jun 30, 2026).

---

## 🎯 Purpose

This repository gives EUC / Modern Workplace consultants a structured, end-to-end
engagement framework to take a partner organisation from **discovery through audit
pass and into production hypercare** for Azure Virtual Desktop.

It contains:

- **Documentation site** (Astro 6 + Starlight 0.39) covering every audit control,
  evidence requirement, and common gap for Module A (Azure Essentials) + Module B
  (AVD workload)
- **Engagement playbook** — offering one-pager, qualification questionnaire,
  discovery workshop kit, WAF assessment, MAP / RDS-to-AVD assessment inputs,
  three reference architectures (single-session, multi-session, personal host
  pool), customer deliverable templates (HLD, LLD, runbook, KT, hypercare)
- **Innersource governance** — CONTRIBUTING, CODEOWNERS, issue / PR templates,
  content governance lifecycle
- **GitHub Issues automation** — one issue per audit control, recreated annually
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

### 2. Set your site URL

`astro.config.mjs` derives `site` and `base` from `GITHUB_REPOSITORY` automatically.
Override only if you need a custom URL by setting repository variables:

- `ASTRO_SITE` = `https://YOUR_ORG.github.io/YOUR_REPO_NAME`
- `ASTRO_GITHUB_URL` = `https://github.com/YOUR_ORG/YOUR_REPO_NAME` (optional)

### 3. Enable GitHub Pages

**Settings → Pages → Source → GitHub Actions**

### 4. Create engagement issues

**Actions → Create Audit Engagement Issues → Run workflow**

This creates labelled issues + a milestone for the current audit cycle.

### 5. Done

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
  `src/content/docs/module-*` or `src/content/docs/engagement/`
- Lessons learned → issue using the `lesson-learned` template
- Reference architecture refresh → PR against
  `src/content/docs/engagement/reference-architectures.mdx`

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and the
[Content Governance](src/content/docs/innersource/content-governance.mdx) page.

---

## 🖥️ Local Development

```bash
npm install
npm run dev
```

Requires **Node 24** (matches CI).

---

## 📁 Structure

```
├── .github/
│   ├── agents/engagement-agent.agent.md
│   ├── memories/mdx-content.md
│   ├── ISSUE_TEMPLATE/*.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   ├── scripts/create-issues.sh
│   └── workflows/{deploy.yml, create-issues.yml}
└── src/content/docs/
    ├── index.mdx / overview.mdx / requirements.mdx / audit-process.mdx
    ├── evidence-tracker.mdx / faq.mdx
    ├── module-a/         # A.1.1 – A.3.3 (Azure Essentials, shared)
    ├── module-b/         # B.1.1 – B.4.2 (AVD-specific)
    ├── engagement/       # offering, qualification, discovery, WAF, MAP, ref arch, deliverables, DoD
    └── innersource/      # contributing, content governance, roadmap
```

---

## 📄 License

Content is provided for partner enablement purposes. Refer to your Microsoft
Partner Agreement for usage terms.
