# Sovereign Clinical Coding

**A three-day Microsoft Global Hackathon project: local identity handling,
policy-controlled Azure inference, and human-reviewed diagnosis-code proposals.**

Private incubation repository owned by `mr-carlitos`. Intended to become a
reusable solution accelerator after a public-release review. Not an official
Microsoft product, medical device, compliance certification, or production system.

## Status

Repository foundation and design stage. The application, local detector, token
vault, egress gateway, catalog importers, UI, and Azure deployment are **not yet
implemented**. The initial executable checks validate configuration contracts;
they do not validate clinical performance or privacy.

## The story

A hospital wants help coding a clinical note but must control what leaves its
boundary. Local detection and a local token vault remove or replace identifiers.
A fail-closed gateway permits only policy-approved, minimized clinical content
to Azure. Cloud retrieval and inference propose diagnosis codes with evidence.
Identity is restored only locally, and a human accepts or rejects the proposal.

The demo uses **entirely synthetic patient records**. One Azure VM represents the
fictional hospital; it is an architectural simulation, not actual on-premises
sovereignty. Two VMs are the maximum planned hospital footprint if runtime
compatibility requires a separate Foundry Local host.

**Pseudonymized is not necessarily anonymized.** Clinical content still crosses
the boundary and can retain re-identification risk. We do not claim "no patient
data leaves," "zero identifiers ever," or that an external-processor prohibition
is automatically satisfied. See [privacy and threat model](docs/privacy.md).

## Hackathon scope

- Switzerland: diagnosis coding with ICD-10-GM, initially German.
- USA: diagnosis coding with ICD-10-CM, initially English.
- Versioned packs separate country, care setting, code system, locale, policy,
  and deployment posture. No country branches in the core pipeline.
- No CPT, TARDOC, tariff calculations, reimbursement, or automated billing.
- Real catalog integration is gated by source-specific terms and provenance.
  No third-party catalog content is bundled in Git, CI artifacts, or images.
- A visibly degraded local mode never silently falls back to cloud processing.

See [catalog policy](docs/catalogs.md), including what remains to be verified
before indexing an official catalog.

## Development

Planned stack: Python 3.12 / FastAPI, React / TypeScript, Bicep.
The foundation checks need only Python's standard library:

```sh
python3 scripts/check_repo.py
python3 -m unittest discover -s tests -v
```

GitHub Actions runs the same checks and retains logs as downloadable artifacts.
No Azure credentials or catalog downloads are needed.

## Project guide

| Document | Purpose |
| --- | --- |
| [Architecture](docs/architecture.md) | Boundaries, Azure components, pack interfaces |
| [Three-day plan](docs/plan.md) | Ownership, priorities, measurable acceptance gates |
| [Demo script](docs/demo.md) | Five-minute story and failure-path demonstrations |
| [Catalog policy](docs/catalogs.md) | Diagnosis scope, attribution and import gates |
| [Privacy](docs/privacy.md) | Honest claims, threat model, audit limits |
| [Agent workflow](docs/agent-workflow.md) | Skills, MCP, CI outputs, scoped autonomy |
| [Azure access](docs/azure-access.md) | Identity, approval, deployment and cleanup plan |
| [Research](docs/research.md) | Primary sources and dated findings |
| [Contributing](CONTRIBUTING.md) | Team workflow and public-release checklist |

The original concept also envisaged service/tariff coding, Azure Functions,
SQL Ledger, Semantic Kernel, and jurisdiction-specific rules. Those remain
possible extensions; they are not all required services for the three-day MVP.
