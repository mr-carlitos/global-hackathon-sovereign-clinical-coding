# Privacy, clinical safety and threat model

This is an engineering demonstration, not legal advice or regulatory approval.
Only fully synthetic records are permitted. Primary references: [research](research.md).

## Claims we can and cannot make

We aim to demonstrate local identity handling, observable policy-controlled
egress, and evidence-linked diagnosis proposals on a disclosed synthetic corpus.
We cannot prove that automated detection finds every identifier in arbitrary
clinical text. Pseudonymized narratives can remain personal/health data.

A signed ledger proves integrity of recorded events under its trust assumptions;
it does not prove that all network traffic was logged, the host was uncompromised,
or no identifier survived detection. Report measured false negatives and test
coverage rather than "zero identifiers ever crossed."

HIPAA de-identification requires Safe Harbor or Expert Determination conditions;
token substitution alone is not either method. Swiss health data also requires
consideration of professional secrecy and applicable federal/cantonal rules.
Do not generalize EU DORA, NIS2 or AI Act obligations to every hospital or country.
A hard "no external processor" policy may still rule out this architecture.

## Threats and required demonstrations

| Threat | Planned control | Evidence required |
| --- | --- | --- |
| IDs in nested FHIR, narrative, extensions, references or attachments | Local allowlist projection; reject unsupported structures | Adversarial fixture coverage, no raw-bundle pass-through |
| Missed names, dates, rare events, quasi-identifiers | Local ensemble, minimization, ambiguity blocks | Recall/false-negative and clinical-utility evaluation by locale |
| Prompt injection in a note | Treat note as data; no tool access; strict output contract | Injection fixtures cannot alter policy or destinations |
| Gateway bypass / accidental SDK telemetry | OS/network egress restriction plus application gateway | Captured outbound request and network-denial tests |
| Sensitive logs and screenshots | Allowlisted telemetry; local-only raw UI | Inspect logs, browser traces, exception paths and artifacts |
| Wrong-patient response | Random per-job token, expiry, binding, replay control | Cross-job and replay rejection tests |
| Invalid or hallucinated codes | Exact catalog/version membership and evidence checks | Reject unknown codes, mismatched edition, unsupported assertions |
| Vault theft | Local encryption, access separation, key lifecycle | No mappings/keys in cloud; local recovery and deletion tests |
| Audit rewriting/truncation | Signed chain, external trusted checkpoints and verifier | Modified/reordered events fail; truncation needs a trusted final checkpoint |
| Country-policy confusion | Validated pack and restrictive hospital overlay | Unknown/changed pack blocks, no fallback to another jurisdiction |

The policy gate must bind its decision to the exact serialized request bytes,
destination, pack and detector versions. Logging a different object from the
transmitted object creates a time-of-check/time-of-use gap.

Store detailed audit evidence locally. Public/cloud audit exports must not include
raw payloads, deterministic identity hashes, or sensitive error strings. Prefer
keyed commitments locally; a plain hash of a predictable identifier leaks guesses.
A blocked request is recorded locally; exporting its raw details is prohibited.

## Clinical limitations

This assists coding of documented facts; it does not diagnose a patient.
Human review is mandatory. "Valid code" is not "correct diagnosis" or guaranteed
reimbursement. Do not infer a condition solely from a medication, negate an
explicit negation, or code a family-history statement as the patient's condition.
Evidence must identify the exact supported span, not merely echo a model rationale.

Live deployment with real data requires qualified clinical review, privacy and
legal assessment, security evaluation, retention and incident procedures, and
applicable contracts. The hackathon does not supply those approvals.
