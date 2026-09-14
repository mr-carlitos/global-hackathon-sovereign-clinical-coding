# Contributing

This repository is private during the hackathon. It is intended for later public
release, but no open-source license has been selected yet.

Read `AGENTS.md`, `docs/plan.md`, and the privacy/catalog policies before work.
Carlos coordinates Azure and integration; the software engineer and solution-sales
specialist own the parallel work described in the plan. GitHub handles for the
two collaborators must be confirmed before invitations or review assignments.

## Development workflow

1. Take a small issue with acceptance criteria and a named owner.
2. Create a short-lived feature branch; keep changes scoped.
3. Run the foundation checks and the targeted tests for the component you change.
4. Commit and push frequently at coherent milestones.
5. Open a PR, inspect CI logs/artifacts directly, and request human review.

No real clinical records, copied proprietary catalog content, credentials or
developer-specific tenant configuration. Preserve original source attribution.
Do not auto-merge someone else's changes or force-push shared branches.

## Public-release checklist

- Owner approves visibility and a source-code license.
- Contributors confirm rights to their contributions; dependency/model licenses
  and third-party notices are reviewed.
- Audit Git history, fixtures, artifacts, images and screenshots for secrets,
  personal data and restricted catalog content.
- Rehearse a clean-clone setup and documented teardown.
- Publish actual evaluation results, supported versions, limitations and threat
  model; remove unsupported legal, privacy and clinical claims.
- Set a responsible disclosure contact and support expectations.
- Verify GitHub permissions, branch protection, CI and cost controls.
- Remove internal tenant/project identifiers and stale demo endpoints.

Do not upload sensitive vulnerability details or patient examples to issues.
Contact the repository owner privately for security concerns.
