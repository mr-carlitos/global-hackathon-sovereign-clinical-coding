---
name: superpowers-test-driven-development
description: Use for explicitly authorized application features, bug fixes or behavior changes; write and observe a failing test before implementation.
---

# TDD: project-adapted Superpowers

Derived from `obra/superpowers` at
`b36e0829c6d0140e93cfef2ca599b1b07d4a7797`,
`skills/test-driven-development/SKILL.md`. Copyright (c) 2025 Jesse Vincent.
MIT license and adaptations: `third_party/superpowers/`.

Read AGENTS.md and the approved feature spec. If implementation is paused, do not
write application code or feature tests: this skill grants no execution approval.

For authorized behavior changes:

1. Name the requirement and the production defect/change the test should detect.
2. Write the smallest test of observable behavior, using synthetic fixtures.
3. Run it and confirm the intended failing assertion. Import errors, typos and
   missing dependencies are not evidence that the behavioral assertion works.
4. Implement the smallest complete change that satisfies the requirement.
5. Rerun the test and relevant existing tests. Inspect the actual output.
6. Refactor only after green; rerun affected checks and commit a coherent slice.

Tests should assert public behavior, not the mock's configuration. Use bounded
test doubles at external/cloud boundaries so offline CI never sends real data.
For fail-closed requirements, assert zero transport calls including retries,
not only an error response. Include malformed inputs and failure paths.

Never delete existing, committed or user-written code to enforce TDD.
For pre-existing untested behavior, add characterization tests before changing
it. If new code preceded its test, disclose the deviation and demonstrate the
regression test detects the defect without destructive history/worktree changes.

Documentation/configuration-only setup uses applicable structural checks rather
than fabricated application tests. A passing mock test does not prove live model,
network isolation, privacy or clinical accuracy.
