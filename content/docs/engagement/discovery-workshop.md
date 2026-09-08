+++
title = 'Discovery – AVD Workshop Kit'
linkTitle = 'Discovery Workshop'
description = 'Structured 1–2 day discovery workshop kit for Azure Virtual Desktop engagements.'
weight = 30
toc = true
+++

{{% alert type="tip" title="Download the workfiles" %}}
- {{< download href="/templates/engagement/discovery-workshop-deck.pptx" >}}Workshop deck (PPTX){{< /download >}}
- {{< download href="/templates/engagement/discovery-workshop-workbook.xlsx" >}}Workshop workbook (XLSX){{< /download >}}
{{% /alert %}}

## When to use this

After the customer has completed (or partially completed) the
[Qualification Questionnaire](/docs/engagement/qualification-questionnaire) and committed
to a paid engagement.

## Inputs you need from the customer

| # | Input | Source | Format |
|---|---|---|---|
| 1 | Completed (or in-progress) qualification questionnaire | EUC team | Document |
| 2 | App inventory export | IT / SCCM / Intune | Excel / CSV |
| 3 | Network diagram (current) | Network team | Visio / PDF |
| 4 | Identity overview | Identity team | Document |
| 5 | Workshop attendees: business sponsor, EUC, identity, security, network, ops, app owner reps | Customer | Calendar |

## Workshop structure (1–2 days)

### Day 1 – Discover

1. **Kick-off + objectives** (30 min)

   Recap business context, review qualification questionnaire summary,
   align on workshop outputs.

2. **Persona deep-dive** (90 min)

   Walk each persona row by row. Confirm user counts, working hours,
   special needs. Tag personas as **must-have** vs **fast-follow**.

3. **App inventory triage** (120 min)

   Per app: MSI / MSIX / AppAttach / Intune / M365 Apps / streamed
   decision. Flag blockers (incompatible, COM, GPU). Output: app delivery
   matrix.

4. **Identity & security session** (60 min)

   Entra-join vs hybrid. CA policies. PIM for AVD admins. Data residency.
   Endpoint isolation requirements.

5. **Network session** (60 min)

   RDP Shortpath feasibility, peering / private endpoints, DNS for
   FSLogix, firewall egress allow-list.

### Day 2 – Decide

1. **Image strategy decision** (60 min)

   Marketplace + customisation vs gold image. Pipeline. Refresh cadence.
   Validation approach. Owner post-handover.

2. **Profile storage decision** (60 min)

   Azure Files Premium vs ANF. Auth (AD / Entra Kerberos). Container size
   budget. Office container split.

3. **Reference architecture selection** (60 min)

   Map each persona to one of the [three reference architectures](/docs/engagement/reference-architectures):
   single-session, multi-session pooled, personal.

4. **Sizing & cost model** (90 min)

   Sessions per host per persona. Host SKU. Total hosts. RI / Savings Plan
   eligibility. Scaling plan working hours.

5. **Risk & decision register** (45 min)

   Capture open risks, decisions taken, decisions deferred.

6. **Wrap + next steps** (30 min)

   Confirm: HLD due date, PoC scope, customer attendees for next phase.

## Output: customer-ready deliverable

A **Discovery Output Pack** containing:

- Updated persona matrix
- App delivery decision matrix
- Identity, security, network decisions
- Image strategy decision record
- Profile storage decision record
- Persona-to-architecture mapping
- Sizing & cost model (rough)
- Risk register
- Decisions log

This pack feeds directly into the [HLD](/docs/engagement/deliverables/hld-template) and
into the audit evidence for
[B.1.1 Workload Assessment](/docs/module-b/1-1-workload-assessment).

## Reuse & contribute back

{{% alert type="tip" %}}
Found a workshop section that always runs over / under? Adjust the timings
and open a PR with a one-line note in the commit explaining what you saw
in the field.
{{% /alert %}}
