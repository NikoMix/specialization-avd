+++
title = 'B.4.1 – Service Validation and Testing'
linkTitle = '4.1 Service Validation and Testing'
description = 'Evidence requirements for control B.4.1 – test plan and results covering logon performance, app launch, scaling, failover, and profile container integrity.'
weight = 60
toc = true
modules = ['Module B']
+++

## What the Auditor Checks

The auditor verifies that the AVD service was **systematically tested**
before and during Go-Live — not just smoke-tested by the project team.

**Typical questions:**
- Where is the test plan?
- What did you test for logon performance, app launch, scaling, failover,
  and FSLogix profile integrity?
- Where are the test results?

---

## Required Evidence Checklist

| # | Evidence Item | Accepted Formats | Status |
|---|---|---|---|
| 1 | **Test plan** covering categories below | PDF, Word, Excel | ⬜ |
| 2 | **Logon performance test** results (cold and warm logons per persona) | PDF, Excel, AVD Insights export | ⬜ |
| 3 | **App launch test** results (key apps, per persona) | PDF, Excel | ⬜ |
| 4 | **Scaling test** — autoscale up / down behaviour under simulated load | PDF, Excel, AVD Insights export | ⬜ |
| 5 | **Failover / resilience test** — host failure, FSLogix share unavailability, region failover (if BCDR active) | PDF, Word | ⬜ |
| 6 | **FSLogix profile container integrity test** — repeated logon, corruption recovery | PDF, Word | ⬜ |
| 7 | **Network test** — RDP Shortpath, latency, throughput per region | PDF, Excel | ⬜ |
| 8 | **User acceptance test (UAT)** results from pilot / early production users | PDF, Excel, Survey export | ⬜ |
| 9 | **Test execution sign-off** | PDF, Word, Email | ⬜ |

---

## Evidence Guidance

### Logon performance

Test cold and warm logons per persona. Capture P50 / P95 / P99 from AVD
Insights' Connection Diagnostics for the test window. Pass thresholds:

| Persona | Cold logon P95 | Warm logon P95 |
|---|---|---|
| Knowledge worker | &lt; 30s | &lt; 10s |
| Power user / developer | &lt; 45s | &lt; 15s |
| Call centre | &lt; 25s | &lt; 8s |

### Scaling test

- Simulate ramp-up at start of working hours; verify hosts come online before
  user logons fail
- Simulate ramp-down; verify hosts drain and deallocate per scaling plan
- Verify min host count is respected
- Capture cost telemetry for one ramped day vs one fully-allocated day

### Failover / resilience

- Force-stop a session host; verify users land on a healthy host
- Force-unmount the FSLogix share; verify alerting fires and user impact
- If BCDR active: invoke region failover in a controlled window

### FSLogix integrity

- Log in / log out a test user 20+ times; verify container size remains
  within expected bounds and no corruption
- Inject a simulated container error; verify recovery runbook works

---

## Evidence Status

| Evidence Item | Owner | Due Date | Status | Notes |
|---|---|---|---|---|
| Test plan | | | ⬜ | |
| Logon performance | | | ⬜ | |
| App launch | | | ⬜ | |
| Scaling | | | ⬜ | |
| Failover / resilience | | | ⬜ | |
| FSLogix integrity | | | ⬜ | |
| Network test | | | ⬜ | |
| UAT | | | ⬜ | |
| Test sign-off | | | ⬜ | |

---

## Common Gaps

| Gap | Remediation |
|---|---|
| Logon perf claimed verbally but no telemetry | Pull AVD Insights for the test window and attach |
| Scaling plan deployed but never actually exercised under load | Run a synthetic load test (even a few dozen scripted sessions) |
| FSLogix integrity not tested | Run the repeated-logon test and document the runbook recovery steps |
| Failover plan documented but never executed even once | Conduct a controlled failover drill and capture it |
