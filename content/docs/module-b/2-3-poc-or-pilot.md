+++
title = 'B.2.3 – PoC or Pilot'
linkTitle = '2.3 PoC or Pilot'
description = 'Evidence requirements for control B.2.3 – Proof of Concept or Pilot with defined scope, success criteria, results, and customer sign-off.'
weight = 40
toc = true
modules = ['Module B']
+++

## What the Auditor Checks

The auditor verifies that the engagement included either a **Proof of Concept
(PoC)** or a **Pilot** — and that it had defined **scope**, **success
criteria**, **measurable results**, and **customer sign-off** before
proceeding to production rollout.

| Term | Definition (V2.7.1 glossary) |
|---|---|
| **PoC** | Narrow validation of capability |
| **Pilot** | Limited production deployment to a subset of users |

**Typical questions:**
- Was it a PoC or a Pilot? What was the scope?
- What were the success criteria? Were they met?
- Was the customer sign-off captured before production rollout?

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **PoC / Pilot scope document** — users, apps, host pool topology, duration | PDF, Word | ⬜ |
| 2 | **Success criteria** — quantitative (logon time, app launch time, NPS, ticket volume, scaling cost) | PDF, Word | ⬜ |
| 3 | **Results report** — measured against the success criteria | PDF, Word | ⬜ |
| 4 | **User feedback** — survey output or session notes from pilot users | PDF, Excel, Survey export | ⬜ |
| 5 | **Issue log** — what broke, root cause, fix taken into production design | Excel, PDF, ADO / Jira export | ⬜ |
| 6 | **Decision to proceed** — written decision (go / no-go / iterate) | PDF, Word, Email | ⬜ |
| 7 | **Customer sign-off** on the PoC / Pilot outcome | PDF, Word, Email | ⬜ |

---

## Evidence Guidance

### Scope statement

| Field | Example |
|---|---|
| Type | Pilot |
| Pilot user count | 50 (1 department) |
| Apps in scope | M365, Edge, Teams, internal CRM (web) |
| Host pool topology | Pooled multi-session, Win 11 Enterprise multi-session 23H2 |
| Identity | Entra-joined, MFA via CA |
| Profile storage | FSLogix on Azure Files Premium |
| Duration | 4 weeks |
| Exit criteria | All success criteria met; user NPS ≥ 7 |

### Success criteria examples

| Criterion | Target | Measure |
|---|---|---|
| Logon time (cold) | &lt; 30s P95 | AVD Insights → Connection Diagnostics |
| App launch time (M365) | &lt; 5s P95 | User Input Delay |
| Connection failure rate | &lt; 1% | AVD Insights |
| Pilot user NPS | ≥ 7 | Microsoft Forms survey |
| Service desk tickets | &lt; 1 per user per week | ITSM export |

---

## Evidence Status

| Evidence Item | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| Scope document | | | ⬜ | |
| Success criteria | | | ⬜ | |
| Results report | | | ⬜ | |
| User feedback | | | ⬜ | |
| Issue log | | | ⬜ | |
| Decision to proceed | | | ⬜ | |
| Customer sign-off | | | ⬜ | |

---

## Common Gaps

| Gap | Remediation |
|---|---|
| Pilot ran but no formal success criteria upfront | Reconstruct from minutes / Teams chat; better: define criteria for every engagement going forward |
| No quantitative results — only "users were happy" | Pull retrospective data from AVD Insights for the pilot window |
| User feedback informal (corridor conversations) | Run a brief Microsoft Forms survey for pilot users; capture results |
| Went to production without a written go decision | Capture the decision retrospectively in writing and have the customer sign |
