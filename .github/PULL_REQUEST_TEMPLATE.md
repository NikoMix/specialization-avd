# Pull Request

## What & why

<!-- 1-3 sentences on the change and the customer scenario / engagement phase that prompted it -->

## Mapping

- **Engagement phase:** <!-- selling / qualification / discovery / design / PoC / deployment / validation / hypercare -->
- **Audit control(s) touched:** <!-- e.g. B.2.1, A.3.1 — or "none" -->
- **Reference architecture variant:** <!-- single-session / multi-session / personal / N/A -->

## Type of change

- [ ] New control / evidence item
- [ ] Refined existing control / evidence guidance
- [ ] New or updated template (HLD / LLD / runbook / KT / hypercare / questionnaire)
- [ ] New or updated reference architecture
- [ ] Lesson learned write-up
- [ ] Tooling / CI / build change

## Checks

- [ ] Markdown tables start at column 0 (never indented inside a list item or shortcode)
- [ ] Evidence checklist edits are made in the control page only — the issues workflow reads it directly
- [ ] No real customer names, revenue figures, or identifiable system details
- [ ] `hugo --gc --minify` passes locally
- [ ] `python3 scripts/verify-tables.py` passes locally
- [ ] Content lifecycle stage noted (Draft / Reviewed / Endorsed)

## Reviewer notes

<!-- Anything reviewers should pay extra attention to -->
