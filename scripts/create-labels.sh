#!/usr/bin/env bash
set -euo pipefail

REPO="${1:-OpenScienceLabs/affiliation-requests}"

require_gh() {
  if ! command -v gh >/dev/null 2>&1; then
    echo "Error: gh CLI is required." >&2
    exit 1
  fi
}

create_label() {
  local name="$1"
  local color="$2"
  local description="$3"
  echo "Creating/updating label: ${name}"
  gh label create "$name" \
    --repo "$REPO" \
    --color "$color" \
    --description "$description" \
    --force
}

require_gh

create_label "type: affiliation-request" "0E8A16" "Request to affiliate a project with OSL"
create_label "type: maintenance-review" "FBCA04" "Review of project maintenance status"
create_label "type: removal-review" "B60205" "Review removal from OSL public lists"
create_label "type: reactivation-request" "5319E7" "Request to restore affiliation"
create_label "type: documentation" "0075CA" "Documentation changes"
create_label "type: automation" "1D76DB" "Automation, scripts, or workflows"

create_label "status: needs-triage" "D4C5F9" "Needs initial review"
create_label "status: needs-info" "F9D0C4" "Waiting for applicant or maintainer information"
create_label "status: in-review" "C2E0C6" "Under OSL review"
create_label "status: approved" "0E8A16" "Approved by OSL"
create_label "status: declined" "B60205" "Declined by OSL"
create_label "status: paused" "FEF2C0" "Paused pending changes or maintainer response"
create_label "status: at-risk" "D93F0B" "Project may lose affiliation if unresolved"
create_label "status: removed" "5319E7" "Removed from public affiliation list"
create_label "status: reactivated" "0E8A16" "Affiliation restored"

create_label "check: license" "BFDADC" "License needs review"
create_label "check: code-of-conduct" "BFDADC" "Code of Conduct needs review"
create_label "check: maintenance" "BFDADC" "Maintenance status needs review"
create_label "check: links" "BFDADC" "Links need review"
create_label "check: security" "BFDADC" "Security reporting needs review"
create_label "check: acknowledgement" "BFDADC" "README/docs acknowledgement needs review"
create_label "check: gsoc-readiness" "BFDADC" "GSoC/internship readiness needs review"
create_label "check: metadata" "BFDADC" "Project metadata needs review"

create_label "priority: low" "C5DEF5" "Low priority"
create_label "priority: medium" "FBCA04" "Medium priority"
create_label "priority: high" "B60205" "High priority"

create_label "decision: accepted" "0E8A16" "Accepted decision"
create_label "decision: declined" "B60205" "Declined decision"
create_label "decision: deferred" "FBCA04" "Deferred decision"

create_label "bot: health-check" "EDEDED" "Created or updated by health-check automation"
create_label "bot: stale" "EDEDED" "Created or updated by stale automation"
create_label "bot: link-check" "EDEDED" "Created or updated by link-check automation"

echo "Done."
