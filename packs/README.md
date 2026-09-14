# Jurisdiction design contracts

These JSON files describe intended profiles, **not executable egress policies or
approved catalog rights**. No runtime loader or clinical catalog is implemented.
`scripts/check_repo.py` validates their structure using only the Python standard
library. Validation does not authorize clinical use or cloud upload.

Every pack has:

| Field | Meaning |
| --- | --- |
| `schema_version` | Contract version, currently integer `1` |
| `id` | Unique lowercase hyphen-separated identifier |
| `country` | Two uppercase letters; validation does not certify ISO membership |
| `locales` | Unique language-country tags supported by this demo profile |
| `status` | Must be `design_only` until a reviewed runtime contract replaces this one |
| `clinical_use` | Must be `false` |
| `coding` | Task, explicit care setting, system, edition and proposed effective dates |
| `catalog` | Publisher/source/terms references, operator review gate, no redistribution |
| `boundary` | Synthetic-only, local identity, fail-closed and no cloud authorization |

Add a new JSON file instead of branching the core code by country. The checker
validates all files, rejects duplicate pack IDs and reports failures explicitly.
Adding a pack does not install recognizers, translators, catalog rules or Azure
resources. A future runtime must resolve the requested pack exactly, validate
its policy/adapters and reject unsupported combinations.

Care setting, version and legal applicability require independent review. The CH
`coding-demonstration` profile does not claim to implement Swiss billing or a
complete inpatient coding standard. US outpatient diagnosis proposals also remain
a non-clinical demonstration.
