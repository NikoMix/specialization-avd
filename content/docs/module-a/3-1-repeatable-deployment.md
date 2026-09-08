+++
title = 'A.3.1 – Repeatable Deployment'
linkTitle = '3.1 Repeatable Deployment'
description = 'Evidence requirements for control A.3.1 – Infrastructure as Code (Bicep / Terraform / ARM) used to deploy the AVD landing zone and host pool.'
weight = 50
toc = true
modules = ['Module A']
+++

## What the Auditor Checks

The auditor verifies that the AVD environment was deployed via
**Infrastructure as Code** (Bicep, Terraform, or ARM) through a repeatable
pipeline — not click-ops in the portal.

**Typical questions:**
- Where is the IaC repository?
- Show me a successful pipeline run that deployed AVD.
- How are changes promoted across environments?

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **IaC repository structure** (Bicep / Terraform / ARM) covering landing zone + host pool | Screenshot, PDF | ⬜ |
| 2 | **Pipeline run** showing a successful AVD deployment | Screenshot, PDF, GitHub Actions / Azure DevOps export | ⬜ |
| 3 | **Promotion pattern** (dev → test → prod, ring-based, etc.) | PDF, Word, Diagram | ⬜ |
| 4 | **Module reuse** — at minimum host pool, session host, FSLogix storage as reusable modules | Screenshot, PDF | ⬜ |
| 5 | **Parameter file pattern** showing environment-specific values (no hardcoding) | Screenshot, PDF | ⬜ |
| 6 | **Drift detection** approach (Bicep what-if / Terraform plan in CI, or Azure Policy alerts) | Screenshot, PDF | ⬜ |

{{% alert type="tip" %}}
The **published Azure Virtual Desktop landing zone Bicep modules**
(aka.ms/avdaccelerator and the ALZ AVD pattern) are recognised as
best-practice baselines. Reference them in your IaC repo README and
capture a screenshot of the module use.
{{% /alert %}}

---

## Evidence Guidance

### Repository structure (Bicep example)

```
iac/
├── modules/
│   ├── avd-host-pool/
│   ├── avd-session-host/
│   ├── avd-app-group/
│   ├── avd-workspace/
│   ├── fslogix-storage/
│   ├── networking/
│   └── monitoring/
├── envs/
│   ├── dev.bicepparam
│   ├── test.bicepparam
│   └── prod.bicepparam
└── main.bicep
```

### Pipeline run

Capture from GitHub Actions or Azure DevOps:

- Run summary showing **plan / what-if** + **apply / deploy** stages
- Artefact of the apply log
- Approval gates between environments

### Anonymisation

Customer-specific values (subscription IDs, tenant IDs, names) should be
redacted in screenshots. Keep the **structure** visible.

---

## Evidence Status

| Evidence Item | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| IaC repository structure | | | ⬜ | |
| Pipeline run | | | ⬜ | |
| Promotion pattern | | | ⬜ | |
| Module reuse | | | ⬜ | |
| Parameter file pattern | | | ⬜ | |
| Drift detection | | | ⬜ | |

---

## Common Gaps

| Gap | Remediation |
|---|---|
| Initial deployment was click-ops, IaC adopted later | Show the IaC was used for at least one subsequent material change |
| Single environment, no promotion pattern | Add at least dev → prod with approval gates |
| Hardcoded subscription IDs in templates | Move to parameter files; show the diff |
| No drift detection in CI | Add what-if / plan stage that fails on drift outside change windows |
