# Explicit disconnected operation

Status: Draft
Spec approval: Not granted
Implementation authorization: Not granted
Proposed owner / issue: Shared, #5

## Outcome and scope

A disconnected hospital can use preloaded local capabilities when supported,
with unmistakable degraded status and no hidden cloud dependency.
Follow docs/architecture.md and docs/privacy.md.

Non-goals: equivalent frontier-model quality, automatic model downloads,
unlabeled stubs, delayed background upload or guaranteed local runtime support.

## Inputs, outputs and boundary

Input: synthetic local case, selected profile, explicit connectivity/mode state,
preloaded model and catalog availability.
Output: local degraded proposals with human-review status, or explicit
unavailability. Identity and evidence mapping remain local.

## Acceptance criteria

| ID | Given / when | Required observable result | Planned evidence |
| --- | --- | --- | --- |
| OF-01 | Disconnected mode is selected with supported preloaded artifacts | Local inference runs and results are labeled local/degraded | Local-adapter test and later live runtime smoke test |
| OF-02 | The model/catalog/profile is unavailable locally | Explicit unavailable result; no invented successful coding | Missing-artifact/profile cases |
| OF-03 | Any case runs disconnected | Zero cloud calls, downloads, remote telemetry or queued upload retries | Transport capture plus later blocked-network inspection |
| OF-04 | Connectivity returns after an offline case | No automatic replay/upload; further cloud use requires an explicit authorized action | Reconnection and queue-inspection cases |
| OF-05 | The reviewer views a local result | Source mode and mandatory review remain visible; evidence/catalog validation still applies | Browser assertions and shared validation tests |

## Open decisions

Runtime/model capability, local retrieval mechanism, connectivity transition
semantics and bounded timeouts. No installation occurs as part of this spec.

## Approval and evidence

Draft only. No feature code or acceptance tests have been written.
