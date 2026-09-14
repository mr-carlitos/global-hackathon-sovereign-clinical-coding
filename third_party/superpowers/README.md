# Superpowers provenance and integration

Source: https://github.com/obra/superpowers

Reviewed revision: `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`

Review/adaptation date: 2026-09-14.
Copyright (c) 2025 Jesse Vincent. Upstream [MIT license](LICENSE) is retained.

## What is included

Four **project-adapted derivatives**, not byte-for-byte upstream copies:

| Upstream source at the pinned revision | Repository skill |
| --- | --- |
| `skills/writing-plans/SKILL.md` | [Planning](../../.github/skills/superpowers-writing-plans/SKILL.md) |
| `skills/test-driven-development/SKILL.md` | [TDD](../../.github/skills/superpowers-test-driven-development/SKILL.md) |
| `skills/systematic-debugging/SKILL.md` | [Debugging](../../.github/skills/superpowers-systematic-debugging/SKILL.md) |
| `skills/verification-before-completion/SKILL.md` | [Verification](../../.github/skills/superpowers-verification-before-completion/SKILL.md) |

The reviewed source snapshot is reachable using:
`https://github.com/obra/superpowers/blob/b36e0829c6d0140e93cfef2ca599b1b07d4a7797/<upstream-source-path>`.
No upstream scripts, examples, supporting files, plugin bootstrap, hooks or
runtime dependencies are required by our self-contained adaptations.

## Deliberate changes

- Prefixed names prevent confusion with a separately installed upstream plugin.
- Shortened the workflows and made referenced guidance self-contained.
- Removed automatic subagent/worktree/execution handoffs and full-code-in-plan
  requirements. A setup-only instruction always stops implementation.
- Replaced blanket code-deletion guidance with preserving existing/user work and
  a scoped test-first or characterization-test workflow.
- Replaced payload/environment logging examples with allowlisted diagnostic
  metadata. No note, identity, credential or full environment dumps.
- Kept root-cause investigation, red/green/refactor and evidence-before-claims.
- Distinguished targeted evidence from full-system proof. No repeated full-suite
  execution for unrelated documentation claims.
- Retained explicit approval boundaries for merges, deployments and scope changes.

These adapted skill files and their modifications are distributed under the
included MIT terms. That third-party license does **not** select a license for
the rest of this repository, clinical catalogs or model weights.

## Update procedure

No automatic upstream updates. In a dedicated setup PR:

1. Select an immutable upstream commit and compare these four source files.
2. Review instructions, dependencies, hooks, data handling and license changes.
3. Adapt only intentional changes; preserve repository safety and user approvals.
4. Update this record and any affected skill references together.
5. Check frontmatter, referenced files, documentation links and CI.
6. Ask the owner to review the PR before merging.

We have reviewed the selected text for integration suitability; this is not an
independent audit or a guarantee about future upstream releases.
