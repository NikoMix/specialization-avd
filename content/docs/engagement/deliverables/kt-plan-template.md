+++
title = 'KT Plan Template'
linkTitle = 'KT Plan Template'
description = 'Knowledge transfer plan template for handing AVD operations to the customer team, structured to satisfy controls A.3.2 and B.4.2.'
weight = 40
toc = true
+++

{{% alert type="tip" title="Download the workfile" %}}
{{< download href="/templates/deliverables/kt-plan-template.docx" >}}KT plan template (DOCX){{< /download >}}
{{% /alert %}}

## When to use this

During the production deployment phase, executed across the final 2–3
weeks. Evidence for both
[A.3.2 Plan for Skilling](/docs/module-a/3-2-plan-for-skilling) and
[B.4.2 Post-deployment Documentation](/docs/module-b/4-2-post-deployment-documentation).

## Plan structure

### 1. Audience and roles

| Customer role | Target capability | Microsoft Learn path |
|---|---|---|
| EUC engineer | Design, deploy, manage AVD end-to-end | AZ-140 |
| Service desk lead | Common end-user issue triage, runbook usage | AVD Learn collection + runbook walkthrough |
| Identity admin | Entra integration, CA, MFA for AVD | AZ-104 + CA scenarios |
| Operations manager | Monitor, alert, autoscale, cost levers | AVD Insights + cost workshop |
| Security reviewer | Defender for Cloud + Policy + CA posture for AVD | A.2.1 walkthrough |

### 2. Session plan

| # | Session | Duration | Audience | Outputs |
|---|---|---|---|---|
| 1 | AVD architecture overview | 90 min | All | Recording + slides |
| 2 | Identity, CA, RBAC for AVD | 90 min | Identity, security | Recording + slides |
| 3 | Network design walkthrough | 60 min | Network team | Recording + diagram |
| 4 | FSLogix profile storage | 90 min | EUC engineer, service desk | Recording + runbook section walkthrough |
| 5 | Image management pipeline | 120 min | EUC engineer | Recording + Azure Image Builder demo |
| 6 | Scaling, monitoring, alerting | 90 min | Operations manager, EUC | Recording + workbook tour |
| 7 | Common end-user incidents | 60 min | Service desk | Recording + decision tree |
| 8 | Runbook walkthrough end-to-end | 120 min | All ops staff | Signed acknowledgement |
| 9 | Shadowing wave 1–2 rollout | (per wave) | EUC engineer | Notes |
| 10 | Hypercare handover + KT sign-off | 60 min | All | Signed handover |

### 3. Hands-on labs

- Build a new gold image end-to-end (in a non-production gallery)
- Reset a test user's FSLogix container
- Trigger and review an alert in AVD Insights
- Add a new app via AppAttach

### 4. Evidence captured

- Meeting invites + Teams attendance reports per session
- Recordings (stored in customer SharePoint / Teams)
- Runbook walkthrough sign-off
- Lab completion sign-off
- Final KT sign-off (customer ops manager + engagement lead)

### 5. KT exit criteria

- All sessions delivered with attendance from named roles
- All labs completed
- Runbook walkthrough acknowledged
- Customer ops manager signs the KT completion form

### 6. KT completion form

| Item | Status | Signature | Date |
|---|---|---|---|
| All sessions delivered | | | |
| Recordings handed over | | | |
| Labs completed | | | |
| Runbook walkthrough acknowledged | | | |
| Customer ops team ready to operate AVD | | | |
