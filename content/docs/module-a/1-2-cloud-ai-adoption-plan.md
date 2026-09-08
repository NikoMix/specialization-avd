+++
title = 'A.1.2 – Cloud & AI Adoption Plan'
linkTitle = '1.2 Cloud & AI Adoption Plan'
description = 'Evidence requirements for control A.1.2 – the wave plan / roadmap sequencing AVD adoption with dependencies.'
weight = 20
toc = true
modules = ['Module A']
+++

## What the Auditor Checks

The auditor verifies that the engagement followed a **documented adoption
plan** that sequenced AVD work realistically against dependencies (identity,
network, profile storage, image, app delivery, training, support model).

**Typical questions:**
- Where is the wave / roadmap plan?
- Were AVD dependencies (identity, network, FSLogix, image) sequenced before
  end-user rollout?
- Was the plan tracked and updated through delivery?

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **AVD wave plan / roadmap** with phases and timelines | PDF, Excel, MS Project, Visio | ⬜ |
| 2 | **Dependency mapping** — identity, network, profile storage, image, apps, support | PDF, Excel | ⬜ |
| 3 | **Wave-by-wave user breakdown** — which personas roll out when | Excel, PDF | ⬜ |
| 4 | **Risk register** entries relevant to AVD adoption | Excel, PDF | ⬜ |
| 5 | **Plan version history** showing the plan was actively maintained | Excel, PDF, ADO / Jira export | ⬜ |

{{% alert type="tip" %}}
The Microsoft **CAF Plan phase** workbook + a simple Excel wave plan
satisfy this control cleanly. Anonymise the customer and export both as PDF.
{{% /alert %}}

---

## Evidence Guidance

### Wave plan structure

| Wave | Scope | Users | Start | End | Dependencies | Owner |
|---|---|---|---|---|---|---|
| 0 | Landing zone build | — | | | Subscriptions, Entra, network | |
| 1 | Pilot — 1 persona | 25 | | | FSLogix storage, gold image v1 | |
| 2 | First production wave | 200 | | | App attach packages, support training | |
| 3 | Wider rollout | 800 | | | Wave 2 success criteria met | |

### Dependency mapping

Show that the following were sequenced **before** end-user rollout:

- Entra ID / hybrid join model
- Network design (RDP Shortpath, peering, DNS, private endpoints)
- FSLogix profile storage (Azure Files / ANF, share permissions, GPOs)
- Image management pipeline (Azure Image Builder, monthly refresh)
- App delivery strategy (Intune, AppAttach, M365 Apps)
- Support model + skilling

---

## Evidence Status

| Evidence Item | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| Wave plan / roadmap | | | ⬜ | |
| Dependency mapping | | | ⬜ | |
| User breakdown | | | ⬜ | |
| Risk register entries | | | ⬜ | |
| Plan version history | | | ⬜ | |

---

## Common Gaps

| Gap | Remediation |
|---|---|
| Plan exists but no dependency mapping | Add a dependency column / matrix to each wave |
| Plan was made once and never updated | Use ADO / Jira board exports to show ongoing maintenance |
| End-user rollout started before identity / profile storage was ready | Re-sequence and document the corrective action |
| Personas not mapped to waves | Add a persona-to-wave matrix |
