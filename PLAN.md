# PLAN: Prepare `OpenScienceLabs/affiliation-requests`

This document is intended for a future isolated Codex session that has write
access to the repository:

```text
~/dev/osl-projects/opensciencelabs/affiliation-requests
/mnt/HC_Volume_102749953/dev/osl-projects/opensciencelabs/affiliation-requests
```

The current session inspected the repository but could not write to it because
it is outside the writable roots. The repo exists, is clean, and currently has
only minimal files:

```text
.gitignore
LICENSE
README.md
```

The remote is:

```text
git@github.com:OpenScienceLabs/affiliation-requests.git
```

## Objective

Prepare the `affiliation-requests` repository as the operational home for OSL
Project Affiliation requests.

The website should remain the public policy/orientation layer, while this repo
should contain the operational workflow:

- request forms;
- review checklists;
- bot automation;
- label setup;
- maintenance reviews;
- removal/reactivation workflows;
- documentation for maintainers and reviewers.

This repo supports the policy documented on the OSL website at:

```text
opensciencelabs.github.io/pages/projects/affiliation/index.md
```

The relevant website language says that affiliation:

- is a lightweight relationship;
- does not transfer ownership or governance to OSL;
- requires an OSI-approved license;
- requires a Code of Conduct;
- requires active/reachable maintainers;
- requires public development;
- does not guarantee GSoC, internships, funding, grants, contributors, mentors,
  or promotion;
- expects projects to acknowledge OSL affiliation in README/docs;
- may be paused or removed if the project becomes inactive, unsafe,
  closed-source, misleading, hostile, or misaligned with OSL values.

## Key Policy Requirements to Encode

Every affiliation request should collect evidence for the following.

### Required

- Project has a clear open-source, open-science, research, education,
  public-interest, or open-technology purpose.
- Project uses an OSI-approved open-source license.
- Repository includes a public `LICENSE` file.
- Project includes `CODE_OF_CONDUCT.md` or equivalent public Code of Conduct
  with a reporting path.
- Project has at least one active or reachable maintainer.
- Project has a public repository.
- Project has a public issue tracker, discussion channel, project board, or
  documented contact path.
- Project is not archived, closed-source, abandoned, misleading, or unsafe for
  contributors.
- Maintainers understand affiliation does not transfer ownership, governance,
  intellectual property, or maintenance responsibility to OSL.
- If accepted, maintainers will acknowledge affiliation in `README.md` and,
  where applicable, public documentation.

### Recommended

- README explains project purpose, users, and current status.
- CONTRIBUTING instructions exist.
- Basic user/developer documentation exists.
- Roadmap, project ideas, starter issues, or labels for contributors exist.
- SECURITY.md or vulnerability reporting path exists where relevant.
- Recent releases, commits, issue responses, or stable-maintenance status exist.
- Project can explain what collaboration it seeks through OSL.

### Boundaries

Affiliation does **not** mean:

- OSL owns the repository, name, logo, code, data, IP, or governance;
- OSL maintains the project;
- OSL certifies correctness, security, legal, ethical, medical, scientific, or
  financial quality;
- OSL endorses every decision, release, public statement, dependency, or
  integration;
- OSL guarantees funding, contributors, interns, mentors, grants, sponsorship,
  fiscal hosting, promotion, or event participation;
- OSL guarantees GSoC participation or a GSoC contributor slot;
- the project can use OSL branding in a way that suggests ownership,
  certification, sponsorship, or control without written permission.

### GSoC / Limited Programs

The repo should make clear that:

- Affiliated projects may submit ideas for GSoC, internships, grants, or similar
  programs only when OSL is participating and the project is ready.
- OSL will do its best to participate in GSoC where possible.
- Participation depends on external selection, OSL capacity, mentor
  availability, project readiness, and limited slots.
- Even when OSL participates, not every affiliated project idea can be selected
  or funded.

### Acknowledgement Requirement

Accepted projects should add a README/docs acknowledgement.

