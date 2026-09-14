# Lightweight feature specifications

Status on 2026-09-14: **setup only; all feature specs are drafts**.
Application coding is planned for 2026-09-15 and still requires an explicit start
instruction. Do not start automatically based on the date or a skill trigger.

This is a small spec-driven workflow, not a Spec Kit installation. No generated
commands, additional framework, code scaffolding or app dependencies are added.

## Workflow

1. Use [the template](_template.md) for a bounded feature.
2. Review intended behavior, failure cases and exclusions with the owner.
3. Record spec approval and unresolved decisions. Approval must be real, not
   inferred from creation of a file or approval of repository setup.
4. When asked, write a short `plan.md` alongside the approved spec, mapping
   requirement IDs to tasks and planned tests.
5. Only after explicit implementation authorization: failing test, change,
   targeted verification, review and frequent commits/pushes on a feature branch.
6. In PRs, link requirement IDs to actual test evidence and disclose gaps.

Spec approval, implementation authorization and deployment approval are separate.
Existing AGENTS.md and docs/architecture.md govern shared constraints; do not
duplicate them into a competing project constitution.

## Drafts prepared for tomorrow's discussion

| Feature | Requirements | Proposed issue |
| --- | --- | --- |
| [Egress gateway](egress-gateway/spec.md) | EG-01 through EG-06 | #3 |
| [Coding and evidence](coding-evidence/spec.md) | CE-01 through CE-06 | #4 |
| [Offline mode](offline-mode/spec.md) | OF-01 through OF-05 | #5 |

No acceptance criterion in these documents is currently marked implemented or
verified. The foundation checks are not feature acceptance tests.
