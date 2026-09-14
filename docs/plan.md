# Three-day hackathon delivery plan

Planning baseline: 2026-09-14; three working days, not an assumed event deadline.
Team: Carlos/project lead, one software engineer, one solution-sales specialist,
with coding agents supporting bounded implementation and investigation.

## Day 1: prove feasibility and the boundary

Lead: Carlos on Azure/runtime; engineer on local pipeline; sales on narrative and
synthetic scenarios. Agents prepare contracts, tests and repeatable commands.

1. Bootstrap private GitHub repository, instructions, CI, design and pack contracts.
2. Confirm deployment subscription, region, VM/runtime support and modest cost
   estimate. Create only the approved demo resources; one hospital VM preferred.
3. Timebox Foundry Local installation and model evaluation to two hours. Test a
   compatible CPU path before GPU. If incompatible, document the precise blocker,
   select a supported host with approval; never relabel another runtime as Foundry.
4. Clear exact catalog source/usage terms, implement import provenance and choose
   ten synthetic notes (five per country/locale) with human-reviewed expectations.
5. Implement local FHIR projection, detector, vault and gateway. Demonstrate both
   a permitted request and an ambiguous/unsupported request being blocked.

Exit: real local inference works on the selected host, raw identifiers remain
local in the fixtures, and a failing detector causes **zero outbound calls**.
If catalog/cloud feasibility is blocked, keep the demo synthetic and label it.

## Day 2: connect cloud coding and country packs

Lead: engineer on coding service/retrieval; Carlos on cloud identity and egress;
sales validates the story and collects demo screenshots using synthetic data only.

1. FastAPI cloud service on Container Apps, approved model, catalog-only AI Search.
2. Structured proposals: code, system, edition, evidence spans, rule results,
   documentation gaps, mode and human-review status.
3. Enforce code membership, edition validity, evidence bounds and exact quotations;
   implement only explicitly documented rule coverage, not "all catalog rules."
4. React UI hosted on the hospital side: original input, redacted payload,
   egress decision, proposal evidence and local identity restoration.
5. Switch packs without modifying core pipeline code. Demonstrate mismatched
   deployment region and unknown pack rejection.

Exit: one end-to-end CH case and one US case. If only one cloud geography is
deployed, the other pack runs locally and is visibly labeled as such.

## Day 3: harden, measure, rehearse

1. Signed local audit chain and verifier; independently retain checkpoint.
2. Deliberate disconnect: preloaded local model/catalog, degraded status, no calls.
3. Run the fixed corpus and failure suite; preserve synthetic-only test reports.
4. Playwright: country selection, evidence, blocked request, disconnected banner,
   and keyboard navigation. Capture failure traces and console/network output.
5. Clean-clone setup rehearsal, demo recording, limitations slide and teardown
   rehearsal. Freeze features halfway through the day.

Exit: rehearsed five-minute demo, reproducible setup, actual measurements and
known limitations. No claim of clinical accuracy from ten synthetic cases.

## Acceptance gates

| Gate | Target |
| --- | --- |
| Synthetic fixtures | At least 10, split across CH/US, reviewed expected behavior |
| Known seeded identifiers | Zero seeded identifiers in captured egress for the fixed corpus; report denominator and residual risk |
| Fail-closed paths | Detector timeout, malformed/unknown pack, unsupported FHIR and denied destination each produce zero cloud calls |
| Code validity | Every displayed proposal belongs to selected imported system/edition |
| Evidence | Every displayed proposal has a valid supporting span; negation/history adversarial cases included |
| Country isolation | No CH/US branching in core orchestration; pack/version mismatch rejected |
| Offline | Network disabled, local mode clearly labeled, no queued hidden cloud retries |
| Audit | Altered events fail verification; truncated history tested against checkpoint |
| CI | Deterministic offline tests on every PR; separately labeled live evaluations |
| UX | Browser test covers success, blocked, offline and country-switch scenarios |

These are **planned gates**, not achieved results. Initial CI checks only the
repository and pack contracts.

## Backlog priorities and parallel ownership

| Priority | Slice | Proposed owner | Depends on |
| --- | --- | --- | --- |
| P0 | Repository, CI, source register | Carlos + agent | None |
| P0 | Local runtime + Azure model feasibility | Carlos | Deployment approval |
| P0 | Catalog import/provenance | Engineer + agent | Terms review |
| P0 | FHIR/minimization/vault/gateway | Engineer | Pack contracts |
| P0 | Cloud retrieval/proposal validation | Carlos + agent | Catalog + boundary |
| P0 | UI + local evidence binding | Engineer | Stable API |
| P0 | Synthetic scenarios + pitch | Sales specialist | Scope |
| P1 | Offline + signed audit + adversarial tests | Shared | End-to-end slice |
| P1 | Deployment/teardown + browser rehearsal | Shared | Deployed demo |
| Later | Billing, more nations, real EHR, production HSM | Unassigned | Post-hackathon |

Do not build Kubernetes, multi-agent orchestration, high availability, production
EHR integration or a full regulatory rule engine in these three days.
