+++
title = 'A.3.2 – Plan for Skilling'
linkTitle = '3.2 Plan for Skilling'
description = 'Evidence requirements for control A.3.2 – skilling plan for the customer operations team on AVD.'
weight = 60
toc = true
modules = ['Module A']
+++

## What the Auditor Checks

The auditor verifies that the engagement included a **skilling plan for the
customer's operations team** so they can run AVD after handover — not just
that your own team is trained.

**Typical questions:**
- Where is the skilling plan?
- Which roles on the customer side were targeted?
- What training was actually delivered (vs. just planned)?

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **Skilling plan document** naming customer roles and target capabilities | PDF, Word | ⬜ |
| 2 | **AZ-140 study path** referenced (and AZ-104 prerequisite if applicable) | PDF, Word, Learn link | ⬜ |
| 3 | **Knowledge Transfer (KT) sessions** schedule and attendance | PDF, Word, Email, Teams record | ⬜ |
| 4 | **Hands-on lab / shadowing** plan for the customer ops team | PDF, Word | ⬜ |
| 5 | **Runbook walkthrough** session evidence | PDF, Word, Teams record | ⬜ |
| 6 | **Customer sign-off** that skilling was completed and they feel ready to operate | PDF, Word, Email | ⬜ |

{{% alert type="tip" %}}
Reuse the [KT Plan template](/docs/engagement/deliverables/kt-plan-template)
as the skilling plan; it is structured to satisfy this control directly.
{{% /alert %}}

---

## Evidence Guidance

### Skilling plan structure

| Role (customer side) | Target capability | Microsoft Learn path | KT session | Hands-on | Sign-off |
|---|---|---|---|---|---|
| EUC engineer | Design, deploy, manage AVD | AZ-140 | Sessions 1–6 | Shadowing wave 1–2 | |
| Service desk lead | Common end-user issue triage | AVD support fundamentals | Session 7 | Lab exercises | |
| Identity admin | Entra integration, CA, MFA for AVD | AZ-104 + CA lab | Session 8 | Policy walkthrough | |
| Operations manager | Monitor, alert, autoscale, cost | AVD Insights + cost workshop | Session 9 | Workbook tour | |

### Microsoft Learn references

- [AZ-140 study path](https://learn.microsoft.com/credentials/certifications/azure-virtual-desktop-specialty/)
- [AVD Learn collection](https://learn.microsoft.com/azure/virtual-desktop/)

---

## Evidence Status

| Evidence Item | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| Skilling plan document | | | ⬜ | |
| AZ-140 study path referenced | | | ⬜ | |
| KT session schedule + attendance | | | ⬜ | |
| Hands-on lab / shadowing plan | | | ⬜ | |
| Runbook walkthrough | | | ⬜ | |
| Customer sign-off | | | ⬜ | |

---

## Common Gaps

| Gap | Remediation |
|---|---|
| Skilling plan exists but no KT session attendance | Capture meeting invites + attendance reports + Teams recordings |
| Customer ops team not named in plan | Add role assignments with named individuals |
| Plan is generic AVD training, not tied to the customer's runbook | Map each Learn module to runbook section relevance |
| No post-skilling sign-off | Add a 1-page acceptance form signed by the customer ops manager |
