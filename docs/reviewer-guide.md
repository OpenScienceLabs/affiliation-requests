# Reviewer Guide

Reviewers represent OSL's values during affiliation reviews. Be transparent,
kind, specific, and evidence-based.

## Review principles

- Ask for links and evidence, not only claims.
- Explain missing requirements clearly.
- Do not approve if the license or Code of Conduct is missing.
- Do not approve if maintainers are unreachable.
- Do not imply funding, GSoC participation, internships, grants, mentors,
  contributors, promotion, maintenance, certification, or endorsement.
- Make affiliation boundaries explicit.
- If unsure, mark `status: needs-info` or ask another reviewer.
- Use labels consistently.
- Leave a decision comment when approving or declining.

## Suggested completeness response

```markdown
Thanks for your request. Before OSL can continue the review, please add links or
evidence for:

- ...

After updating the issue, please leave a comment so reviewers know it is ready
for another look.
```

## Suggested approval comment

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

## Suggested declined comment

```markdown
Thanks for your request. OSL cannot approve affiliation at this time because:

- ...

You are welcome to apply again after addressing these points.
```

## Suggested at-risk maintenance comment

```markdown
OSL is reviewing this affiliated project because one or more baseline
requirements may need attention:

- ...

Please respond with updated links or context. If OSL cannot confirm the baseline
requirements after the review period, affiliation may be paused or removed from
public lists. Removal is not permanent; projects may request reactivation after
restoring the requirements.
```

## Label use

Use type, status, check, priority, decision, and bot labels as documented in
[labels.md](labels.md). Avoid conflicting status labels where possible; for
example, remove `status: needs-triage` when applying `status: in-review` or
`status: approved`.
