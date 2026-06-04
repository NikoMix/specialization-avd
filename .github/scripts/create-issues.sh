#!/usr/bin/env bash
# create-issues.sh
# Creates audit engagement issues for the Azure Virtual Desktop Advanced
# Specialization (checklist V2.7.1). Skips any issue whose title already exists
# (open or closed) within this cycle's label to avoid duplicates across re-runs.
#
# Environment variables expected:
#   GH_TOKEN     - GitHub token with issues:write permission
#   CYCLE_LABEL  - e.g. "audit-2026"
#   MILESTONE    - milestone title (e.g. "Audit 2026")
#   REPO         - owner/repo

set -euo pipefail

create_issue() {
  local title="$1"
  local labels="$2"
  local body="$3"

  local existing
  existing=$(gh issue list \
    --repo "$REPO" \
    --state all \
    --label "$CYCLE_LABEL" \
    --limit 200 \
    --json title \
    --jq "[.[] | select(.title == \"$title\")] | length")

  if [ "${existing:-0}" -gt 0 ]; then
    echo "Skipping (exists): $title"
    return
  fi

  gh issue create \
    --repo "$REPO" \
    --title "$title" \
    --label "$labels" \
    --milestone "$MILESTONE" \
    --body "$body"

  echo "Created: $title"
}

# ─── Pre-Qualification Gate ───────────────────────────────────────────────────

create_issue \
  "Pre-Qualification Gate (AVD V2.7.1)" \
  "pre-qualification,$CYCLE_LABEL" \
  "## Pre-Qualification Gate

Confirm all pre-qualification requirements are met **before** requesting the
Azure Virtual Desktop Advanced Specialization audit from Partner Center.

Reference: \`src/content/docs/requirements.mdx\`

---

### 1 - Solutions Partner designation

- [ ] Active **Solutions Partner for Infrastructure (Azure)** designation confirmed in Partner Center
- [ ] Screenshot of active designation exported

### 2 - Customer evidence (last 12 months)

- [ ] At least **2 unique customers** delivered in the last 12 months
- [ ] At least **1 customer is Native AVD**
- [ ] 2nd customer is Native AVD / Citrix on Azure / Horizon on Azure (anything else does not count)
- [ ] Customer sign-off captured for each engagement

### 3 - Audit scheduling

- [ ] Audit requested via Partner Center
- [ ] Auditor (ISSI) assignment received
- [ ] Kickoff call scheduled
- [ ] Module choice confirmed: Module B only (4h, \$2,400) vs Module A+B (8h, \$3,600)
"

# ─── Module A controls ────────────────────────────────────────────────────────

declare -A MODULE_A=(
  ["A.1.1 Cloud & AI Adoption Business Strategy"]="module-a/1-1-cloud-ai-adoption-business-strategy"
  ["A.1.2 Cloud & AI Adoption Plan"]="module-a/1-2-cloud-ai-adoption-plan"
  ["A.2.1 Security & Governance Tooling"]="module-a/2-1-security-governance-tooling"
  ["A.2.2 Well-Architected Workloads"]="module-a/2-2-well-architected-workloads"
  ["A.3.1 Repeatable Deployment"]="module-a/3-1-repeatable-deployment"
  ["A.3.2 Plan for Skilling"]="module-a/3-2-plan-for-skilling"
  ["A.3.3 Operations Management Tooling"]="module-a/3-3-operations-management-tooling"
)

for title in "${!MODULE_A[@]}"; do
  path="${MODULE_A[$title]}"
  create_issue \
    "$title" \
    "module-a,audit-evidence,$CYCLE_LABEL" \
    "## $title

Evidence collection for Module A control.

Reference: \`src/content/docs/${path}.mdx\`

- [ ] Required evidence items collected (see control page)
- [ ] Evidence filed in \`evidence/module-a/$(echo "$title" | awk '{print $1}')/\`
- [ ] Owner assigned and status tracked in evidence-tracker
- [ ] Internal peer review complete
"
done

# ─── Module B controls ────────────────────────────────────────────────────────

declare -A MODULE_B=(
  ["B.1.1 Workload Assessment"]="module-b/1-1-workload-assessment"
  ["B.2.1 Solution Design"]="module-b/2-1-solution-design"
  ["B.2.2 Azure Well-Architected Review"]="module-b/2-2-azure-well-architected-review"
  ["B.2.3 PoC or Pilot"]="module-b/2-3-poc-or-pilot"
  ["B.3.1 Deployment to Production"]="module-b/3-1-deployment-to-production"
  ["B.4.1 Service Validation and Testing"]="module-b/4-1-service-validation-and-testing"
  ["B.4.2 Post-deployment Documentation"]="module-b/4-2-post-deployment-documentation"
)

for title in "${!MODULE_B[@]}"; do
  path="${MODULE_B[$title]}"
  create_issue \
    "$title" \
    "module-b,audit-evidence,$CYCLE_LABEL" \
    "## $title

Evidence collection for Module B (AVD workload) control.

Reference: \`src/content/docs/${path}.mdx\`

- [ ] Required evidence items collected (see control page)
- [ ] Customer-specific evidence captured for each of the 2 qualifying customers
- [ ] Evidence filed in \`evidence/module-b/$(echo "$title" | awk '{print $1}')/\`
- [ ] Owner assigned and status tracked in evidence-tracker
- [ ] Internal peer review complete
"
done

echo "Done."
