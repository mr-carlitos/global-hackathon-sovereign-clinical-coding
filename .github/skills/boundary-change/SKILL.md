---
name: boundary-change
description: Implement or change local detection, FHIR projection, token vault, outbound contracts or audit handling.
---

Read AGENTS.md, docs/privacy.md and docs/architecture.md.
Trace every data path including logs, exceptions, telemetry, browser traces,
retries, attachments, DNS and redirects. Raw identity and keys stay local.
Add adversarial synthetic fixtures before changing behavior. Bind gate approval
to the exact bytes and destination used by the transport; fail closed.
Test detector failure, unsupported input, unknown pack, cross-job response,
prompt injection and offline mode. Check network calls, not just return values.
Do not claim anonymization, legal compliance or universal zero leakage from a
finite test suite. Preserve human review and disclose unsupported cases.
