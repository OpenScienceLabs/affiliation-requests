# Contributing

Thanks for helping maintain the OSL affiliation workflow.

## What belongs here

This repository contains operational material for project affiliation requests:
issue templates, review guidance, labels, workflow documentation, and supporting
automation. Public policy language should remain aligned with the OSL website.

## Updating documentation

- Keep documentation concise, evidence-based, and kind.
- Do not add language that implies OSL ownership, certification, guaranteed
  maintenance, guaranteed funding, or guaranteed GSoC participation.
- Link to the public OSL website for policy summaries when possible.
- If changing criteria, check that the change does not contradict the website.

## Editing issue templates

Issue forms live in `.github/ISSUE_TEMPLATE/`.

When editing them:

- keep required eligibility questions required;
- keep the GSoC/funding disclaimer visible;
- keep acknowledgement and independence confirmations;
- validate YAML before merging; and
- open a test issue in a fork or temporary branch when practical.

## Editing workflows and scripts

Before opening a pull request, run the relevant checks locally:

```bash
bash -n scripts/create-labels.sh
python -m py_compile scripts/check-affiliated-projects.py
git diff --check
```

If you add Python dependencies, document them and update the workflows. Prefer
standard-library Python for repository automation unless a dependency is clearly
worth the maintenance cost.

## Pull request expectations

Use the pull request template and include:

- a short summary of the change;
- the type of change;
- validation performed; and
- any policy implications.

Reviewers should not approve changes that weaken baseline requirements or imply
OSL guarantees ownership, governance, funding, contributors, mentors,
certification, security, scientific quality, or maintenance.
