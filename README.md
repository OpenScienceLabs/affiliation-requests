# OSL Affiliation Requests

This repository is the operational home for requesting project affiliation with
[Open Science Labs (OSL)](https://opensciencelabs.org/).

It hosts public affiliation requests, review records, maintenance reviews,
removal/reactivation discussions, issue templates, labels, and automation used by
OSL reviewers. The OSL website remains the public policy and orientation layer;
this repository records the evidence-based workflow.

## What affiliation means

OSL affiliation is a lightweight relationship between OSL and an independently
maintained project. It means the project aligns with OSL's mission and is
connected to the OSL ecosystem.

Affiliation does **not** mean that OSL owns, governs, maintains, certifies,
funds, or controls the project. The project's maintainers remain responsible for
its governance, roadmap, releases, code, data, intellectual property, community,
and support obligations.

## Who should apply

Affiliation is intended for existing projects that:

- have an open-source, open-science, research, education, public-interest, or
  open-technology purpose;
- have at least one active or reachable maintainer;
- are public and usable by the community; and
- are ready to maintain baseline contributor-safety and openness requirements.

## Before applying

Please confirm that the project has:

- an OSI-approved open-source license;
- a public `LICENSE` file;
- a `CODE_OF_CONDUCT.md` or equivalent public Code of Conduct with a reporting
  path;
- at least one active or reachable maintainer;
- a public repository;
- a public issue tracker, discussion channel, project board, or documented
  contact path; and
- no current archived, closed-source, abandoned, misleading, hostile, or unsafe
  status that would make affiliation inappropriate.

Recommended supporting materials include `CONTRIBUTING.md`, user/developer docs,
project ideas or starter issues, a security reporting path where relevant, and a
clear statement of the collaboration the project seeks through OSL.

See [docs/criteria.md](docs/criteria.md) for the detailed criteria.

## How to request affiliation

Open a new issue using the **Affiliation request** form. The form asks for links
to evidence such as the repository, license, Code of Conduct, maintainer contact
path, maintenance status, and alignment with OSL.

Requests that are missing required evidence may be marked `status: needs-info`
until the applicant updates the issue.

## Review workflow

A typical review follows this path:

1. A maintainer opens an affiliation request issue.
2. Automation applies `type: affiliation-request` and `status: needs-triage`.
3. A reviewer checks completeness and requests missing information if needed.
4. A reviewer evaluates eligibility, alignment, and maintainer readiness.
5. OSL may allow public/community comment where useful.
6. A reviewer records a decision: approved, declined, or needs changes.
7. If approved, OSL coordinates public listing updates and onboarding follow-up.
8. Periodic maintenance reviews continue after listing.

See [docs/workflow.md](docs/workflow.md) and
[docs/reviewer-guide.md](docs/reviewer-guide.md) for details.

## GSoC and limited programs

Affiliated projects may submit ideas for Google Summer of Code, internships,
grants, or similar programs only when OSL is participating and the project is
ready. OSL will do its best to participate in GSoC where possible.

Participation is never guaranteed. It depends on external selection, OSL
capacity, mentor availability, project readiness, and limited slots. Even when
OSL participates, not every affiliated project idea can be selected or funded.

## Acknowledgement requirement

Accepted projects should acknowledge affiliation in their README and public docs
where applicable. Suggested wording:

```markdown
## Open Science Labs Affiliation

This project is affiliated with Open Science Labs (OSL). Affiliation means that
the project aligns with OSL's mission and is connected to the OSL ecosystem,
while governance, roadmap, maintenance, and releases remain the responsibility
of the project maintainers.
```

Projects should remove or update this text if affiliation is paused, removed, or
changed. See [docs/acknowledgement.md](docs/acknowledgement.md).

## Maintenance reviews

OSL may review affiliated projects periodically or when concerns are reported.
Projects may be marked at risk, paused, removed from public lists, or reactivated
after restoring baseline requirements.

Common review triggers include missing license or Code of Conduct information,
broken links, unreachable maintainers, unsafe community behavior, misleading use
of OSL branding, closed-source changes, or long-term inactivity without a stable
maintenance note.

## Useful links

- [Open Science Labs website](https://opensciencelabs.org/)
- [OSL project affiliation policy](https://opensciencelabs.org/projects/affiliation/)
- [OSL project list](https://opensciencelabs.org/projects/list/)
- [OSL Discord](https://opensciencelabs.org/discord)
- [OSL Code of Conduct](https://opensciencelabs.org/about/coc/)
