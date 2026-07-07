# Labels

Use labels to make review state clear and searchable. The script
`scripts/create-labels.sh` creates or updates the labels listed here.

## Type labels

- `type: affiliation-request` — request to affiliate a project with OSL.
- `type: maintenance-review` — review of an affiliated project's health.
- `type: removal-review` — review removal from OSL public lists.
- `type: reactivation-request` — request to restore affiliation.
- `type: documentation` — documentation changes.
- `type: automation` — automation, scripts, or workflows.

## Status labels

- `status: needs-triage` — needs initial review.
- `status: needs-info` — waiting for applicant or maintainer information.
- `status: in-review` — under OSL review.
- `status: approved` — approved by OSL.
- `status: declined` — declined by OSL.
- `status: paused` — paused pending changes or maintainer response.
- `status: at-risk` — project may lose affiliation if unresolved.
- `status: removed` — removed from public affiliation list.
- `status: reactivated` — affiliation restored.

## Check labels

- `check: license` — license needs review.
- `check: code-of-conduct` — Code of Conduct needs review.
- `check: maintenance` — maintenance status needs review.
- `check: links` — links need review.
- `check: security` — security reporting needs review.
- `check: acknowledgement` — README/docs acknowledgement needs review.
- `check: gsoc-readiness` — GSoC/internship readiness needs review.
- `check: metadata` — project metadata needs review.

## Priority labels

- `priority: low` — low priority.
- `priority: medium` — medium priority.
- `priority: high` — high priority.

## Decision labels

- `decision: accepted` — accepted decision.
- `decision: declined` — declined decision.
- `decision: deferred` — deferred decision.

## Bot labels

- `bot: health-check` — created or updated by health-check automation.
- `bot: stale` — created or updated by stale automation.
- `bot: link-check` — created or updated by link-check automation.
