---
name: superpowers-writing-plans
description: Plan multi-step feature work from an approved specification before implementation; stop at planning when the user requests setup only.
---

# Planning: project-adapted Superpowers

Derived from `obra/superpowers` at
`b36e0829c6d0140e93cfef2ca599b1b07d4a7797`,
`skills/writing-plans/SKILL.md`. Copyright (c) 2025 Jesse Vincent.
MIT license and adaptations: `third_party/superpowers/`.

Read AGENTS.md, specs/README.md and the feature spec. Check the current phase and
approval state first. An approved plan is not permission to execute it.

For an approved feature, create `specs/<feature>/plan.md` when requested:

1. State the goal, spec path, exclusions, constraints and implementation approval.
2. Map each requirement ID to a small independently testable task.
3. Name intended file responsibilities and interfaces. Mark proposed paths as
   proposed; do not imply modules already exist.
4. For each task, specify the observable test, expected initial failure,
   minimal implementation scope and targeted verification command.
5. Include relevant error paths, privacy effects, catalog/version handling and
   documentation changes. Do not add unrequested generalization.
6. Identify unresolved design decisions as blockers, not guessed approvals.
7. Self-review requirement coverage, interface consistency and dependencies.

Keep plans concise; do not write a second implementation in a document.
No automatic worktrees, subagents or executable-code generation. Do not invoke
upstream plugin skills that are not installed. Once implementation is explicitly
authorized, execute small coherent slices with review and frequent commits.
During setup-only work, stop after the planning document.
