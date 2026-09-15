# Catalog Increment Review

Review date: 2026-09-14

## Scope

- Previous catalog maintenance boundary: 2026-09-07.
- Search window: 2026-08-24 through 2026-09-14, retaining roughly 14 days of overlap for delayed indexing, repository releases, and product-status changes.
- Sources checked: official arXiv recent listings and record pages; official paper pages, GitHub repositories, source trees, installation and execution instructions, data releases, and licenses; and first-party CAD vendor product pages and release notes.
- Search concepts: parametric CAD, B-rep, CSG, sketches and constraints, engineering drawings, text/image/sketch-to-CAD, CAD generation and reconstruction, CAD agents, CAD/CAM, manufacturing-aware design, CAD-native datasets, executable evaluation, and physics-aware design.
- Curation boundary: resources must directly operate on editable CAD representations, CAD-native engineering workflows, or CAD-specific evaluation. Generic 3D/mesh generation, medical uses of CAD, EDA-only work, and unreleased product vision remain outside the catalog.

## Result

Three paper entries met the evidence and relevance threshold. No separately released dataset or benchmark, independently useful open-source tool, or company product change qualified for a new entry.

| Resource class | High-signal candidates reviewed | Added | In-place updates | Deferred or excluded |
|---|---:|---:|---:|---:|
| Papers | 8 | 3 | 0 | 5 |
| Datasets and benchmarks | 4 | 0 | 0 | 4 |
| Open-source projects | 10 | 0 | 0 | 10 |
| Company products | 8 vendor families | 0 | 0 | 8 unchanged or non-qualifying |
| **Net README change** | — | **3** | **0** | — |

The README catalog moves from 602 to 605 entries. The historical JSONL registry remains at 638 deduplicated records, including 496 dated 2024–2026, because this weekly increment does not rewrite that separately sourced snapshot.

## Papers

Official arXiv records and recent listings for `cs.CV`, `cs.SE`, `cs.AI`, `cs.CL`, `cs.GR`, and `cs.CE` were checked with focused CAD and engineering-design queries.

### Added

- **Learn the Solid, Not the File** (`2609.11573`) — A canonical region graph derived from the solid rather than file-specific face partitions, evaluated under repartitioning, kernel round-trips, rigid motions, and independently authored FreeCAD models.
- **CIT-CAD** (`2609.07434`) — A Constraint Intent Tree guides executable CadQuery generation and supports deterministic construction-aware verification and repair.
- **LLM-Aided Design for Manufacturing** (`2609.05559`) — A multi-agent loop proposes manufacturability edits to CadQuery programs and verifies each transition by compilation and visual review.

### Deferred or Excluded

- **RealCADBench** (`2609.03773`) now describes a final public release boundary, but still provides no stable dataset, code, download, or leaderboard endpoint; deferred pending an accessible release.
- The human FreeCAD data described in **Learn the Solid, Not the File** has no independent public dataset endpoint and remains attached to the paper entry only.
- Generic image/text-to-mesh generation, non-editable 3D reconstruction, EDA-only work, and unrelated uses of the CAD acronym were excluded.

## Datasets and Benchmarks

- RealCADBench remains deferred because its 12,632-task specification and metrics are documented but the promised public assets are not linked or independently accessible.
- The human-authored FreeCAD equivalence data in `2609.11573` and the 46-part DFM study in `2609.05559` are not separately released benchmark resources.
- No other candidate combined CAD-native tasks, explicit metrics, and a stable public data or evaluation release.

## Open-Source Projects

GitHub searches covered text-to-CAD, parametric CAD, CAD agents, FreeCAD, CadQuery, build123d, OpenSCAD, MCP, and CAD verification.

- **HarnessCAD** remains deferred: its source, tests, CLI, examples, and third-party notices are substantial, but the repository still has no root project license or unambiguous package-level license declaration.
- New repositories that were empty, README-only, generated skill wrappers, small demonstrations, mirrors, or lacked installation, execution, tests/examples, and clear license evidence were excluded.
- No paper implementation with a verified public repository appeared for the three added papers.

## Company Products

First-party product and release material was checked for Autodesk/Fusion, Siemens/NX, Dassault Systèmes/SOLIDWORKS, PTC/Creo and Onshape, Ansys, nTop, and AI-native CAD/engineering vendors.

- No new CAD-native capability was verified as publicly available, beta, or early access during the review window.
- Existing cataloged products did not show a verified roadmap-to-available status transition.
- PLM-only assistants, general documentation chat, financing announcements, and ordinary text/image-to-mesh products were excluded.

## Deduplication and Validation

- README and `research/papers/*.jsonl` were checked by normalized title, unversioned arXiv ID, DOI, paper URL, and code/project URL before insertion.
- Each resource appears once in its most specific section; data and implementations remain attached to their paper when they are the same resource.
- All new arXiv links use unversioned identifiers as labels.
- `python3 scripts/validate_catalog.py` passes with 605 README entries, 638 deduplicated JSONL records, and 496 JSONL records dated 2024–2026.
- `git diff --check` passes.
