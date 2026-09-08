+++
title = 'Innersource – Contributing'
linkTitle = 'Contributing'
description = 'How to contribute back to this AVD specialization repository — branching, PRs, review SLA, governance.'
weight = 10
toc = true
+++

## Why innersource

This repository is the partner's **shared brain** for AVD engagements.
Every consultant who runs an engagement is expected to contribute back:
control refinements, template improvements, reference architecture
variants, lessons learned.

If you delivered something you wish you'd known on day one — file it here so
the next consultant doesn't have to learn it the hard way.

## Quick links

- [Branching, PRs, review SLA](https://github.com/) → see the root
  [`CONTRIBUTING.md`](https://github.com/)
- [Content governance lifecycle](/docs/innersource/content-governance)
- [Roadmap & backlog](/docs/innersource/roadmap)
- Issue templates: control improvement, template improvement, lesson learned

## What goes where

| You learned this | Open this |
|---|---|
| The auditor asked for an evidence item we don't list | PR a new row in the relevant control page — the issues workflow reads that table directly |
| A faster way to gather an existing evidence item | PR the relevant control page's "Evidence Guidance" section |
| A customer scenario the qualification questionnaire missed | PR `engagement/qualification-questionnaire.md` |
| A WAF lever that was a big win | PR `engagement/waf-assessment.md` |
| A reference architecture variant | PR `engagement/reference-architectures.md` |
| A runbook procedure that resolved a tricky incident | PR `engagement/deliverables/runbook-template.md` |
| Anything else worth remembering | Open a lesson-learned issue |

## Content rules reminder

See `.github/memories/hugo-content.md`. The most common traps:

| ❌ Wrong | ✅ Right |
|---|---|
| A table indented inside a numbered list | A `###` heading, table at column 0 |
| `{{</* alert */>}}` around Markdown | `{{%/* alert */%}}` around Markdown |
| A plain Markdown link to a file under `static/` | The `download` shortcode, so the Pages sub-path is applied |
| `[B.2.1](../module-b/2-1-solution-design/)` | `[B.2.1](/docs/module-b/2-1-solution-design)` |

## Review SLA

- First reviewer response: within **5 business days**
- Practice lead endorsement: within **10 business days**

See [CODEOWNERS](https://github.com/) for content-area reviewers.

{{% alert type="tip" %}}
Small PRs are reviewed fastest. If you have a big change, split it
into a "structural" PR (rename, move, format) and a "content" PR
(the actual change).
{{% /alert %}}
