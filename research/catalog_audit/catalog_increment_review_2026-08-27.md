# Catalog Increment Review

Review date: 2026-08-27

## Scope

- Previous catalog maintenance boundary: 2026-07-27.
- Search window: 2026-07-13 through 2026-08-27, including a 14-day overlap to catch late indexing and revised metadata.
- Sources checked: the official arXiv API and record pages, plus official public GitHub repositories linked by authors or projects.
- Search concepts: parametric CAD, B-rep/CSG, engineering drawings, CAD agents, text/image/point-cloud-to-CAD, CAD-native benchmarks, topology optimization, and manufacturing-aware design loops.
- Curation boundary: entries must make a material AI contribution to CAD representation, generation, editing, analysis, simulation, or manufacturing. Medical uses of the abbreviation CAD, EDA-only work, generic 3D assets, generic implicit-shape learning, and non-AI engineering papers were excluded.

## Result

The merged search returned 97 candidates before relevance filtering and catalog deduplication.

| Decision | Count |
|---|---:|
| New work first published after 2026-07-27 | 24 |
| Earlier high-relevance omissions backfilled | 3 |
| Dataset and benchmark resources added in the second pass | 3 |
| Runnable open-source projects added in the second pass | 3 |
| Public company products added in the second pass | 7 |
| Existing entries updated in place | 2 |
| Net new README entries | 40 |

The README catalog therefore moves from 555 to 595 entries. The historical JSONL registry remains at 638 deduplicated records because this maintenance slice updates the public curated catalog and does not rewrite the separately sourced registry snapshot.

## Added arXiv Records

`2608.24760`, `2608.24056`, `2608.24039`, `2608.24020`, `2608.22606`, `2608.22128`, `2608.17843`, `2608.16485`, `2608.11793`, `2608.09706`, `2608.09296`, `2608.05714`, `2608.05539`, `2608.04955`, `2608.04434`, `2608.03062`, `2608.00891`, `2608.00800`, `2608.00799`, `2608.00473`, `2607.28217`, `2607.28050`, `2607.27558`, `2607.26234`, `2607.23191`, `2607.16631`, `2607.16288`, `2607.13174`, `2606.20146`, and `2604.14927`.

## Second-Pass Resource Review

The first pass was paper-centric and did not systematically cover standalone datasets, runnable repositories, or commercial releases. A second pass added:

- Datasets and benchmarks: MFGNet-Gear, STEP-Parts, and BIM-Edit.
- Open-source projects: MAC (Multi-Agent CAD), Text23D Mechanical, and Sphaire.
- Public products: Onshape Labs FeatureScript MCP Server, PTC Creo 13 AI Assistant, Ansys GeomAI, Autodesk Fusion AI, CloudNC CAM Assist, Backflip AI, and DraftAid.

The existing Dassault Systèmes Virtual Companions entry was replaced with the more concrete SOLIDWORKS Design AI Virtual Companions product entry. The existing A2Z record was corrected to its official A2Z-10M+ title, 2026 publication year, and arXiv author list.

## Verified Project Links

- HiFi-BRep: `https://github.com/1nnoh/HiFi-BRep`
- CADENA: `https://github.com/zhemdi/cadena`
- PhysicsBench leaderboard: `https://github.com/Narnialabs/leaderboard`
- CADCON derangement control: `https://github.com/Jacky628/cadcon-derangement-control`
- Customized foot orthoses prototype: `https://github.com/HAHA1122344/tans-fo-orthotics`
- Multimaterial distribution optimization: `https://github.com/LuoXueling/optimization_of_digital_material_distribution`
- MAC (Multi-Agent CAD): `https://github.com/Pan-Chera/Multi-Agent-CAD`
- Text23D Mechanical: `https://github.com/zqf3229294/Text23D`
- Sphaire: `https://github.com/PranavChahal/sphaire-web`

These repositories contained public implementation, evaluation, data, or experiment artifacts when checked. Merely existing repositories were not treated as sufficient evidence for a Code link.

## Deferred or Excluded

- ExpConCAD: the linked repository contained only a minimal placeholder README, so the paper was added without a Code link.
- AIMold: the linked repository contained only README and asset files, so the paper was added without a Code link.
- FORGE-SIM: the official project link in the paper returned 404, so no Code link was added.
- Nova3D (`2607.22738`): programmatic Blender asset generation rather than CAD-native representation or modeling.
- Fluid-SDF (`2607.18646`): generic two-dimensional implicit shape representation without a material CAD contribution.
- SUFLECA (`2607.15058`): CAD-to-image pose alignment and already excluded in the preceding review.
- `2608.10344`: relevant to topology optimization, but the work did not present a clear AI or learning contribution.
- Medical papers using CAD to mean coronary artery disease, EDA and hardware-design papers, and generic 3D generation results were removed during relevance filtering.
- Onshape AI Advisor was not added as a separate entry because it is primarily documentation and troubleshooting assistance; the action-capable FeatureScript MCP release represents the platform instead.
- Windchill AI was excluded because its current product scope is PLM and product-data retrieval rather than CAD modeling or engineering analysis.
- Generic text-to-mesh and image-to-mesh products were excluded unless they exposed editable parametric CAD, a feature tree, or a CAD/CAM/CAE-native workflow.

## Workflow Observations

- A broad `CAD` query has high recall but severe abbreviation and domain noise; it must be combined with focused queries and a manual relevance gate.
- Paper metadata stating that code is available is not enough for a Code link. Repository contents and link status must be checked.
- Generic 3D, simulation, BIM, and additive-manufacturing work need an explicit CAD-native or design-loop contribution to cross the catalog boundary.
- The exact README count is intentionally repeated in README metadata, the badge and denominator table, `AGENTS.md`, and the validator expectation; all locations must move together.
- Deduplication must be scoped to catalog list entries. The representative-anchor table intentionally reuses eight arXiv links, while the 582 catalog entries have no repeated exact title or arXiv ID.
- Two pre-existing catalog entries, BRepGAT and Real-Time Tool-Path Planning Using Deep Learning for Subtractive Manufacturing, share the generic `https://www.researchgate.net` URL. This increment does not change them, but their primary sources should be repaired in a separate metadata pass.
- The contributor guide and agent guide used a legacy entry template that did not match the README's description-bearing format; both guides were aligned with the catalog in this increment.