Suggested wording:

```markdown
## Open Science Labs Affiliation

This project is affiliated with Open Science Labs (OSL). Affiliation means that
the project aligns with OSL's mission and is connected to the OSL ecosystem,
while governance, roadmap, maintenance, and releases remain the responsibility
of the project maintainers.
```

Projects should remove or update this text if affiliation is paused, removed,
or changed.

## Proposed Repository Structure

Create this structure:

```text
README.md
CONTRIBUTING.md
CODE_OF_CONDUCT.md
SECURITY.md

.github/
  ISSUE_TEMPLATE/
    affiliation-request.yml
    maintenance-review.yml
    removal-review.yml
    reactivation-request.yml
    config.yml
  PULL_REQUEST_TEMPLATE.md
  workflows/
    affiliation-intake.yml
    health-check.yml
    stale.yml
    link-check.yml
    label-check.yml

docs/
  criteria.md
  workflow.md
  reviewer-guide.md
  maintainer-guide.md
  bot-workflows.md
  labels.md
  acknowledgement.md

scripts/
  create-labels.sh
  check-affiliated-projects.py
  validate-issue-forms.py
```

Optional later additions:

```text
data/
  affiliated-projects.yml
  removed-projects.yml
  reviewers.yml
```

The optional `data/` directory can be used if the repo becomes the canonical
operational registry. For now, the website project list may remain canonical.

## README.md Requirements

Rewrite `README.md` into a complete public landing page.

Suggested sections:

1. **Title**: OSL Affiliation Requests
2. **Purpose**
   - This repo is for requesting affiliation with Open Science Labs.
   - It hosts public requests, review records, maintenance reviews, and
     reactivation/removal discussions.
3. **What affiliation means**
   - Lightweight relationship, not ownership.
4. **Who should apply**
   - Existing open-source/open-science/open-technology projects with maintainers.
5. **Before applying**
   - Required criteria checklist.
6. **How to request affiliation**
   - Open a GitHub issue using the affiliation request form.
7. **Review workflow**
   - Request opened -> completeness check -> eligibility review -> maintainer
     follow-up -> decision -> website update -> onboarding -> periodic review.
8. **GSoC and limited programs**
   - Not guaranteed; slots are limited.
9. **Acknowledgement requirement**
   - README/docs text for accepted projects.
10. **Maintenance reviews**
    - Projects may be marked at risk or removed.
11. **Useful links**
    - OSL website, Discord, Code of Conduct, project list.

## docs/criteria.md

Create a detailed criteria page.

Include:

- Required criteria.
- Recommended criteria.
- Reasons requests may be declined.
- Reasons affiliation may be paused or removed.
- Program-readiness criteria for GSoC/internships.
- Acknowledgement requirement.

Suggested decline reasons:

- no OSI-approved license;
- missing Code of Conduct;
- no reachable maintainer;
- repository is private/archived/abandoned;
- project is not aligned with OSL;
- unsafe community practices;
- misleading use of OSL name;
- unclear ownership/license status;
- project is not ready for contributors;
- application lacks evidence and maintainers did not respond.

## docs/workflow.md

Document the workflow:

```text
1. Maintainer opens affiliation request issue.
2. Bot labels issue: type: affiliation-request, status: needs-triage.
3. Bot checks required fields if possible.
4. Reviewer performs completeness check.
5. Reviewer requests missing info using status: needs-info if needed.
6. Maintainer updates issue.
7. Reviewer performs eligibility review.
8. Optional public/community comment period.
9. Decision:
   - approved
   - needs changes
   - declined
10. If approved:
   - add label status: approved
   - open/update website PR to add project listing
   - confirm acknowledgement requirement
   - optionally create follow-up onboarding checklist
11. Periodic maintenance checks continue after listing.
```

Decision states:

- `status: needs-triage`
- `status: needs-info`
- `status: in-review`
- `status: approved`
- `status: declined`
- `status: paused`
- `status: at-risk`
- `status: removed`
- `status: reactivated`

