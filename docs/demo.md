# Five-minute demo

**Opening:** "We separate identity handling from coding assistance. The hospital
controls an observable boundary; Azure receives only policy-approved clinical
content. This demo uses synthetic records, not actual patient data."

| Time | On-screen action | Point |
| --- | --- | --- |
| 0:00-0:40 | Show diagram and simulated-hospital label | Azure VM stands in for on-premises; not a physical-sovereignty claim |
| 0:40-1:40 | Select CH and a German synthetic note; show local detection and payload diff | Raw identity stays in the local path; show actual transmitted envelope |
| 1:40-2:30 | Retrieve diagnosis candidates and highlight evidence | Useful Azure inference grounded in an edition-specific catalog, not autonomous diagnosis |
| 2:30-3:10 | Select US English scenario | Same pipeline, different pack, catalog and policy; display actual processing location |
| 3:10-3:50 | Send deliberately unsupported/ambiguous fixture | Fail-closed decision and zero cloud calls, not a happy-path-only demo |
| 3:50-4:20 | Disconnect and repeat | Local, degraded mode; no silent cloud fallback |
| 4:20-5:00 | Verify audit chain, show metrics and limitations | Tamper evidence plus observed egress, not proof of perfect anonymization |

Cloud-heavy value: each eligible request uses Azure inference and catalog
retrieval, orchestrated in Container Apps. Do not claim consumption grows exactly
linearly: caching, routing and workload shape affect it.

Sales specialist owns the customer problem, limitations slide and reusable
story; engineers own evidence and architecture accuracy. Human review remains
visible throughout. Never show real records or imply a certified diagnosis.

Fallback order: live demo; clearly labeled recorded synthetic demo; explicit
unavailable component. Never disguise a stub or recording as live Foundry.
