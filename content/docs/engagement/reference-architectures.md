+++
title = 'Reference Architectures'
linkTitle = 'Reference Architectures'
description = 'The Microsoft Azure Virtual Desktop landing zone reference architecture from the Azure Architecture Center, plus three reusable implementation patterns — pooled multi-session, personal host pool, and single-session pooled.'
weight = 60
toc = true
+++

## When to use this

Use during [Discovery](/docs/engagement/discovery-workshop) to pick the right pattern
per persona, and again during [HLD](/docs/engagement/deliverables/hld-template) authoring
as the structural backbone of the design.

## Start from the Microsoft reference architecture

The Azure Architecture Center publishes a first-party reference architecture that
covers every technology the V2.7.1 checklist asks about, so anchor the HLD to it
rather than inventing a structure. Auditors recognise it, and the accelerator
that implements it ships the Bicep and Terraform that
[A.3.1](/docs/module-a/3-1-repeatable-deployment) and
[B.3.1](/docs/module-b/3-1-deployment-to-production) both ask you to demonstrate.

| Article | Type | Use it for |
|---|---|---|
| [Azure Virtual Desktop landing zone design guide](https://learn.microsoft.com/azure/architecture/landing-zones/azure-virtual-desktop/design-guide) | Reference architecture | The primary anchor for [B.2.1](/docs/module-b/2-1-solution-design). Subscription layout, identity, networking, security, management, BCDR, platform automation |
| [Enterprise-scale landing zone for AVD](https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/azure-virtual-desktop/enterprise-scale-landing-zone) | Design areas | The nine design areas the design guide indexes; one section per area in the HLD |
| [AVD landing zone accelerator (`Azure/avdaccelerator`)](https://github.com/Azure/avdaccelerator) | Reference implementation | Bicep / Terraform / portal UI baseline and custom image build for [A.3.1](/docs/module-a/3-1-repeatable-deployment) and [B.3.1](/docs/module-b/3-1-deployment-to-production) |
| [Azure Well-Architected Framework — AVD workload](https://learn.microsoft.com/azure/well-architected/azure-virtual-desktop/overview) | WAF service guide | The workload lens for [A.2.2](/docs/module-a/2-2-well-architected-workloads) and [B.2.2](/docs/module-b/2-2-azure-well-architected-review) |
| [Multiregion BCDR for Azure Virtual Desktop](https://learn.microsoft.com/azure/architecture/example-scenario/azure-virtual-desktop/azure-virtual-desktop-multi-region-bcdr) | Example scenario | The BCDR section of the HLD — paired-region host pools, profile replication, RTO / RPO |
| [Azure Virtual Desktop for Azure Local](https://learn.microsoft.com/azure/architecture/hybrid/azure-local-workload-virtual-desktop) | Example scenario | Customers with a data-residency or latency reason to keep session hosts on-premises |
| [Esri ArcGIS Pro in Azure Virtual Desktop](https://learn.microsoft.com/azure/architecture/example-scenario/data/esri-arcgis-azure-virtual-desktop) | Example scenario | GPU personas — sizing and driver guidance for a personal or single-session pool |
| [Enterprise-scale support for Citrix on Azure](https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/azure-virtual-desktop/landing-zone-citrix/citrix-enterprise-scale-landing-zone) | Design guidelines | The second qualifying customer when they run Citrix on Azure rather than Native AVD |
| [Azure VMware Solution landing zone](https://learn.microsoft.com/azure/cloud-adoption-framework/azure-vmware-solution/architecture-landing-zone) · [Horizon on AVS](https://learn.microsoft.com/azure/azure-vmware/azure-vmware-solution-horizon) | Design guidelines | The second qualifying customer when they run Horizon on Azure |

### How the design areas map to the audit

The design guide labels its architecture diagram A–I. Each label is a design
area, and each design area lands in a specific control's evidence pack.

| Design area | Landing zone label | Evidences |
|---|---|---|
| Azure billing and tenant | A | [A.1.2](/docs/module-a/1-2-cloud-ai-adoption-plan) |
| Identity and access management | B | [B.2.1](/docs/module-b/2-1-solution-design) identity design, [A.2.1](/docs/module-a/2-1-security-governance-tooling) Conditional Access |
| Resource organization | C | [A.2.1](/docs/module-a/2-1-security-governance-tooling), [A.3.1](/docs/module-a/3-1-repeatable-deployment) |
| Management and monitoring | D, G, H | [A.3.3](/docs/module-a/3-3-operations-management-tooling), [B.4.2](/docs/module-b/4-2-post-deployment-documentation) |
| Network topology and connectivity | E | [B.2.1](/docs/module-b/2-1-solution-design) networking section |
| Security | F | [A.2.1](/docs/module-a/2-1-security-governance-tooling) |
| Business continuity and disaster recovery | F, G | [B.2.1](/docs/module-b/2-1-solution-design) BCDR section, [B.4.1](/docs/module-b/4-1-service-validation-and-testing) failover test |
| Platform automation and DevOps | I | [A.3.1](/docs/module-a/3-1-repeatable-deployment), [B.3.1](/docs/module-b/3-1-deployment-to-production) |

{{% alert type="tip" title="Cite the architecture in the HLD" %}}
Auditors ask *"why this design?"* far more often than *"what is this design?"*.
A one-line citation of the landing zone design guide next to each decision, plus
a note where you deliberately deviated and why, answers both at once.
{{% /alert %}}

## The three implementation patterns

The patterns below sit **inside** the landing zone above — they decide the host
pool shape per persona, not the platform around it.

| Pattern | Best for | Density | Cost per user | Persistence |
|---|---|---|---|---|
| **Pooled multi-session** | Knowledge workers, call centre, shift workers | Highest (4–16 sessions / host) | Lowest | Stateless (profile via FSLogix) |
| **Personal host pool** | Developers, power users, GPU, regulated isolation | 1 session / host (assigned) | Highest | Persistent at host level |
| **Single-session pooled** | Per-session isolation without permanent assignment | 1 session / host (rotating) | Mid | Stateless (profile via FSLogix) |

{{< tabs >}}
{{% tab title="Pooled multi-session" %}}
### Pooled multi-session — default for knowledge workers

**Topology**

- Host pool: pooled, load-balancing breadth-first
- OS: Windows 11 Enterprise multi-session 23H2 (or current)
- Session host SKU: D8as v5 (typical knowledge worker, 8 sessions / host)
- Max session limit per host: per persona density test (B.4.1)
- Scaling plan: working-hours schedule + ramp-up safety margin

**Identity**

- Entra-joined + Intune
- MFA via Conditional Access policy targeting AVD client app
- AVD admin model: PIM eligible, JIT activation

**Profile storage**

- FSLogix on Azure Files Premium share, Kerberos auth
- Profile container + Office container split
- Per-user budget: 30 GB starting

**Networking**

- RDP Shortpath for managed networks enabled
- VNet peered to hub for shared services + on-prem reachability
- Private endpoints for storage (FSLogix share, Key Vault)
- Egress firewall: AVD service URLs allow-listed

**Image management**

- Custom gold image built by Azure Image Builder
- Monthly refresh; validation pool first, production second
- Pre-staged: M365 Apps (shared-computer activation), Teams (AVD-optimised),
  FSLogix agent, AVD agent, base LOB apps

**App delivery**

- M365 Apps: per-host install with shared-computer activation
- Shared apps: AppAttach (MSIX) where possible
- Per-user apps: Intune
- Legacy COM-bound apps: per-host install in gold image

**BCDR**

- Paired-region host pool (cold standby) + FSLogix replication
- RPO: ≤ container replication interval (e.g. 1h)
- RTO: ≤ 4h (cold pool warm-up)
{{% /tab %}}

{{% tab title="Personal host pool" %}}
### Personal host pool — developers, power users, GPU

**Topology**

- Host pool: personal, assignment direct or automatic-on-first-login
- OS: Windows 11 Enterprise 23H2
- Session host SKU: D16as v5 (or NCas T4 for GPU)
- 1 user assigned per host
- Scaling plan: time-based deallocate when offline (cost lever)

**Identity**

- Entra-joined + Intune
- Hybrid join if LOB tools need on-prem AD

**Profile storage**

- Locally on the personal VM (persistent disk)
- FSLogix optional for OneDrive Known Folder Move container only

**Networking**

- Same hub-spoke pattern as pooled
- RDP Shortpath enabled
- Outbound internet via Azure Firewall / customer proxy

**Image management**

- Gold image (lighter customisation than pooled — users install their own
  tools)
- Quarterly refresh; user reinstall pattern documented in runbook

**App delivery**

- Local install rights for developers / power users (with caveats)
- Intune baseline for managed apps
- M365 Apps user-bound activation

**BCDR**

- Personal host pool is the highest-risk pattern for BCDR (state is on the
  VM). Document: backup strategy (Azure Backup), user-data on OneDrive
  / network share, host re-provisioning runbook
{{% /tab %}}

{{% tab title="Single-session pooled" %}}
### Single-session pooled — per-session isolation

**Topology**

- Host pool: pooled, max session limit = 1
- OS: Windows 11 Enterprise 23H2 (single-session)
- Session host SKU: D4as v5 (typical)
- Scaling plan: working-hours schedule
- Use case: regulated isolation, GPU workload that can't share, audit
  boundary per session

**Identity**

- Entra-joined + Intune
- CA policy strict (compliant device, named locations)

**Profile storage**

- FSLogix on Azure Files Premium share (Kerberos)
- Per-user budget tuned to workload

**Networking**

- Same hub-spoke pattern
- Often paired with dedicated egress for regulated traffic flows

**Image management**

- Gold image, monthly refresh
- Validation pool first

**App delivery**

- Per-host install in gold image (locked-down)
- AppAttach for any shared apps

**BCDR**

- Same as pooled multi-session: paired-region host pool + FSLogix
  replication
{{% /tab %}}
{{< /tabs >}}

## Decision shortcut

| Question | If yes → |
|---|---|
| Persona installs / customises their own tools? | Personal |
| Persona needs GPU dedicated? | Personal |
| Persona needs audit boundary per session? | Single-session pooled |
| Persona is knowledge worker / call centre / shift? | Pooled multi-session |
| In doubt? | Pooled multi-session is the default |

## Reuse & contribute back

{{% alert type="tip" %}}
Hit a persona shape the three patterns don't cleanly fit? PR a new tab
with the variant pattern (e.g. "pooled multi-session + per-user persistent
data disk"). Include the decision shortcut that should route to it.
{{% /alert %}}