## docs/reviewer-guide.md

Add reviewer instructions:

- Be transparent and kind.
- Ask for links/evidence, not only claims.
- Do not approve if license or Code of Conduct is missing.
- Do not approve if maintainers are unreachable.
- Do not imply funding/GSoC availability.
- Make boundaries explicit.
- If unsure, mark `needs-info` or ask another reviewer.
- Use labels consistently.
- Leave a decision comment when approving/declining.

Suggested approval comment:

```markdown
Thanks for your request. OSL has approved this project for affiliation.

Next steps:

- Please add the OSL affiliation acknowledgement to your README/docs.
- OSL will add the project to the public project list.
- Participation in GSoC, internships, grants, or sponsorship opportunities is
  not guaranteed and depends on program availability, mentor capacity, project
  readiness, and limited slots.
- The project remains independently governed and maintained by its maintainers.
```

Suggested declined comment:

```markdown
Thanks for your request. OSL cannot approve affiliation at this time because:

- ...

You are welcome to apply again after addressing these points.
```

## docs/maintainer-guide.md

Explain maintainers' responsibilities:

- keep license and Code of Conduct in place;
- keep maintainers reachable;
- keep links and metadata accurate;
- respond to maintenance review pings;
- update README/docs acknowledgement;
- notify OSL if project is archived, moved, renamed, transferred, relicensed,
  paused, or no longer wants affiliation;
- do not imply OSL ownership/certification.

Include GSoC/internship readiness:

- mentors available;
- scoped ideas;
- clear public issues;
- communication channels;
- contributor review capacity;
- project idea does not guarantee slot.

## docs/bot-workflows.md

Document automation intent.

Bots should support human review, not replace it.

### Intake bot

Triggered on issue open/edit.

Responsibilities:

- label based on issue form;
- warn if required sections are empty;
- add `status: needs-triage`;
- optionally add `status: needs-info` if obvious required links are missing.

### Health-check bot

Runs quarterly, with manual dispatch.

Checks:

- repo reachable;
- repo public;
- repo not archived;
- LICENSE exists;
- Code of Conduct exists;
- README exists;
- optional CONTRIBUTING exists;
- optional SECURITY exists;
- last push date;
- issue/PR activity;
- listed URL works;
- maintainer/user exists where detectable.

Outputs:

- summary in workflow logs;
- creates/updates maintenance review issue for failures;
- applies labels such as `status: at-risk`, `check: license`, etc.;
- never removes affiliation without human review.

### Stale/needs-info bot

For request issues:

- after 30 days waiting on applicant, comment and keep `status: needs-info`;
- after 60 days waiting on applicant, mark `status: paused` or close as
  incomplete;
- allow applicants to reopen/reapply.

For maintenance reviews:

- Day 0: issue opened and maintainers pinged;
- Day 30: mark at risk if no response;
- Day 60: open removal review;
- Day 90: human may remove from website list.

### Link check bot

Runs weekly or on PR.

Checks links in Markdown files and issue templates.

## docs/labels.md

Document labels and their meanings. The label script should create these.

### Type labels

- `type: affiliation-request`
- `type: maintenance-review`
- `type: removal-review`
- `type: reactivation-request`
- `type: documentation`
- `type: automation`

### Status labels

- `status: needs-triage`
- `status: needs-info`
- `status: in-review`
- `status: approved`
- `status: declined`
- `status: paused`
- `status: at-risk`
- `status: removed`
- `status: reactivated`

### Check labels

- `check: license`
- `check: code-of-conduct`
- `check: maintenance`
- `check: links`
- `check: security`
- `check: acknowledgement`
- `check: gsoc-readiness`
- `check: metadata`

### Priority labels

- `priority: low`
- `priority: medium`
- `priority: high`

### Decision labels

- `decision: accepted`
- `decision: declined`
- `decision: deferred`

### Bot labels

