# Research register

Reviewed 2026-09-14. Primary sources; observations are not legal opinions.
Re-check exact versions and terms at import/deployment time.

| Topic | Source | Project implication |
| --- | --- | --- |
| Accelerator examples | https://accelerators.ms/ ; https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator | Use a clear overview, setup, architecture, responsible-AI limits and cleanup; do not imply Microsoft endorsement |
| ICD-10-GM rights | https://www.bfarm.de/SharedDocs/Downloads/DE/Kodiersysteme/downloadbedingungen-2024.pdf?__blob=publicationFile | Attribute, preserve official content, respect original-format redistribution restrictions; review cloud-index use |
| Swiss official catalogs | https://www.mct.bfs.admin.ch/en/home | Use publisher files and verify edition/setting; no scraping proprietary tariff browsers |
| US editions | https://www.cms.gov/medicare/coding-billing/ICD-10-codes | April 2026 update applies through September 30; FY2027 starts October 1 |
| US source files | https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2026-update/ | Direct official import, retain provenance; third-party enhancements are not automatically covered |
| CPT exclusions | https://www.ama-assn.org/practice-management/cpt/cpt-licensing-frequently-asked-questions-faqs | CPT electronic development/testing requires rights; omit from MVP |
| OAAT exclusions | https://oaat-otma.ch/rechtliche-hinweise | Public access does not establish integration/redistribution permission; omit billing tariffs |
| HIPAA de-identification | https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html | Safe Harbor/Expert Determination are substantive standards, not synonyms for pseudonymization |
| Swiss patient data | https://www.edoeb.admin.ch/de/bekanntgabe-von-patientendaten | Sensitive health data and professional secrecy require separate assessment |
| Presidio limitations | https://github.com/microsoft/presidio/blob/main/docs/faq.md | Automated detection does not guarantee all identifiers are found |
| Foundry Local | https://learn.microsoft.com/en-us/azure/foundry-local/get-started ; https://learn.microsoft.com/en-us/windows/ai/foundry-local/get-started | SDK/OS/execution-provider support varies; run actual VM compatibility spike, especially WinML/GPU |
| Foundry processing geography | https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/deployment-types | Regional, Data Zone and Global are different processing scopes; resource location alone is insufficient |
| Agent skills | https://docs.github.com/en/copilot/concepts/agents/about-agent-skills | Small versioned repository skills complement universal instructions |
| Skill authoring | https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills | `.github/skills/<name>/SKILL.md`, descriptive triggers |
| Superpowers | https://github.com/obra/superpowers | Optional workflow framework; review/pin rather than bulk-install under time pressure |
| GitHub OIDC | https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure | Short-lived federation and restricted trust; verify current subject format |
| Azure federation | https://learn.microsoft.com/en-us/azure/developer/github/connect-from-azure-openid-connect | Entra application or managed identity federation instead of long-lived secrets |

## Important corrections to the original concept

The cloud receives clinical data, not "no data." An Azure-hosted hospital mock
is already hosted by a cloud processor. Country packs encode selected requirements,
not legal certification. An audit signature detects certain tampering, not unknown
identifier leakage. Disconnected operation needs preloaded artifacts. Catalog
copyright and model-weight licensing remain separate from source-code licensing.

## Unresolved before live implementation

Exact Swiss edition/care-setting guidance and cloud-index permission; catalog
acknowledgment records; local model/license/runtime; cloud model/version/region
quota and retention; VM size; approved subscription; scoped identities; collaborator
handles; repository protection availability. None is silently assumed complete.
