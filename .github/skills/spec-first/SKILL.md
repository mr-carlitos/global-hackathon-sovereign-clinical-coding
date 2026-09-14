---
name: spec-first
description: Define or clarify feature behavior, acceptance criteria and failure cases before planning or implementing clinical-coding accelerator features.
---

# Lightweight specification workflow

Read AGENTS.md, specs/README.md and the relevant architecture/privacy/catalog docs.
Use specs/_template.md. Existing drafts are proposals, not implementation approval.

1. Describe the user outcome and explicit non-goals.
2. Define inputs/outputs in behavioral terms, including privacy boundaries.
3. Assign stable requirement IDs and observable acceptance criteria.
4. Include success, malformed input, dependencies failing, retries and offline
   behavior where relevant. Specify what must not happen.
5. Link each requirement to planned evidence, not fabricated test results.
6. Identify decisions that require owner review and keep the spec draft until
   approval is explicitly recorded.

Reuse existing project constraints; avoid a competing constitution or duplicative
architecture. Keep each feature spec short enough for all three teammates to review.
Hand approved specs to superpowers-writing-plans only when planning is requested.
Do not start implementation until the owner explicitly authorizes it.