- `bot: health-check`
- `bot: stale`
- `bot: link-check`

## docs/acknowledgement.md

Include:

- required acknowledgement text;
- allowed phrases;
- disallowed phrases;
- examples.

Allowed:

```text
OSL affiliated project
Affiliated with Open Science Labs
```

Disallowed unless separately agreed:

```text
OSL certified
OSL approved software
OSL maintained project
Official OSL project
OSL guarantees this project
```

## .github/ISSUE_TEMPLATE/config.yml

Create:

```yaml
blank_issues_enabled: false
contact_links:
  - name: Open Science Labs website
    url: https://opensciencelabs.org/
    about: Learn more about OSL.
  - name: OSL Discord
    url: https://opensciencelabs.org/discord
    about: Join the OSL community.
  - name: Email OSL
    url: mailto:team@opensciencelabs.org
    about: Contact OSL if GitHub is not accessible to you.
```

## .github/ISSUE_TEMPLATE/affiliation-request.yml

Create a GitHub issue form. Important: include checkboxes for requirements,
GSoC disclaimer, and acknowledgement.

Suggested content:

```yaml
name: Affiliation request
description: Request affiliation with Open Science Labs
title: "Affiliation request: <project name>"
labels:
  - "type: affiliation-request"
  - "status: needs-triage"
body:
  - type: markdown
    attributes:
      value: |
        Thanks for requesting affiliation with Open Science Labs (OSL).

        Affiliation is a lightweight relationship. It does not transfer project
        ownership, governance, intellectual property, maintenance responsibility,
        or roadmap control to OSL.

        Participation in Google Summer of Code, internships, grants, sponsorship,
        or similar opportunities is not guaranteed. Even when OSL participates
        in GSoC, contributor slots are limited.

  - type: input
    id: project_name
    attributes:
      label: Project name
      placeholder: Example Project
    validations:
      required: true

  - type: input
    id: repository
    attributes:
      label: Repository URL
      placeholder: https://github.com/org/project
    validations:
      required: true

  - type: input
    id: website
    attributes:
      label: Website or documentation URL
      placeholder: https://example.org/project
    validations:
      required: false

  - type: textarea
    id: description
    attributes:
      label: Short description
      description: What does the project do and who is it for?
    validations:
      required: true

  - type: textarea
    id: alignment
    attributes:
      label: Alignment with OSL
      description: How does this project align with open science, open source, research, education, public-interest technology, or open infrastructure?
    validations:
      required: true

  - type: input
    id: license
    attributes:
      label: License link
      placeholder: https://github.com/org/project/blob/main/LICENSE
    validations:
      required: true

  - type: input
    id: code_of_conduct
    attributes:
      label: Code of Conduct link
      placeholder: https://github.com/org/project/blob/main/CODE_OF_CONDUCT.md
    validations:
      required: true

  - type: textarea
    id: maintainers
    attributes:
      label: Maintainers
      description: List maintainer names, GitHub handles, and public contact path.
      placeholder: "- Name (@handle), email or contact path"
    validations:
      required: true

  - type: input
    id: communication
    attributes:
      label: Public communication channel or contact path
      placeholder: GitHub Discussions, Discord, mailing list, issue tracker, etc.
    validations:
      required: true

  - type: dropdown
    id: maintenance_status
    attributes:
      label: Maintenance status
      options:
        - Active
        - Maintained / stable
        - Temporarily paused
        - Other / explain below
    validations:
      required: true

  - type: textarea
    id: maintenance_notes
    attributes:
      label: Maintenance notes
      description: Describe recent activity, stable status, release cadence, or maintenance plan.
    validations:
      required: true

  - type: input
    id: contributing
    attributes:
      label: Contribution instructions URL
      placeholder: https://github.com/org/project/blob/main/CONTRIBUTING.md
    validations:
      required: false

  - type: input
    id: security
    attributes:
      label: Security policy or vulnerability reporting URL
      placeholder: https://github.com/org/project/blob/main/SECURITY.md
    validations:
      required: false

  - type: textarea
    id: collaboration
    attributes:
      label: What collaboration are you seeking through OSL?
      description: Visibility, community connection, internships, GSoC ideas, grants, mentorship, etc.
    validations:
      required: true

  - type: textarea
    id: program_readiness
    attributes:
      label: Program readiness, if applicable
      description: If you want internships or GSoC, describe project ideas, mentors, and review capacity. If not applicable, write N/A.
    validations:
      required: true

  - type: checkboxes
    id: required_checks
    attributes:
      label: Required checks
      options:
        - label: The project uses an OSI-approved open-source license.
          required: true
        - label: The repository includes a public LICENSE file.
          required: true
        - label: The project has a Code of Conduct with a reporting path.
          required: true
        - label: The project has at least one active or reachable maintainer.
          required: true
        - label: The project has a public repository.
          required: true
        - label: The project has a public issue tracker, discussion channel, project board, or documented contact path.
          required: true
        - label: The project is not archived, closed-source, abandoned, misleading, or unsafe for contributors.
          required: true
        - label: I understand affiliation does not transfer ownership, governance, IP, roadmap, or maintenance responsibility to OSL.
          required: true
        - label: If accepted, we will acknowledge OSL affiliation in README.md and public documentation where applicable.
          required: true
        - label: I understand GSoC, internships, grants, funding, contributors, mentors, and promotion are not guaranteed.
          required: true
```

