+++
title = 'LLD Template'
linkTitle = 'LLD Template'
description = 'Low-Level Design (as-built) template for an Azure Virtual Desktop deployment, structured to satisfy audit control B.4.2.'
weight = 20
toc = true
+++

{{% alert type="tip" title="Download the workfile" %}}
{{< download href="/templates/deliverables/lld-template.docx" >}}LLD template (DOCX){{< /download >}}
{{% /alert %}}

## When to use this

After production deployment, captured as the **as-built** state at Go-Live.
Primary evidence artefact for
[B.4.2 Post-deployment Documentation](/docs/module-b/4-2-post-deployment-documentation).

The LLD differs from the HLD: HLD is **why and what**; LLD is **what is
running, with names and values**.

## Document structure

```
1. Scope & version (Go-Live date, image version, IaC commit SHA)
2. Subscription & management group structure
3. Resource group layout
4. Networking (VNets, subnets, NSGs, firewall rules, DNS, private endpoints)
5. Host pools (per pool: name, type, max session limit, load balancing,
   session host SKU, count, image)
6. Session hosts (current host names, deployment date, image version,
   tags)
7. FSLogix profile storage (storage account, share, permissions, container
   config)
8. Image gallery (gallery name, image definitions, current version)
9. Identity (Entra groups, RBAC role assignments, PIM eligible assignments,
   Conditional Access policy IDs and conditions)
10. Monitoring (Log Analytics workspace, diagnostic settings, AVD Insights
    workbook, alert rules and action groups)
11. Scaling plans (name, schedule, ramp-up/down configuration)
12. App delivery (AppAttach packages, Intune app assignments, M365 Apps
    config)
13. BCDR resources (paired-region resources, replication mechanism, runbooks)
14. IaC repository reference (repo URL, commit SHA, parameter files)
15. Change history since Go-Live
```

## Tips

- Pull resource names and values from `az resource list` / Bicep what-if
  output / Terraform state — do not hand-curate.
- Anonymise customer-specific names if the LLD will be reused as a
  template, but **the LLD shared with the auditor and the customer must use
  real names**.
- The LLD is a living document — version it alongside the IaC.
