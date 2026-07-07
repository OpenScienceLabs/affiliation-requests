# Bot Workflows

Automation in this repository supports human review. Bots should surface useful
signals, apply routine labels, and reduce manual work. Bots must not replace
human judgement for affiliation approval, removal, or reactivation.

## Intake bot

Triggered when an issue is opened, edited, or reopened.

Responsibilities:

- detect affiliation request issues;
- apply `type: affiliation-request` and `status: needs-triage` when needed;
- post an acknowledgement comment on new requests;
- warn if required sections are obviously empty; and
- optionally apply `status: needs-info` when required links are missing.

## Health-check bot

Runs quarterly and through manual dispatch.

Checks may include:

- repository reachable;
- repository public;
- repository not archived;
- license file exists;
- Code of Conduct exists;
- README exists;
- optional `CONTRIBUTING.md` exists;
- optional `SECURITY.md` exists;
- last push date;
- issue or pull-request activity;
- listed URL works; and
- maintainer/user exists where detectable.

Outputs:

- Markdown summary in workflow logs;
- optional `health-check-report.md` artifact;
- future maintenance review issues for failures; and
- labels such as `status: at-risk` or `check: license` when a human review is
  needed.

The bot should never remove affiliation without human review.

## Stale/needs-info bot

For request issues:

- after about 30 days waiting on applicant information, comment and keep or apply
  `status: needs-info`/`status: paused`;
- after about 60 days waiting on applicant information, close as incomplete or
  keep paused; and
- allow applicants to reopen or reapply later.

For maintenance reviews:

- Day 0: issue opened and maintainers pinged;
- Day 30: mark at risk if there is no response;
- Day 60: open removal review if baseline requirements remain unresolved; and
- Day 90: a human may remove the project from the public list.

## Link-check bot

Runs weekly, manually, and on pull requests. It checks links in Markdown files
and issue templates. Link failures should be reviewed before making policy or
listing changes.

## Label check

The label check workflow is manual. It verifies that the label creation script is
syntactically valid and lists current repository labels. Label creation is done
with `scripts/create-labels.sh` by a maintainer with appropriate permissions.