## .github/ISSUE_TEMPLATE/maintenance-review.yml

Create:

```yaml
name: Maintenance review
description: Review an affiliated project that may need attention
title: "Maintenance review: <project name>"
labels:
  - "type: maintenance-review"
  - "status: needs-triage"
body:
  - type: input
    id: project_name
    attributes:
      label: Project name
    validations:
      required: true
  - type: input
    id: repository
    attributes:
      label: Repository URL
    validations:
      required: true
  - type: checkboxes
    id: concerns
    attributes:
      label: Concerns
      options:
        - label: Missing or unclear license
        - label: Missing Code of Conduct
        - label: Repository archived
        - label: Repository unreachable
        - label: Website/docs link broken
        - label: Maintainer unreachable
        - label: No recent activity and no stable-maintenance note
        - label: Unsafe or hostile community behavior
        - label: Misleading OSL affiliation/branding language
        - label: Other
  - type: textarea
    id: details
    attributes:
      label: Details and evidence
    validations:
      required: true
  - type: textarea
    id: maintainer_pings
    attributes:
      label: Maintainers to ping
      placeholder: "@maintainer1 @maintainer2"
    validations:
      required: false
```

## .github/ISSUE_TEMPLATE/removal-review.yml

Create:

```yaml
name: Removal review
description: Review whether to remove an affiliated project from OSL public lists
title: "Removal review: <project name>"
labels:
  - "type: removal-review"
  - "status: in-review"
body:
  - type: markdown
    attributes:
      value: |
        Removal from the OSL public list is not permanent. A project may request
        reactivation after restoring baseline requirements and maintenance.
  - type: input
    id: project_name
    attributes:
      label: Project name
    validations:
      required: true
  - type: input
    id: repository
    attributes:
      label: Repository URL
    validations:
      required: true
  - type: input
    id: prior_review
    attributes:
      label: Prior maintenance review issue
      placeholder: https://github.com/OpenScienceLabs/affiliation-requests/issues/123
    validations:
      required: true
  - type: checkboxes
    id: removal_reasons
    attributes:
      label: Removal reasons
      options:
        - label: No maintainer response after review period
        - label: Missing license not resolved
        - label: Missing Code of Conduct not resolved
        - label: Repository archived or unreachable
        - label: Project closed-source or relicensed incompatibly
        - label: Project unsafe or misaligned with OSL values
        - label: Maintainers requested removal
        - label: Other
  - type: textarea
    id: evidence
    attributes:
      label: Evidence and timeline
    validations:
      required: true
```

