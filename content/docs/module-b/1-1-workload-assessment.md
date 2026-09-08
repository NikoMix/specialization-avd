+++
title = 'B.1.1 – Workload Assessment'
linkTitle = '1.1 Workload Assessment'
description = 'Evidence requirements for control B.1.1 – user persona inventory, app inventory, and image strategy decisions for the AVD migration / greenfield engagement.'
weight = 10
toc = true
modules = ['Module B']
+++

## What the Auditor Checks

The auditor verifies that the engagement began with a **rigorous workload
assessment** — user personas, application inventory, and image strategy
decisions were captured before solution design.

This applies to both **greenfield** AVD and **migration** (RDS → AVD,
Citrix → AVD, Horizon → AVD).

**Typical questions:**
- Where is the user persona inventory?
- Where is the app inventory with compatibility / delivery method?
- How was the gold image strategy decided?
- For migrations: where is the source-system assessment (MAP, Azure Migrate)?

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **User persona inventory** with profile types (knowledge worker / power user / dev / regulated) and density assumptions | Excel, PDF | ⬜ |
| 2 | **Application inventory** with delivery method decision (MSI / MSIX / AppAttach / streamed / M365 Apps) | Excel, PDF | ⬜ |
| 3 | **App compatibility / packaging output** — at least sampled (RDA, Test Base, manual test results) | Excel, PDF | ⬜ |
| 4 | **Image strategy decision** — gold image vs Marketplace, baseline OS, customisation, refresh cadence | PDF, Word | ⬜ |
| 5 | **(Migration) source assessment** — MAP toolkit / Azure Migrate output for RDS / Citrix / Horizon footprint | Excel, PDF | ⬜ |
| 6 | **Sizing & density model** — sessions per host, host SKU, total host count per persona | Excel, PDF | ⬜ |
| 7 | **Customer review & sign-off** of the assessment | PDF, Word, Email | ⬜ |

{{% alert type="tip" %}}
Reuse the [Qualification Questionnaire](/docs/engagement/qualification-questionnaire)
and [Assessment Platform Inputs](/docs/engagement/assessment-platform-inputs)
pages — they are structured to produce evidence for this control directly.
{{% /alert %}}

---

## Evidence Guidance

### User persona template

| Persona | Profile type | Users | Apps in scope | Session host SKU | Sessions per host | Total hosts |
|---|---|---|---|---|---|---|
| Knowledge worker | Pooled multi-session | 800 | M365, Edge, Teams, 4 LOB | D8as v5 | 8 | 100 |
| Power user | Personal | 50 | + Visio, Project, AutoCAD viewer | D16as v5 | 1 | 50 |
| Developer | Personal | 30 | + VS, Docker | D16as v5 + Premium SSD | 1 | 30 |
| Call centre | Pooled multi-session | 200 | M365 + CRM web | D4as v5 | 12 | 17 |

### App delivery decision matrix

| App | Vendor MSIX? | Per-user vs shared | Decision |
|---|---|---|---|
| M365 Apps | n/a | Shared | Per-host install with shared-computer activation |
| Adobe Reader | Yes | Shared | AppAttach |
| Custom LOB | No | Per-user | Intune deployment |
| Vendor tool with COM dependency | No | Shared | Per-host install in gold image |

### Image strategy

Document the decision:

- **Source OS:** Win 11 Enterprise multi-session 23H2 (or current)
- **Base image:** Azure Marketplace + customisations OR custom gold image
- **Pipeline:** Azure Image Builder + monthly refresh
- **Customisations:** M365 Apps, Teams optimisation, FSLogix client, AVD agent, base LOB apps
- **Validation:** automated test suite + sign-off before promotion

---

## Evidence Status

| Evidence Item | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| User persona inventory | | | ⬜ | |
| Application inventory | | | ⬜ | |
| App compatibility output | | | ⬜ | |
| Image strategy decision | | | ⬜ | |
| Source assessment (migration) | | | ⬜ | |
| Sizing & density model | | | ⬜ | |
| Customer sign-off | | | ⬜ | |

---

## Common Gaps

| Gap | Remediation |
|---|---|
| Personas captured but no density / sizing | Add sessions-per-host and host SKU columns |
| App inventory exists but no delivery decision per app | Add a decision column to every row |
| Greenfield assessment skipped because "no source system" | Capture user / app / image discovery from scratch — assessment is still required |
| Migration assessment was Excel-only, no MAP / Azure Migrate output | Run MAP or Azure Migrate even retrospectively to corroborate the manual inventory |
