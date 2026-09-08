+++
title = 'A.2.2 – Well-Architected Workloads'
linkTitle = '2.2 Well-Architected Workloads'
description = 'Evidence requirements for control A.2.2 – a Microsoft Well-Architected Framework assessment for at least one delivered AVD workload.'
weight = 40
toc = true
modules = ['Module A']
+++

## What the Auditor Checks

The auditor verifies that you applied the **Microsoft Well-Architected
Framework (WAF)** to at least one delivered AVD workload — using a published
assessment instrument, with recommendations triaged and tracked.

**Typical questions:**
- Where is the WAF assessment output?
- Which AVD workload was assessed?
- Were recommendations triaged into accept / action / backlog?

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **WAF assessment output** for the AVD workload (all five pillars: Reliability, Security, Cost Optimization, Operational Excellence, Performance Efficiency) | PDF, Word | ⬜ |
| 2 | **Recommendation register** with status (accepted / actioned / backlog / declined-with-rationale) | Excel, PDF, ADO / Jira export | ⬜ |
| 3 | **Workshop minutes** showing the assessment was customer-facing, not internal-only | PDF, Word, Email | ⬜ |
| 4 | **Re-assessment cadence** documented (when will it be repeated) | PDF, Word | ⬜ |

{{% alert type="tip" %}}
Use the official **Microsoft Azure Well-Architected Review** assessment
(azure.com/architecture/framework/cost/azure-well-architected-review).
Export the result PDF and pair it with your triage spreadsheet. This is
the cleanest possible evidence shape.
{{% /alert %}}

---

## Evidence Guidance

### WAF assessment output

- Use the **Azure Well-Architected Review** tool with the **Azure Virtual
  Desktop** workload lens selected
- Cover all five pillars (do not skip any — the auditor will check)
- Export the result as PDF; do not just attach the share link

### Recommendation register

| Pillar | Recommendation | Severity | Decision | Owner | Status |
|---|---|---|---|---|---|
| Cost | Implement scaling plan for pooled hosts | High | Accept | | Done |
| Reliability | Add validation host pool for ring-based updates | Medium | Accept | | In progress |
| Performance | Move profile share to Premium tier | High | Accept | | Done |

### AVD-specific WAF guidance

See the engagement playbook page
[WAF Assessment](/docs/engagement/waf-assessment) for AVD-specific levers
across Cost, Performance, Reliability.

---

## Evidence Status

| Evidence Item | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| WAF assessment output | | | ⬜ | |
| Recommendation register | | | ⬜ | |
| Workshop minutes | | | ⬜ | |
| Re-assessment cadence | | | ⬜ | |

---

## Common Gaps

| Gap | Remediation |
|---|---|
| Assessment was internal-only, no customer participation | Re-run as a workshop with the customer present; capture minutes |
| Recommendations exist but no triage / decisions | Walk the register with the customer and capture accept / action / decline outcomes |
| Some WAF pillars skipped | Re-run the assessment covering all five pillars |
| No re-assessment cadence stated | Document a 12-month re-assessment commitment in the engagement DoD |
