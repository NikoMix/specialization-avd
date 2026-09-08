+++
title = 'B.4.2 – Post-deployment Documentation'
linkTitle = '4.2 Post-deployment Documentation'
description = 'Evidence requirements for control B.4.2 – LLD, runbook, knowledge transfer, hypercare plan, and customer sign-off.'
weight = 70
toc = true
modules = ['Module B']
+++

## What the Auditor Checks

The auditor verifies that the customer was **handed over to operate** with a
complete documentation pack — and that they signed off accepting it.

**Typical questions:**
- Show me the LLD.
- Walk me through the runbook.
- Show the KT plan and attendance.
- What is the hypercare arrangement and what is the exit criteria?
- Where is the customer sign-off?

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **Low-Level Design (LLD)** — the as-built, with named resources and values | PDF, Word | ⬜ |
| 2 | **Runbook** — operational procedures (image refresh, scaling, FSLogix, user onboarding, common incidents) | PDF, Word | ⬜ |
| 3 | **Knowledge Transfer (KT) plan** + attendance + recordings | PDF, Word, Teams record | ⬜ |
| 4 | **Hypercare plan** — duration, channels, escalation, exit criteria | PDF, Word | ⬜ |
| 5 | **Handover acceptance / customer sign-off** | PDF, Word, Email | ⬜ |
| 6 | **Lessons learned** captured for innersource | PDF, Word, repo PR | ⬜ |

{{% alert type="tip" %}}
Use the deliverable templates in
[`engagement/deliverables/`](/docs/engagement/deliverables/runbook-template)
— they are pre-structured to satisfy this control.
{{% /alert %}}

---

## Evidence Guidance

### LLD must include

- Subscription / management group / resource group structure
- Named resources (host pools, session host pool names, image gallery,
  FSLogix storage account & share, scaling plan, log analytics workspace)
- Networking: VNets, subnets, NSGs, RDP Shortpath config, private endpoints,
  DNS zones, firewall rules
- Identity: Entra groups, RBAC role assignments, CA policies, PIM eligible
  assignments
- Image: source, customisation steps, refresh pipeline, current version
- Monitoring: diagnostic settings, workbooks, alerts, action groups

### Runbook must include

- **Image refresh** — how to build, test, promote a new gold image
- **Scaling** — how to adjust min/max, schedule changes, troubleshoot
  unexpected scaling
- **FSLogix** — profile reset, container repair, share permission audit,
  growth review
- **User onboarding / offboarding** — add to AVD Entra group, profile
  pre-stage, leaver process
- **Common incidents** — connection failure, slow logon, app launch failure,
  print/peripheral issues
- **Patching** — ring-based update flow, validation host pool process
- **BCDR** — region failover procedure (and how to fail back)
- **Backup / restore** — what is backed up, RTO / RPO

### Hypercare plan

- Duration (e.g. 2–4 weeks post Go-Live)
- Communication channels (Teams channel, email DL, on-call rota)
- Escalation matrix (severity → response time → owner)
- Daily / weekly stand-up cadence
- **Exit criteria** — what must be true to leave hypercare (incident rate
  below X, customer ops team confidence, all P1 / P2 issues closed)

---

## Evidence Status

| Evidence Item | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| LLD | | | ⬜ | |
| Runbook | | | ⬜ | |
| KT plan + attendance | | | ⬜ | |
| Hypercare plan | | | ⬜ | |
| Handover sign-off | | | ⬜ | |
| Lessons learned | | | ⬜ | |

---

## Common Gaps

| Gap | Remediation |
|---|---|
| LLD is just a copy of the HLD with no resource names / values | Capture the as-built from the portal / IaC outputs |
| Runbook missing FSLogix profile reset / repair | Add the procedure; it is the most common AVD incident type |
| KT delivered but no attendance record | Pull Teams meeting attendance reports |
| Hypercare ended on time but no exit criteria documented | Add exit criteria for future engagements; capture retrospective sign-off |
| No lessons learned filed | Open a lesson-learned issue in this repo |
