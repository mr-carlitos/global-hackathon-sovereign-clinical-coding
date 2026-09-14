---
name: superpowers-verification-before-completion
description: Before declaring work complete or pushing a milestone, verify the exact claim with current commands and inspect the evidence.
---

# Verification: project-adapted Superpowers

Derived from `obra/superpowers` at
`b36e0829c6d0140e93cfef2ca599b1b07d4a7797`,
`skills/verification-before-completion/SKILL.md`. Copyright (c) 2025 Jesse Vincent.
MIT license and adaptations: `third_party/superpowers/`.

Read AGENTS.md. Verification cannot authorize implementation or deployment.

Before a completion claim:

1. Identify the requirement and the command or observation that proves it.
2. Run the smallest complete check for that claim against the current changes.
3. Read its output, exit status and failures; do not infer success from silence.
4. Compare with each claimed acceptance criterion. Record unmet/untested items.
5. Commit/push only the intended changes; inspect the relevant CI run afterward.
6. State the actual result and limitations. Pending workflows are not passing.

Match evidence to the claim:

- Unit tests do not prove live Azure behavior.
- A schema-valid pack does not grant licensing or privacy approval.
- A signed audit chain does not prove no identifiers leaked.
- A committed skill file does not prove client discovery or invocation.
- A pushed branch/PR is not a merged change.
- A startup message is not a responsive service.

Use existing repository checks for setup; review skill frontmatter, references,
provenance and scope. Do not create application code just to demonstrate a tool.
Do not rerun unrelated full suites when targeted evidence answers the claim.
Retrieve logs and artifacts directly, keeping all evidence synthetic and sanitized.
