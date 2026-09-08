+++
title = 'A.2.1 – Security & Governance Tooling'
linkTitle = '2.1 Security & Governance Tooling'
description = 'Evidence requirements for control A.2.1 – Defender for Cloud, Azure Policy, and Entra Conditional Access applied to the AVD subscription.'
weight = 30
toc = true
modules = ['Module A']
+++

## What the Auditor Checks

The auditor verifies that the **AVD landing zone has security and governance
tooling deployed and operating** — not just policy intent.

**Typical questions:**
- Is Defender for Cloud enabled on the AVD subscription?
- Are Azure Policy initiatives assigned (e.g. ALZ Default, NIST 800-53, CIS)?
- Are Entra Conditional Access policies in force for AVD client sign-in?

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **Microsoft Defender for Cloud** enabled on AVD subscription (Foundational CSPM at minimum, Defender for Servers Plan 2 recommended) | Screenshot, PDF | ⬜ |
| 2 | **Defender for Cloud secure score** for the AVD subscription | Screenshot, PDF | ⬜ |
| 3 | **Azure Policy initiative assignments** covering the AVD scope | Screenshot, PDF, Policy export | ⬜ |
| 4 | **Entra Conditional Access policies** scoped to AVD app sign-in (e.g. require compliant device, MFA, country / network filters) | Screenshot, PDF | ⬜ |
| 5 | **Privileged access model** for AVD admins (PIM, just-in-time elevation) | Screenshot, PDF | ⬜ |
| 6 | **Diagnostic settings** routing AVD logs to Log Analytics / Sentinel | Screenshot, PDF | ⬜ |

{{% alert type="tip" %}}
The Azure Landing Zone (ALZ) Default policy initiative already covers the
majority of this control. If the customer deployed ALZ, capture the
initiative assignment screenshot and the compliance state — that is
significant evidence in one shot.
{{% /alert %}}

---

## Evidence Guidance

### Defender for Cloud

Capture from **Microsoft Defender for Cloud → Environment settings →
&lt;AVD subscription&gt;**:

- Plans enabled (CSPM, Defender for Servers, Defender for Storage if FSLogix
  on Azure Files)
- Auto-provisioning of agents (MMA / AMA, vulnerability assessment)
- Secure score over time (trend, not just snapshot)

### Azure Policy

Capture from **Policy → Compliance**:

- Initiative(s) assigned to the AVD management group / subscription
- Number of compliant / non-compliant resources
- A drill-down on at least one AVD-specific policy (e.g. disk encryption,
  network access)

### Entra Conditional Access

Capture from **Entra ID → Conditional Access → Policies**:

- Policy targeting the AVD client app(s) / cloud apps
- Conditions applied (require MFA, compliant device, location)
- Sign-in logs sample showing the policy was enforced

---

## Evidence Status

| Evidence Item | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| Defender for Cloud enabled | | | ⬜ | |
| Secure score | | | ⬜ | |
| Azure Policy assignments | | | ⬜ | |
| Conditional Access policy | | | ⬜ | |
| Privileged access (PIM) | | | ⬜ | |
| Diagnostic settings | | | ⬜ | |

---

## Common Gaps

| Gap | Remediation |
|---|---|
| Defender for Cloud is on the management group but not the AVD subscription | Confirm scope inheritance; capture the AVD subscription screenshot specifically |
| Policy assignments exist but no compliance state is shown | Capture the compliance % and a drill-down for at least one policy |
| Conditional Access exists for Azure but is not scoped to AVD client sign-in | Add a CA policy targeting the AVD cloud app and capture a sign-in log entry |
| AVD admins are permanent role-holders, no PIM | Move to PIM eligible assignments and capture an activation request as evidence |