## .github/ISSUE_TEMPLATE/reactivation-request.yml

Create:

```yaml
name: Reactivation request
description: Request reactivation after affiliation was paused or removed
title: "Reactivation request: <project name>"
labels:
  - "type: reactivation-request"
  - "status: needs-triage"
body:
  - type: input
    id: project_name
    attributes:
      label: Project name
    validations:
      required: true
  - type: input
    id: repository
    attributes:
      label: Repository URL
    validations:
      required: true
  - type: input
    id: prior_issue
    attributes:
      label: Prior removal or maintenance issue
    validations:
      required: false
  - type: textarea
    id: changes
    attributes:
      label: What changed?
      description: Explain how required criteria and maintenance have been restored.
    validations:
      required: true
  - type: checkboxes
    id: restored_requirements
    attributes:
      label: Restored requirements
      options:
        - label: OSI-approved license is present.
          required: true
        - label: Code of Conduct is present.
          required: true
        - label: Maintainers are reachable.
          required: true
        - label: Repository is public and not archived.
          required: true
        - label: README/docs acknowledgement will be updated if reactivated.
          required: true
```

## .github/PULL_REQUEST_TEMPLATE.md

Create:

```markdown
## Summary

<!-- What changed and why? -->

## Type

- [ ] Documentation
- [ ] Issue template
- [ ] Workflow / automation
- [ ] Label script
- [ ] Maintenance / cleanup

## Checklist

- [ ] Markdown renders correctly.
- [ ] YAML is valid.
- [ ] Shell scripts pass `bash -n`.
- [ ] Python scripts pass `python -m py_compile`.
- [ ] Changes do not imply OSL guarantees funding, GSoC, or maintenance.
```

## scripts/create-labels.sh

Create executable script. It should work with either current repo or `-R`.

Suggested implementation:

```bash
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
```

After creating it:

```bash
chmod +x scripts/create-labels.sh
bash -n scripts/create-labels.sh
```

To run:

```bash
scripts/create-labels.sh OpenScienceLabs/affiliation-requests
```

## scripts/check-affiliated-projects.py

Create a first version of a health-check script. It does not need to be perfect;
it should be safe and report-only initially.

Recommended behavior:

- Read project entries from a YAML file if `data/affiliated-projects.yml` exists.
- Otherwise optionally fetch the website repo project list using GitHub API or
  skip with a clear message.
- For each project URL/repo:
  - check repository reachable through GitHub API when GitHub URL;
  - check archived status;
  - check default branch;
  - check `LICENSE` exists;
  - check `CODE_OF_CONDUCT.md`, `.github/CODE_OF_CONDUCT.md`, or docs variant;
  - check `README.md` exists;
  - check `SECURITY.md` exists and warn only;
  - check recent pushed date;
  - check homepage URL if provided;
  - check acknowledgement text if feasible.
- Output Markdown summary to stdout and optionally to `health-check-report.md`.
- Exit 0 by default so the first workflow is non-disruptive.
- Later, add issue creation/update behavior.

Suggested CLI:

```bash
python scripts/check-affiliated-projects.py \
  --repo OpenScienceLabs/affiliation-requests \
  --source data/affiliated-projects.yml \
  --max-inactive-days 180 \
  --output health-check-report.md
```

Example data file format if used:

```yaml
projects:
  - name: Example Project
    repository: https://github.com/example/project
    website: https://example.org
    maintainers:
      - github: maintainer1
    status: affiliated
```

Python dependencies: prefer standard library only for v1. If YAML is needed,
either use JSON instead or document PyYAML. Since GitHub Actions runners may not
have PyYAML, standard-library JSON is simpler. Alternative: use `data/projects.json`.

Recommendation: for v1, use JSON to avoid dependencies:

```text
data/affiliated-projects.json
```

## scripts/validate-issue-forms.py

