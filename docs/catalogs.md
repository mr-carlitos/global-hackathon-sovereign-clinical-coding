# Catalog selection and licensing gates

Decision: 2026-09-14. MVP is **diagnosis coding**, not service billing.
We avoid paid-code dependencies; we do not promise that every conceivable use is
license-free. Source terms can differ by language, edition, format, and publisher.

## Selected paths

| Pack | Intended system | Edition for fixed demo dates | Distribution |
| --- | --- | --- | --- |
| CH, German | ICD-10-GM systematic classification | 2024 for the proposed Swiss 2026 scenario; verify applicable care-setting guidance before import | Operator downloads official source after reviewing terms; never redistribute original archive |
| US, English | ICD-10-CM | FY2026 April update, encounters 2026-04-01 through 2026-09-30 | Operator obtains official CDC/CMS files; retain source and edition attribution |

Fix demo encounter dates to September 2026. Do not choose an edition by the
computer's current year. US FY2027 becomes effective October 1, 2026.
Swiss statistical coding guidance must not be presented as a universal outpatient
billing requirement; the first CH profile is an explicitly labeled coding demo.

BfArM conditions permit specified use subject to attribution and preservation
of official content, restrict redistribution in the acquired format, and discuss
derived value-added products. That does not automatically settle cloud indexing
or distribution of an embedding database. **Review that use before indexing.**
See the official [download conditions](https://www.bfarm.de/SharedDocs/Downloads/DE/Kodiersysteme/downloadbedingungen-2024.pdf?__blob=publicationFile).

Official US files are available from [CMS](https://www.cms.gov/medicare/coding-billing/ICD-10-codes)
and [CDC](https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Publications/ICD10CM/2026-update/).
Do not import third-party coding books, commentary, guidelines, or proprietary
crosswalks simply because the underlying code identifiers are publicly available.

## Import gate (to implement)

1. Select publisher, exact file, edition, language, applicable dates and setting.
2. Record source URL, retrieval date, SHA-256, terms URL, required attribution,
   and the operator's terms review/acknowledgment.
3. Check rights for local processing, cloud indexing, and any intended export
   independently. A download click is not blanket permission.
4. Validate archive paths and sizes, parser output, uniqueness, hierarchy and
   version; preserve official descriptions unchanged.
5. Store archives, normalized data and search indexes outside Git and CI artifacts.
   Display source/edition attribution in the UI.
6. Keep cloud upload disabled if scope is unclear. Use original synthetic test
   labels for pipeline development, visibly marked non-clinical, while resolving it.

No catalog is downloaded, licensed, indexed, or approved by merely selecting a
committed pack. The current files use `operator_review_required`.

## Explicit exclusions

CPT/HCPCS Level I, TARDOC, outpatient flat rates, SwissDRG grouping, tariff
calculations, payer rules and automated claims are outside the MVP.
CHOP, ICD-10-PCS and HCPCS Level II are future adapters, not current dependencies.

Before public release, review code licensing separately from data, model weights,
SDKs and trademarks. This repo currently grants **no open-source license**;
select one with the owner before making it public. No license is inferred from
the goal of eventually becoming a solution accelerator.
