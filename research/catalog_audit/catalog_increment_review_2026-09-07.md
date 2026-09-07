# Catalog Increment Review

Review date: 2026-09-07

## Scope

- Previous catalog maintenance boundary: 2026-08-31.
- Search window: 2026-08-17 through 2026-09-07, retaining roughly 14 days of overlap for delayed indexing, repository releases, and product-status changes.
- Sources checked: official arXiv recent listings and record pages; official paper project pages, GitHub repositories, source trees, installation and execution instructions, tests, data releases, and licenses; and first-party CAD vendor product pages and release notes.
- Search concepts: computer-aided design, parametric CAD, B-rep, CSG, sketches and constraints, feature histories, engineering drawings, text/image/sketch-to-CAD, CAD generation and reconstruction, CAD agents, CAD/CAM, manufacturing-aware design, CAD-native datasets, executable evaluation, and physics-aware design.
- Curation boundary: resources must directly operate on editable CAD representations, CAD-native engineering workflows, or CAD-specific evaluation. Generic 3D/mesh generation, medical uses of CAD, EDA-only work, and unreleased product vision remain outside the catalog.

## Result

Four paper entries met the evidence and relevance threshold. No separately released dataset or benchmark, independently useful open-source tool, or company product change qualified for a new entry.

| Resource class | High-signal candidates reviewed | Added | In-place updates | Deferred or excluded |
|---|---:|---:|---:|---:|
| Papers | 9 | 4 | 0 | 5 |
| Datasets and benchmarks | 3 | 0 | 0 | 3 |
| Open-source projects | 7 | 0 | 0 | 7 |
| Company products | 8 vendor families | 0 | 0 | 8 unchanged or non-qualifying |
| **Net README change** | — | **4** | **0** | — |

The README catalog moves from 598 to 602 entries. The historical JSONL registry remains at 638 deduplicated records, including 496 dated 2024–2026, because this weekly increment does not rewrite that separately sourced snapshot.

## Papers

Official arXiv records and recent listings for `cs.CV`, `cs.SE`, `cs.AI`, `cs.CL`, `cs.GR`, and `cs.CE` were checked with focused CAD and engineering-design queries.

### Added

- **VisCAD** (`2609.03811`) — Multimodal industrial part-to-program generation and an assembly-specific harness for mating, pose estimation, and placement.
- **RealCAD** (`2608.30617`) — Real-image-to-editable-CAD reconstruction with a corrected parameter representation and the OpenRealCAD photo/command-sequence data release; the official repository contains model, data, evaluation, training, and testing source plus a license.
- **MIRAGE-CAD** (`2608.28669`) — Construction-mediated generation of executable OpenCASCADE Python programs from text, image, point-cloud, and STEP/B-Rep inputs; its official repository includes packaged source, dependencies, documentation, evaluation scripts, reports, and a license.
- **Learning to Ground Before Reading** (`2608.29268`) — Full-page PCB engineering-drawing parsing into region classes, boxes, and structured content.

### Deferred or Excluded

- **RealCADBench** (`2609.03773`) specifies 12,632 multimodal part and assembly tasks and CAD-native metrics, but no stable public dataset, code, download, or leaderboard release was found; deferred pending release evidence.
- Generic image/text-to-mesh generation, non-editable 3D reconstruction, PCB work without an engineering-drawing or CAD workflow, and unrelated uses of the CAD acronym were excluded.

## Datasets and Benchmarks

- **OpenRealCAD** is described and linked with the RealCAD method in one README entry to avoid duplicating the same work across sections. The official release pairs four-view photographs of 392 printed objects with CAD command sequences.
- **RealCADBench** remains deferred because its paper describes tasks and metrics but does not provide a stable public release endpoint.
- The Engineering Drawing Dataset used by the PCB parser was not added as a separate entry because the paper does not establish an independently released dataset page or download.

## Open-Source Projects

GitHub searches covered text-to-CAD, parametric CAD, CAD agents, FreeCAD, CadQuery, build123d, OpenSCAD, MCP, and CAD verification. Seven high-signal repositories received README and tree review.

- RealCAD and MIRAGE-CAD are attached to their paper entries rather than repeated as tools.
- **HarnessCAD** remains deferred: its source, tests, and CLI are substantial, but the repository still has no root license file or unambiguous package-level license evidence.
- Newly created repositories that were empty, README-only, small demonstrations, mirrors, or lacked installation, execution, tests/examples, and clear license evidence were excluded.
- No new repository demonstrated sufficient independent utility beyond a paper implementation to justify a standalone Open-Source Tools entry.

## Company Products

First-party product pages and release material were checked for Autodesk/Fusion, Siemens/NX, Dassault Systèmes/SOLIDWORKS, PTC/Creo and Onshape, Ansys/Synopsys, nTop, and AI-native CAD/engineering vendors.

- No vendor published a new qualifying CAD-native capability during the review window that was both concrete and publicly available, beta, or early access.
- Existing cataloged capabilities did not show a verified roadmap-to-available status transition.
- PLM-only assistants, generic documentation chat, financing announcements, and ordinary text/image-to-mesh products were not treated as CAD-native product evidence.

## Deduplication and Validation

- README and `research/papers/*.jsonl` were checked by normalized title, unversioned arXiv ID, DOI, paper URL, and code/project URL before insertion.
- Each resource appears once in its most specific section; datasets and implementations remain attached to their paper when the work is the same resource.
- All new arXiv links use unversioned identifiers as labels.
- `python3 scripts/validate_catalog.py` passes with 602 README entries, 638 deduplicated JSONL records, and 496 JSONL records dated 2024–2026.
- `git diff --check` passes.