Optional validation script using Python standard library is hard for YAML. If
PyYAML is available, validate issue forms. Otherwise, the workflow can simply
print files and rely on GitHub parsing.

Simpler option: do not create this initially unless adding PyYAML to the
workflow.

## .github/workflows/affiliation-intake.yml

Purpose: when a request issue opens, post an acknowledgement comment and ensure
labels are present.

Use `actions/github-script`.

Suggested:

```yaml
name: Affiliation intake

on:
  issues:
    types: [opened, edited, reopened]

permissions:
  issues: write
  contents: read

jobs:
  intake:
    runs-on: ubuntu-latest
    if: contains(github.event.issue.labels.*.name, 'type: affiliation-request')
    steps:
      - name: Add intake comment on new requests
        if: github.event.action == 'opened'
        uses: actions/github-script@v7
        with:
          script: |
            const issue = context.payload.issue;
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: issue.number,
              body: `Thanks for opening an OSL affiliation request.\n\nAn OSL reviewer will check the required evidence: OSI-approved license, Code of Conduct, maintainer contact, public repository, maintenance status, and alignment with OSL.\n\nReminder: affiliation does not guarantee GSoC participation, contributor slots, funding, interns, mentors, or promotion. If approved, please add the OSL affiliation acknowledgement to your README/docs.`
            });
            await github.rest.issues.addLabels({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: issue.number,
              labels: ['status: needs-triage']
            });
```

Potential issue: `contains(github.event.issue.labels.*.name, ...)` may be
supported in GitHub expressions, but if not, remove `if` and inspect labels in
script.

## .github/workflows/stale.yml

Use `actions/stale`.

Suggested:

```yaml
name: Stale issues

on:
  schedule:
    - cron: "0 9 * * 1"
  workflow_dispatch:

permissions:
  issues: write
  pull-requests: write

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          days-before-stale: 30
          days-before-close: 30
          only-labels: "status: needs-info"
          stale-issue-label: "status: paused"
          stale-issue-message: |
            This request has been waiting for maintainer/applicant information for about 30 days.

            Please provide the missing information so OSL can continue the review. If there is no response, the request may be closed as incomplete. You may apply again later.
          close-issue-message: |
            Closing this request as incomplete because OSL did not receive the requested information.

            You are welcome to open a new request after the missing information is available.
          exempt-issue-labels: "status: approved,status: declined,status: in-review"
```

## .github/workflows/link-check.yml

Use lychee or markdown-link-check. Example with lychee:

```yaml
name: Link check

on:
  pull_request:
  workflow_dispatch:
  schedule:
    - cron: "0 10 * * 1"

permissions:
  contents: read
  issues: write

jobs:
  link-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Link Checker
        uses: lycheeverse/lychee-action@v2
        with:
          args: --verbose --no-progress './**/*.md' './.github/**/*.yml'
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

If external actions are undesired, replace with a simple grep/report script.

## .github/workflows/health-check.yml

Create as report-only initially.

```yaml
name: Affiliated project health check

on:
  schedule:
    - cron: "0 8 1 */3 *" # quarterly
  workflow_dispatch:

permissions:
  contents: read
  issues: write

jobs:
  health-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - name: Run health check
        run: |
          python scripts/check-affiliated-projects.py --output health-check-report.md || true
      - name: Upload report
        uses: actions/upload-artifact@v4
        with:
          name: affiliation-health-check-report
          path: health-check-report.md
```

Later enhancement: create/update one tracking issue per project with failures.
Use `actions/github-script` or `gh issue create`.

## .github/workflows/label-check.yml

Purpose: remind maintainers to run label creation script if labels are missing.
This can be manual.

```yaml
name: Label check

on:
  workflow_dispatch:

permissions:
  issues: read

jobs:
  label-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check script syntax
        run: bash -n scripts/create-labels.sh
      - name: List labels
        env:
          GH_TOKEN: ${{ github.token }}
        run: gh label list --repo "${{ github.repository }}"
