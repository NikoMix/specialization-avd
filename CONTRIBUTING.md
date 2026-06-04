# Contributing

This repository is **innersource** — every consultant who runs an AVD engagement
is expected to contribute lessons, control refinements, and template
improvements back to it.

## When to contribute

| You did this | Open this |
|---|---|
| Found a missing evidence item the auditor asked for | PR against `src/content/docs/module-a/` or `module-b/` + issue with `audit-evidence` label |
| Discovered a faster way to gather an existing evidence item | PR against the relevant control page |
| Improved a customer deliverable template after using it | PR against `src/content/docs/engagement/deliverables/` |
| Hit a customer scenario the qualification questionnaire didn't cover | PR against `qualification-questionnaire.mdx` |
| Identified a new reference architecture variant | PR against `reference-architectures.mdx` + an ADR-style write-up |
| Anything you wish you'd known on day 1 | Issue using the **Lesson Learned** template |

## Branching

- Base: `main`
- Feature branches: `engagement/<short-slug>`, `control/<ref>-<slug>`,
  `template/<short-slug>`, `lesson/<short-slug>`
- PRs **squash-merge** to keep history readable.

## Review SLA

- First reviewer response: **within 5 business days**
- Practice lead endorsement: **within 10 business days**

See [CODEOWNERS](CODEOWNERS) for content-area reviewers.

## PR checklist

Use [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md).
A good PR explains:

1. The engagement phase / control number it maps to
2. The customer scenario that prompted the change
3. Whether it changes evidence requirements (if so, update
   `.github/scripts/create-issues.sh` so issue checklists stay aligned)
4. Whether MDX syntax rules (see `.github/memories/mdx-content.md`) were
   followed (escape `<` before letter/digit/space → `&lt;`)

## Content lifecycle

| Stage | Meaning |
|---|---|
| **Draft** | Page exists but is incomplete or unreviewed |
| **Reviewed** | Peer-reviewed by another consultant |
| **Endorsed** | Approved by the practice lead listed in CODEOWNERS |
| **Deprecated** | No longer recommended; kept for reference |

See [`src/content/docs/innersource/content-governance.mdx`](src/content/docs/innersource/content-governance.mdx).

## Code of conduct

Be specific, respectful, and customer-anonymising. No real customer names,
revenue figures, or identifiable system details in this repository.
