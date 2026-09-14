---
name: jurisdiction-pack
description: Add or modify country, locale, code-system and edition packs; use for catalog or jurisdiction configuration work.
---

Read AGENTS.md, docs/catalogs.md, docs/architecture.md and existing packs.
Keep country, care setting, code system, edition and policy distinct.
Do not copy a country's settings and assert they satisfy another country's law.
Record official source and terms; do not bundle catalogs or enable cloud upload.
Update contract validation and tests for missing/invalid values, effective dates
and cross-pack isolation. Unknown packs must fail, never default to CH or US.
Run `python3 scripts/check_repo.py` and
`python3 -m unittest discover -s tests -v`.
Document limitations, commit and push the coherent change on a feature branch.
