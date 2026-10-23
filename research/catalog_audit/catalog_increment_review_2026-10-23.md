# Catalog Increment Review

Review date: 2026-10-23

## Scope

Focused public-source review after the 2026-09-14 maintenance boundary, with
overlap for older work indexed late. Search concepts included parametric CAD,
functional mechanisms, stateful CAD editing, CAD constraints, engineering
drawings, visual CAD agents, and executable evaluation. Official arXiv records
were opened to verify each included title, author list, and contribution.
This increment is selective and does not claim exhaustive coverage.

## Added papers

| Official source | Placement | Verified contribution |
|---|---|---|
| [EngiWorld — 2609.37686](https://arxiv.org/abs/2609.37686) | Benchmark Challenges | Artifact-centric engineering evaluation includes CAD, CAE, CAM, BIM, EDA, and DCC. It is included for its CAD-native engineering tasks, not for EDA alone. |
| [Functional CAD Mechanisms — 2610.26861](https://arxiv.org/abs/2610.26861) | Benchmark Challenges | FunCAD-Harness builds candidate-specific physical tests; FunCADBench covers functional mechanism families. |
| [AgenticCADedit — 2609.29621](https://arxiv.org/abs/2609.29621) | CAD Editing | Persistent CAD state supports incremental edits, geometric inspection, and individual-operation rollback. |
| [ConCAD — 2609.34494](https://arxiv.org/abs/2609.34494) | Reinforcement Learning-Enhanced Generation | Code-level constraints and execution-level geometric rewards support constraint-aware image-to-CAD generation. |
| [DrawingsDreamer — 2609.35242](https://arxiv.org/abs/2609.35242) | Floor Plan and Drawing Generation | Hierarchical tokenization supports multi-view vector engineering drawings. |
| [Vision2CAD — 2609.22688](https://arxiv.org/abs/2609.22688) | LLM and VLM-Based Generation | Explicit geometry IDs, coordinate conversion, and deterministic kernel operations support parametric modeling. |
| [DepthBenchCAD — 2609.15122](https://arxiv.org/abs/2609.15122) | Evaluation Metrics | Separates tasks, generations, and parameter edits when allocating a fixed evaluation budget. |

These are paper entries. Their inclusion does not certify a downloadable dataset,
licensed implementation, or reproduced result. No separate tool or dataset entry
was created merely from a paper's claim of a release.

## Deferred and duplicate candidates

- CIT-CAD (`2609.07434`) and LLM-Aided Design for Manufacturing (`2609.05559`)
  are already in README and were not inserted again.
- RealCADBench (`2609.03773`) was revisited at the paper-record level, but no new
  accessible asset release was established in this pass. The previous release
  verification requirement remains unresolved, so it remains deferred.
- The existing Luphra PR #3 was inspected. Its historical 595 → 596 count patch
  cannot be applied to the current catalog as written. This paper increment does
  not decide the product's inclusion or close the contributor's PR.
- Generic 3D mesh generation and EDA-only search results were excluded.

## Registry and validation

- README catalog entries: 605 → 612.
- Deduplicated JSONL records: 638 → 645.
- JSONL records dated 2024–2026: 496 → 503.
- Seven new records are stored in `research/papers/maintenance_2026-10-23.jsonl`;
  historical JSONL files remain intact.
- New entries were checked against README and all registry files by unversioned
  arXiv ID and normalized title. Every historical README catalog entry is unchanged.
- README metadata, badges, AGENTS counts, and validator expectations were updated
  together. All arXiv labels use their unversioned identifiers.
- `python3 scripts/validate_catalog.py` and `git diff --check` pass.
