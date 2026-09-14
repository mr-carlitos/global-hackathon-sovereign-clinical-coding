# Agent-assisted development

## Selected setup

Use canonical `AGENTS.md`, Copilot instructions, the three domain/CI skills,
a lightweight spec-first skill and four project-adapted Superpowers skills.
The owner approved this setup on 2026-09-14, with application coding explicitly
paused until a later start instruction. The planned coding date is 2026-09-15.

| Repo-local skill | When to use |
| --- | --- |
| `spec-first` | Define observable behavior, exclusions, failure cases and approval status |
| `superpowers-writing-plans` | Break an approved spec into small implementation/test tasks |
| `superpowers-test-driven-development` | Write a failing behavior test before authorized implementation |
| `superpowers-systematic-debugging` | Reproduce and investigate failures before changing code |
| `superpowers-verification-before-completion` | Collect evidence for the exact completion claim |

The four adapted skills are based on a fixed Superpowers commit, not a moving
marketplace installation. Attribution, license, reviewed source paths and changes
are recorded in [the provenance record](../third_party/superpowers/README.md).
No global/user-level installation, session hooks, telemetry, automatic updates,
additional MCP servers or subagent orchestrator are enabled.

We intentionally adapted rather than copied the full upstream workflows:
boundary diagnostics must never dump patient content/secrets; TDD must not delete
existing work; planning must not automatically dispatch agents or begin execution.
Our short feature specs replace the need for a second full workflow framework.
**Spec Kit is not installed.** This is lightweight spec-driven development, not a
claim to implement Spec Kit's tooling or generated commands.

Read [the specification workflow](../specs/README.md). Three draft feature specs
are ready for discussion, not implementation approval. Existing architecture and
catalog docs remain authoritative for project-wide constraints.

## What is configured

- Repository instructions and focused skills checked into Git.
- Offline GitHub Actions foundation checks, with downloadable logs.
- Copilot cloud-agent setup workflow prepares Python and runs the same checks.
- Dependabot monitors GitHub Actions references.
- PR template records boundary changes, catalog sources and verification.
- Versioned adapted SDLC skills, provenance and a spec template.

## Skill discovery and team onboarding

These skills are plain repository files under `.github/skills/`, available with
a normal clone; there is no separate dependency installation. Start a fresh
Copilot session on this branch (or on main after the setup PR is merged) and
check `/skills` and `/instructions`. Existing sessions may retain their original
skill list. Do not claim a skill was invoked merely because its file exists.

If the client does not discover repository skills, read the named `SKILL.md`
directly through its file tools and follow it as project guidance; report the
discovery limitation. Do not invent plugin-prefixed commands. Azure MCP and
browser availability are configured separately and are not changed by these files.

The setup PR is reviewed and merged by the owner; agents must not auto-merge it.
The setup files do not modify account-wide Copilot configuration or install
anything for other users of this machine.

## Tool access and separation

| Tool | Intended use | Boundary |
| --- | --- | --- |
| `gh` CLI | Issues, branches, PRs, CI logs/artifacts, workflow dispatch | Current authenticated user; no secrets in output |
| GitHub MCP | Read/search code and project context | Available tools here do not replace `gh` for all write/run operations |
| Azure CLI + Azure MCP | Inspect quota/resources, scoped deployment, metrics | Explicit subscription and approved project scope |
| Microsoft Learn MCP | Primary product docs and code samples | No patient data in search queries |
| Context7 | Library API documentation | Public library questions only; verify package identity |
| Playwright MCP | Interactive UI debugging, snapshots, console/network inspection | Synthetic demo app only; no signed-in personal browser session |
| Playwright test runner (planned) | Repeatable UI tests and CI trace artifacts | Distinct from MCP; pin packages/browser versions when UI exists |
| Chrome DevTools MCP (optional) | Performance/network investigation | Do not add a second browser tool unless needed |

No need for Fabric, WorkIQ, broad tenant-admin MCP, or external observability
services for this workload. Tools visible in this CLI are **not automatically
available to GitHub's cloud agent**. Configure its MCP allowlist separately in
repository settings after reviewing each server and credential scope.
Do not check local credential-bearing MCP configuration into the repo.

The repository does not yet install third-party MCP servers, enable cloud-agent
repository access, grant Azure rights, or configure browser dependencies.
These are explicit setup tasks, not inferred from the workflow file's existence.

## Autonomous iteration

```sh
gh issue list --limit 10
gh run list --limit 5
gh run view RUN_ID --json status,conclusion,jobs
gh run view RUN_ID --log-failed
gh run download RUN_ID --dir artifacts/RUN_ID
```

Agents inspect logs directly, reproduce the failure, make the smallest complete
fix, and push a coherent commit. Never rerun a failing live test until green
without explaining intermittent failures. Downloaded artifacts are ignored.
Use issues with acceptance criteria and PRs linked to those issues.

For the future UI: start its server, verify readiness, run Playwright, retain
traces/screenshots on failure, and inspect console/network failures directly.
Neither browser traces nor cloud logs may contain real patient data.

## Permission model

Autonomy covers edits, tests, commits, pushes to feature branches and diagnosis
of CI failures. The owner approves merges, infrastructure scope, role assignments,
destructive actions and public release. Do not disable approvals globally.
Cloud-agent availability, protected branches and required environment reviewers
depend on account/repository capabilities; verify rather than claim enabled.