```

Do not auto-create labels from workflow unless comfortable giving write
permissions and using `GH_TOKEN` with `issues: write`.

## CONTRIBUTING.md

Create concise contribution instructions:

- how to update docs;
- how to edit issue templates;
- how to test shell scripts;
- how to test workflows lightly;
- PR expectations;
- reviewers should not approve policy changes that contradict the website.

## CODE_OF_CONDUCT.md

Option 1: copy OSL Code of Conduct if there is a canonical one.
Option 2: link to website Code of Conduct.

Best for this repo: include a short document that points to the canonical OSL
Code of Conduct:

```markdown
# Code of Conduct

This repository follows the Open Science Labs Code of Conduct:

https://opensciencelabs.org/about/coc/

By participating in issues, pull requests, reviews, and discussions in this
repository, you agree to follow it.
```

## SECURITY.md

Create:

```markdown
# Security Policy

This repository is for affiliation workflow documentation and automation. It is
not the security reporting channel for affiliated projects.

If you need to report a vulnerability in an affiliated project, use that
project's own security policy or maintainer contact path.

If you need to report a security issue in this repository's automation, please
contact Open Science Labs at team@opensciencelabs.org or use GitHub private
vulnerability reporting if enabled.
```

## Implementation Steps for Future Codex Session

1. Open a session rooted at:

   ```text
   /mnt/HC_Volume_102749953/dev/osl-projects/opensciencelabs/affiliation-requests
   ```

2. Check repo state:

   ```bash
   git status --short
   git remote -v
   ```

3. Create directories:

   ```bash
   mkdir -p .github/ISSUE_TEMPLATE .github/workflows docs scripts
   ```

4. Create/update files described above.

5. Make scripts executable:

   ```bash
   chmod +x scripts/create-labels.sh scripts/check-affiliated-projects.py || true
   ```

6. Validate:

   ```bash
   bash -n scripts/create-labels.sh
   python -m py_compile scripts/check-affiliated-projects.py
   find .github -name '*.yml' -o -name '*.yaml' -print
   git diff --check
   ```

   If `yamllint` is available:

   ```bash
   yamllint .github docs || true
   ```

7. Review generated docs and templates.

8. Commit changes:

   ```bash
   git add .
   git commit -m "Prepare affiliation request workflow"
   ```

9. Create labels after repo permissions are available:

   ```bash
   scripts/create-labels.sh OpenScienceLabs/affiliation-requests
   ```

## Important Design Principle

Keep the website and this repo complementary:

| Topic | Website | This repo |
| --- | --- | --- |
| What affiliation means | Public summary | Detailed operational docs |
| Requirements | Public checklist | Evidence-based issue form |
| Boundaries | Public policy | Review checklist + required acknowledgement |
| GSoC disclaimer | Public statement | Required applicant confirmation |
| Maintenance reviews | Policy/timeline | Issues, labels, bots |
| Removal/reactivation | Policy summary | Issue templates and records |
| Bot checks | High-level description | Workflows and scripts |

## Current Website Changes Already Made

The current session already updated the website repo with relevant affiliation
and incubation policy language. Do not duplicate the entire website content in
this repo; instead, link to it and keep operational details here.

Website pages changed in the current session:

```text
pages/projects/index.md
pages/projects/affiliation/index.md
pages/projects/incubation/index.md
pages/projects/list/index.md
```

Build validation passed in the website repo:

```bash
python -m mkdocs build --strict
```

## Possible Follow-up After This Repo Is Prepared

- Update the website affiliation page to mention the issue template by name if
  needed.
- Add a link from website to `docs/criteria.md` once published.
- Add a bot that opens a PR against `opensciencelabs.github.io` when an
  affiliation request is approved. This requires cross-repo token permissions
  and should be designed carefully.
- Add a `data/affiliated-projects.json` mirror if the request repo becomes the
  operational source of truth.
- Add periodic reports summarizing approved, at-risk, removed, and reactivated
  projects.
