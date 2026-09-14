# Agent-assisted development

## Recommendation

Start small: canonical `AGENTS.md`, Copilot instructions, and three focused
repository skills for pack changes, CI triage and the boundary workflow.
Use test-first implementation, small PRs, direct log retrieval and human review.
GitHub supports project skills in `.github/skills/`; see [research](research.md).

Superpowers is a useful optional workflow library, and its upstream currently
documents Copilot support. Do not install it wholesale for this three-day project:
our short instructions and domain-specific skills are easier to review and less
likely to compete with existing Azure skills. Reconsider after the demo; pin a
reviewed revision, inspect hooks/commands and keep permissions narrow.
This is a project recommendation, not a claim of comparative benchmark results.

## What is configured

- Repository instructions and focused skills checked into Git.
- Offline GitHub Actions foundation checks, with downloadable logs.
- Copilot cloud-agent setup workflow prepares Python and runs the same checks.
- Dependabot monitors GitHub Actions references.
- PR template records boundary changes, catalog sources and verification.

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
