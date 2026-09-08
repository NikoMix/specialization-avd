+++
title = 'Module B – Azure Virtual Desktop'
linkTitle = 'Module B – Azure Virtual Desktop'
description = 'The seven AVD-specific Module B controls (B.1.1 – B.4.2): workload assessment, solution design, Azure Well-Architected review, PoC or pilot, deployment to production, service validation and testing, and post-deployment documentation.'
lede = 'Seven controls covering the Azure Virtual Desktop workload itself, evidenced from two qualifying customer engagements. A Module B pass is valid for one calendar year, so plan a full evidence re-collection every cycle.'
weight = 50
+++

Module B is the workload audit. Every control must be evidenced from real
customer delivery within the last twelve months, across **two unique
customers**, at least one of which must be Native Azure Virtual Desktop. The
auditor walks both engagements end to end, so keep the evidence for each
customer in its own folder and cross-reference it consistently.

| Control | Focus | Page |
|---|---|---|
| B.1.1 | Workload assessment — personas, apps, image strategy | [Open](/docs/module-b/1-1-workload-assessment) |
| B.2.1 | Solution design — the HLD | [Open](/docs/module-b/2-1-solution-design) |
| B.2.2 | Azure Well-Architected review | [Open](/docs/module-b/2-2-azure-well-architected-review) |
| B.2.3 | PoC or pilot | [Open](/docs/module-b/2-3-poc-or-pilot) |
| B.3.1 | Deployment to production | [Open](/docs/module-b/3-1-deployment-to-production) |
| B.4.1 | Service validation and testing | [Open](/docs/module-b/4-1-service-validation-and-testing) |
| B.4.2 | Post-deployment documentation | [Open](/docs/module-b/4-2-post-deployment-documentation) |

{{% alert type="tip" title="Start from the reference architecture" %}}
Designs that follow the published
[Azure Virtual Desktop landing zone reference architecture](/docs/engagement/reference-architectures)
carry most of B.2.1, B.2.2 and B.3.1 by construction — the accelerator ships
the Bicep and Terraform that A.3.1 and B.3.1 both ask you to show.
{{% /alert %}}
