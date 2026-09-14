# Azure access and operations plan

**No Azure resources or identities have been created for this project yet.**
Azure CLI is installed and authenticated on the development machine. The active
subscription has not been approved as this project's deployment target.
Tenant/subscription identifiers stay in local deployment configuration, not in
this public-intended documentation.

## Identity design

Do not give the agent a new human account, tenant admin, or subscription Owner.

- Interactive development: approved developer identity with project-scoped rights.
- CI deployment: dedicated Entra workload identity with GitHub OIDC federation;
  no stored client secret. Trust this repository and the intended deployment
  environment, not arbitrary branches or pull requests.
- Runtime: separate managed identities for cloud API, catalog ingestion and
  other components, with only the data-plane permissions each needs.
- Role creation: owner/admin bootstraps resource-group scope and assignments.
  Do not grant the deployment identity authority to assign itself broader roles.

Federated subject formats can vary with repository creation date and GitHub
configuration. Verify the actual expected subject and audience from current
GitHub/Azure guidance; do not paste a legacy `repo:owner/name` template blindly.
See [OIDC guidance](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure).

## Before provisioning

Confirm the specific subscription and tenant, project resource group(s), region,
model deployment type/version/quota, VM image/runtime compatibility and SKU.
Provide an estimate even though this is short-lived: VM disks, Search, logs and
networking may continue charging after a VM is stopped. One hospital VM preferred,
two only if necessary. No HA or large cluster.

Tag every resource with project, owner and expiry date. Review a Bicep `what-if`
before applying. Get separate approval for generating deployment infrastructure
and for provisioning it. Initial docs/CI bootstrap grants neither.

Deployment workflow (to implement): manual dispatch, approved GitHub environment,
least-privilege OIDC, explicit parameters, bounded timeout, health checks and
sanitized outputs. No Azure credentials in untrusted pull-request workflows.
If private-repo environment protection is unavailable on the account's plan,
keep deployment an explicitly approved CLI operation instead.

## Live evaluation and observability

Deterministic CI stays offline. Live inference tests require a separately approved
environment and synthetic-only fixtures. Emit request counts, timings, decision
codes and opaque run IDs; disable request/response logging. Use `gh` for workflow
logs and Azure tools for scoped resource diagnostics. No patient-bearing traces.

## Teardown

After the hackathon, first list resources by explicit project group and ownership
tags. Confirm the inventory with the owner; delete only approved project groups,
then verify deletion. Do not automate broad subscription cleanup.

Also remove demo-specific federated credentials/RBAC, secrets, private DNS
artifacts outside those groups, retained logs, registry images and public demo
endpoints where applicable. Verify that nothing chargeable was left behind.
Stopping/deallocating VMs alone is not teardown.

A concrete executable deployment/cleanup runbook will be generated alongside
approved infrastructure, using actual resource names rather than invented IDs.
