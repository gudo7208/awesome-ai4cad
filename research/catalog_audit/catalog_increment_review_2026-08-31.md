# Catalog Increment Review

Review date: 2026-08-31

## Scope

- Previous catalog maintenance boundary: 2026-08-27.
- Search window: 2026-08-13 through 2026-08-31, retaining roughly 14 days of overlap for delayed indexing, repository releases, and product-status changes.
- Sources checked: official arXiv recent listings and record pages; official GitHub repositories, releases, package metadata, source trees, tests, examples, and licenses; and first-party product pages, release notes, and vendor announcements.
- Search concepts: computer-aided design/CAD, parametric CAD, B-rep, CSG, sketches and constraints, extrusion and feature histories, engineering drawings, text/image/sketch-to-CAD, CAD generation/editing/reconstruction/understanding/retrieval, CAD agents, CAD/CAM, manufacturing-aware design, executable CAD evaluation, and physics-aware CAD benchmarks.
- Curation boundary: resources must directly act on editable CAD representations, CAD-native engineering workflows, or CAD-specific evaluation. Generic mesh/3D generation, Blender-only editing, non-AI optimization, PLM-only assistants, and product announcements without a released capability remain outside the catalog.

## Result

The review added two executable CAD-native benchmarks and one independently useful open-source CAD tool. No paper or company-product entry met the threshold for a new catalog item. The final normalized-URL check also repaired two older paper entries that shared a generic ResearchGate homepage.

| Resource class | High-signal candidates reviewed | Added | In-place updates | Deferred or excluded |
|---|---:|---:|---:|---:|
| Papers | 6 | 0 | 2 metadata repairs | 4 excluded; 2 already cataloged |
| Datasets and benchmarks | 3 | 2 | 0 | 1 duplicate mirror |
| Open-source projects | 8 | 1 | 0 | 1 deferred; 6 excluded |
| Company products | 8 vendor families | 0 | 0 | 8 unchanged or non-qualifying |
| **Net README change** | — | **3** | **0** | — |

The README catalog moves from 595 to 598 entries. The historical JSONL registry remains at 638 deduplicated records, including 496 dated 2024–2026, because this weekly increment does not rewrite that separately sourced snapshot.

## Papers

Official arXiv recent listings for `cs.CV`, `cs.AI`, `cs.CE`, `cs.RO`, `cs.GR`, `cs.HC`, `cs.LG`, and `math.OC` were checked with focused CAD and engineering-design terms.

- IterCAD (`2608.24020`) and Design-to-Plan (`2608.24039`) appeared inside the overlap window but were already present, so no duplicate entries were added.
- Procedura (`2608.26238`) emits editable OpenSCAD programs and machine-checkable mates, but its evaluated scope is primarily articulated 3D-asset generation and mesh-oriented export rather than a CAD-native engineering design or evaluation workflow; excluded under the current boundary.
- ViSculpt (`2608.24169`) edits arbitrary meshes through Blender rather than editable parametric CAD or B-rep/CSG; excluded.
- TailorCoPilot (`2608.25462`) targets garment pattern-making interactions and does not establish a direct engineering-CAD contribution; excluded.
- A recent cable-structure topology-optimization paper was relevant to design optimization but did not present a clear AI or learning contribution; excluded.

### In-Place Metadata Repairs

- **BRepGAT** — Replaced a generic ResearchGate homepage with DOI `10.1093/jcde/qwad106` and restored the publisher-verified authors, journal, and 2023 publication year.
- **Real-Time Tool-Path Planning Using Deep Learning for Subtractive Manufacturing** — Replaced the same generic ResearchGate homepage with DOI `10.1109/TII.2023.3342474` and restored the IEEE-verified authors, venue, and 2024 publication year.

No new-paper candidate required a version-only or successor update.

## Datasets and Benchmarks

### Added

