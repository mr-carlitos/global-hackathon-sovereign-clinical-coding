# Hospital egress gateway

Status: Draft
Spec approval: Not granted
Implementation authorization: Not granted
Proposed owner / issue: Software engineer, #3

## Outcome and scope

The hospital operator can see what is permitted to leave and why a request was
blocked. Only minimized synthetic clinical content reaches an approved destination.
Follow docs/architecture.md and docs/privacy.md.

Non-goals: proof of anonymization, legal certification, real patient processing,
production firewall design or authorization based solely on the country dropdown.

## Inputs, outputs and boundary

Input: locally projected clinical facts and narrative, local detection result,
selected pack/policy versions, intended destination and random per-job token.
The runtime request schema and local evidence map are not implemented yet.

Output: blocked local result, or the exact approved outbound envelope. No identity
mapping, raw FHIR, detector input or local re-identification material is exported.

## Acceptance criteria

| ID | Given / when | Required observable result | Planned evidence |
| --- | --- | --- | --- |
| EG-01 | A valid minimized request meets an approved runtime policy | Sent bytes and destination match the approved envelope; local audit binds that decision | Capturing transport and canonical-envelope comparison |
| EG-02 | Local detector times out, fails or returns an invalid result | Blocked result, sanitized local event, zero cloud calls including retries | Fault injection plus call count |
| EG-03 | Pack/policy is missing, unknown, incompatible or still design-only | Block; never default to another pack | Invalid-pack cases and transport inspection |
| EG-04 | FHIR contains unsupported structures or unprocessed content | Reject before egress; no raw-bundle pass-through | Nested narrative/extension/reference/attachment fixtures |
| EG-05 | Destination or processing geography violates the approved posture | Block; redirects cannot expand the destination allowlist | Destination/redirect cases; later network-denial test |
| EG-06 | Seeded identifiers appear in synthetic input or exceptions | No seeded value in captured egress or exported logs for the fixed corpus | Exact seeded-value checks; disclose corpus size and detector limitations |

## Open decisions

Exact outbound schema, supported FHIR resource/field subset, transformations,
detector thresholds and timeout, canonicalization and network enforcement.
Application-level tests alone will not prove host-level egress isolation.

## Approval and evidence

Draft only. No feature code or acceptance tests have been written.
