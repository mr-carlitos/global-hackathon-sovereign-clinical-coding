---
name: superpowers-systematic-debugging
description: Investigate a reproducible root cause for test, build, integration or runtime failures before attempting fixes.
---

# Debugging: project-adapted Superpowers

Derived from `obra/superpowers` at
`b36e0829c6d0140e93cfef2ca599b1b07d4a7797`,
`skills/systematic-debugging/SKILL.md`. Copyright (c) 2025 Jesse Vincent.
MIT license and adaptations: `third_party/superpowers/`.

Read AGENTS.md. During setup-only work, investigate/fix setup failures only;
application implementation and Azure changes remain paused.

## Investigate

Read complete relevant errors; retrieve CI logs/artifacts directly. Reproduce
with the actual command and inspect recent changes. For intermittent failures,
gather evidence rather than repeatedly rerunning until green.

Trace the failing value backward from the boundary to its origin. Compare with
working paths, configuration and documented interfaces. Inspect one continuous
trace directly instead of delegating fragments without context.

Diagnostics may contain only allowlisted metadata: stage, sanitized error code,
opaque run ID and timing. Never dump payloads, notes, identity, tokens, secrets,
full environments or request/response bodies. Review output before publishing.

## Test a hypothesis

State one hypothesis and the evidence supporting it. Make one bounded diagnostic
change and test. If disproved, revise the hypothesis; do not stack speculative
patches. Prefer condition-based waits with explicit timeouts over arbitrary sleeps.

## Fix and verify

When the fix is in scope, reproduce the defect in a test, fix its origin, then
check the original symptom and affected regressions. Do not weaken assertions,
change unrelated code or silently add cloud fallbacks.

After three unsuccessful candidate fixes, stop and reassess assumptions with
the owner. If an external limitation is proven, report it and preserve evidence;
do not invent a root cause or claim successful recovery.