- **ParamCAD-AgentBench** — Public executable benchmark for long-horizon language agents constructing kernel-valid parametric CAD. The frozen preview contains 2,409 CadQuery/OpenCASCADE-validated models and 4,818 paired abstract/detailed tasks. The 400-model development split exposes oracles; test and challenge source geometry and oracles are withheld. Code is MIT-licensed, while the data has separate research-release terms. Repository validation completed successfully with `python scripts/validate_release.py`. Source: `https://github.com/Fasuiker/ParamCAD-AgentBench`.
- **ParaEval** — Apache-2.0 evaluation framework for executed Rhino/Grasshopper artifacts across runtime validity, measured geometry, visual judgment, and headless structural solvability. The repository includes runnable CLI entry points, examples, tests, CI, and two sample `.3dm` models. It reports aggregate development results for 2,216 records across 139 prompts, but does not publish those underlying evaluation records; the README entry therefore describes the public evaluation framework rather than claiming a released full corpus. Source: `https://github.com/magnush01/ParaEval`.

### Excluded

- A newly surfaced `CADTestBench` repository was a mirror of the already cataloged official `dimitrismallis/CADTestBench` implementation; excluded as a duplicate.

## Open-Source Projects

GitHub repository searches covered text-to-CAD, parametric CAD, CAD agents/copilots, FreeCAD, CadQuery, build123d, OpenSCAD, MCP, CAD verification, and CAD benchmarks. More than 100 raw results were noisy forks, mirrors, and minimal scaffolds; eight high-signal repositories received source-tree review.

### Added

- **build123d-mcp** — Apache-2.0 MCP server using build123d/OpenCascade to let AI clients iteratively create, render, inspect, measure, repair, and export CAD as STEP, STL, SVG, and DXF. The repository contains a packaged command-line entry point, PyPI release path, CI, source modules, examples, and tests, and is independently useful beyond any single paper. Source: `https://github.com/pzfreo/build123d-mcp`.

### Deferred or Excluded

- **HarnessCAD** — Substantial multi-backend implementation with installation instructions, CLI entry points, source, and tests, but the README's MIT claim was not backed by a root `LICENSE` file or package-license field when inspected. Deferred pending unambiguous repository-level license evidence.
- **FreeCAD MCP Next** — Public implementation with source and tests, but it identifies itself as derived from the already cataloged `neka-nat/freecad-mcp`; excluded as a successor/fork without a sufficiently distinct catalog role.
- Recent `text-to-cad`, `CADTestBench`, and similar repositories whose own badges or metadata pointed to already cataloged canonical projects were excluded as mirrors or forks.
- README-only repositories, empty scaffolds, and projects lacking a usable execution path or inspectable implementation were excluded.

## Company Products

First-party pages and release material were checked for Autodesk/Fusion, Siemens/NX, Dassault Systèmes/SOLIDWORKS, PTC/Creo and Onshape, Ansys/Synopsys, nTop, and AI-native engineering vendors including Backflip.

- Onshape's FeatureScript MCP release, SOLIDWORKS Design AI companions AURA and LEO, and the Backflip Fusion add-in remain publicly described and were already represented accurately in the catalog.
- Autodesk, Siemens, PTC, Ansys/Synopsys, and nTop did not publish a new qualifying CAD-native capability inside the review window that was both concrete and publicly available, beta, or early access.
- PLM-only assistants, roadmap language, webinars, generic conversational help, and text/image-to-mesh offerings were not treated as released CAD-product evidence.

No commercial entry needed a status transition or in-place metadata update.

## Deduplication and Validation

- README and `research/papers/*.jsonl` were checked using canonical titles, unversioned arXiv IDs, DOI links, and normalized project URLs before insertion.
- Each new resource appears once in the most specific section; the benchmark entries are not repeated under tools, and the standalone MCP server is not attached to a paper.
- All three repository URLs resolve to the canonical public projects. The two pre-existing duplicate generic ResearchGate links were replaced with their distinct primary DOI records, leaving no duplicate normalized URL among catalog entries.
- `python3 scripts/validate_catalog.py` passes with 598 README entries, 638 deduplicated JSONL records, and 496 JSONL records dated 2024–2026.
- `git diff --check` passes.
