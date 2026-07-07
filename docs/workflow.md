# Affiliation Review Workflow

This workflow keeps affiliation decisions transparent, evidence-based, and
consistent.

## Request workflow

1. Maintainer opens an affiliation request issue.
2. Bot labels the issue with `type: affiliation-request` and
   `status: needs-triage`.
3. Bot checks required fields when possible.
4. Reviewer performs a completeness check.
5. Reviewer requests missing information with `status: needs-info` if needed.
6. Maintainer updates the issue.
7. Reviewer performs eligibility review.
8. OSL may allow a public/community comment period when useful.
9. Reviewer records a decision:
   - approved;
   - needs changes; or
   - declined.
10. If approved:
    - add `status: approved` and `decision: accepted`;
    - open or update the website pull request to add the project listing;
    - confirm the README/docs acknowledgement requirement;
    - optionally create an onboarding checklist; and
    - schedule the project for periodic maintenance checks.

## Decision states

Use status labels consistently:

- `status: needs-triage` — needs first review.
- `status: needs-info` — waiting for applicant or maintainer information.
- `status: in-review` — under OSL review.
- `status: approved` — approved for affiliation.
- `status: declined` — declined at this time.
- `status: paused` — paused pending changes or maintainer response.
- `status: at-risk` — may lose affiliation if unresolved.
- `status: removed` — removed from the public affiliation list.
- `status: reactivated` — affiliation restored.

## Completeness check

Before judging eligibility, verify that the request includes links or evidence
for:

- repository;
- license;
- Code of Conduct;
- maintainer contact path;
- public collaboration or communication path;
- maintenance status;
- OSL mission alignment;
- collaboration requested through OSL;
- program readiness, if applicable; and
- acknowledgement and independence confirmations.

If required evidence is missing, ask for the specific missing links and apply
`status: needs-info`.

## Eligibility review

Reviewers should evaluate whether the project meets baseline criteria and
whether affiliation would be clear, safe, and non-misleading. Reviewers should
ask for evidence rather than relying only on claims.

Do not approve a request when the project lacks an OSI-approved license, lacks a
Code of Conduct with a reporting path, has no reachable maintainer, or would use
affiliation to imply ownership, certification, funding, or maintenance by OSL.

## After approval

After approval, confirm that the project:

- understands that it remains independently governed and maintained;
- adds the OSL acknowledgement to README/docs;
- knows GSoC, internships, funding, grants, mentors, contributors, and promotion
  are not guaranteed; and
- has a path for future maintenance review communication.

The public project listing may remain on the OSL website. This repository keeps
the operational record.
