# Diagnosis proposals and evidence binding

Status: Draft
Spec approval: Not granted
Implementation authorization: Not granted
Proposed owner / issue: Engineer and Carlos, #4

## Outcome and scope

The reviewer receives diagnosis-code proposals supported by documented facts,
with versioned catalog membership checks and visible documentation gaps.
Follow docs/catalogs.md and docs/privacy.md.

Non-goals: new medical diagnoses, tariffs, reimbursement, autonomous acceptance,
claims submission, complete catalog-rule coverage or restricted catalog content.

## Inputs, outputs and boundary

Input: approved minimized request, opaque job token and exact pack/system/edition.
Retrieval uses only catalog content whose intended use has passed operator review.

Output: structured proposals with code/system/edition, supporting narrative spans,
validation results, documentation gaps, mode and mandatory human-review status.
Original-text evidence mapping and identity restoration occur only locally.

## Acceptance criteria

| ID | Given / when | Required observable result | Planned evidence |
| --- | --- | --- | --- |
| CE-01 | A proposal names a code outside the selected system/edition | Reject it instead of displaying a validated proposal | Catalog membership and edition-mismatch cases |
| CE-02 | Evidence offsets are out of bounds or the cited text differs | Reject; do not invent a quote or rationale as evidence | Offset/quote mismatch cases |
| CE-03 | Model output is malformed or identifies another job/pack | Explicit invalid result; no local identity lookup for that response | Malformed and cross-job fixtures |
| CE-04 | A reviewed synthetic note contains negation or family history | Do not validate the negated/family condition as the patient's diagnosis | Curated clinician-reviewed expectations; report model failures |
| CE-05 | CH and US profiles are selected | Same core orchestration, correct source/edition attribution and actual processing-location label | Contract tests plus later browser scenarios |
| CE-06 | Valid proposals are shown to a reviewer | Human-review-required state remains visible; validation coverage and gaps are disclosed | UI assertions and structured-output inspection |

## Open decisions

Structured response schema, evidence offset convention, local span mapping,
minimum supported deterministic rules and evaluation rubric. Catalog import and
actual cloud-region availability are prerequisites, not assumed completed.

## Approval and evidence

Draft only. No feature code or acceptance tests have been written.
