# Expanded multi-source CAD review — 2026-10-23

## Scope and outcome

This pass expands the earlier narrow arXiv increment. It prioritizes July–October
2026 while backfilling current-year conference and journal omissions. It does
not describe all added records as newly published in the last month and does
not claim exhaustive coverage.

| Change | Count |
|---|---:|
| New paper entries | 22 |
| New software/platform entries | 4 |
| New dataset/challenge entries | 2 |
| New vendor capability entries | 2 |
| Existing README entries corrected/enriched | 8 |
| README entries before / after | 613 / 643 |
| Deduplicated JSONL records before / after | 645 / 675 |
| JSONL records dated 2024–2026 before / after | 503 / 533 |

The [candidate ledger](expanded_candidates_2026-10-23.json) records all additions,
metadata corrections, primary URLs, discovery routes, and source-level limits.
A [CSV view](expanded_candidates_2026-10-23.csv) supports filtering and review.
New machine-readable entries are in
`research/papers/expanded_2026-10-23.jsonl`; historical JSONL source snapshots
are preserved. The eight corrections apply to README metadata and are recorded
in the ledger rather than silently rewriting historical collection snapshots.

## Source expansion

| Source family actually checked | Example entry point | What it contributed |
|---|---|---|
| arXiv by task/representation | [CADFather](https://arxiv.org/abs/2610.09127), [LED-BENCH](https://arxiv.org/abs/2610.19571) | Agentic reconstruction, policy learning, GUI evaluation, drawings, segmentation, assembly planning |
| Conference programs/proceedings | [CVPR](https://openaccess.thecvf.com/CVPR2026), [ECCV accepted papers](https://eccv.ecva.net/Conferences/2026/AcceptedPapers), [SIGGRAPH program](https://s2026.conference-schedule.org/) | CAD-Refiner, bidirectional sketches, CADLoop, PP-Brep, accepted venues |
| Publishers | [State-CAD](https://doi.org/10.1016/j.cad.2026.104128), [Mind-CAD](https://doi.org/10.1016/j.cad.2026.104126), [BRepFacetGen](https://doi.org/10.1007/978-3-032-37258-1_35) | Journal work and ECCV material missed by arXiv-only discovery |
| Author/lab publication pages | [Xiang Xu](https://samxuxiang.github.io/) | B-rep publication status and the official ABC-1M asset link |
| GitHub search/topics | [text-to-CAD topic](https://github.com/topics/text-to-cad) | Independent tool discovery and source/license inspection |
| Hugging Face | [ABC-1M](https://huggingface.co/datasets/ADSKAILab/ABC-1M), [ECCV challenge](https://huggingface.co/datasets/jingwei-xu-00/eccv2026-cad-challenge-data) | Actual dataset splits, file paths, evaluation examples, and license notices |
| Vendor release notes | [Onshape October release](https://www.onshape.com/en/resource-center/what-is-new/propagate-configuration-inputs-references-persistent-center-mass-indicator-assemblies-ar-view-android), [NX 2606](https://blogs.sw.siemens.com/nx-manufacturing/whats-new-in-nx-for-manufacturing-2606-june-2026/) | Available CAD guidance and generative CAM capability |
| Specialist lists | [Awesome Neural CAD](https://bunnysocrazy.com/), [B-rep reconstruction list](https://github.com/Bigger-and-Stronger/awesome-brep-reconstruction) | Gap discovery followed by primary-source checks |
| Bibliographic indexes | DBLP title/DOI search | Journal discovery leads; not used as technical evidence |

GitHub repository search returned 30 leads. This is a discovery result, not a
claim that all 30 were fully reviewed. Eight focused repositories received
metadata/source-tree inspection attempts; seven had accessible trees and
READMEs, while one transport failure remains unresolved. Existing Chamfer and
text-to-cad entries were identified, avoiding duplicate software entries.

## Main additions

- Generation/reconstruction: UniBRep, CADFather, ReliCAD, HiCAD, PrimitiveCAD,
  StepCAD, CADForge, SightCAD, BrepForge, BRepFacetGen, and State-CAD.
- Editing/sketches/data: CAD-Refiner, Mind-CAD, bidirectional parametric sketches,
  and CADLoop.
- Understanding/evaluation: PP-Brep, real-world hole segmentation, LED-BENCH,
  CADWorld, and DeciCAD.
- Assembly/manufacturing: CAD-based relation learning and geometric-symbolic
  assembly planning; a STEP-grounded assembly-manual proof of concept.
- Software: `jdilla1277/agentcad`, `n3r/AgentCAD`, AgentSCAD, and nurb.
  The similarly named agentcad projects are separate repositories, not aliases.
- Assets/capabilities: Autodesk ABC-1M, ECCV CAD Challenge, Onshape AI Advisor,
  and NX X Manufacturing AI Make Machining Suggestion.

The HiCAD paper is unrelated to the existing MrXujiang/HiCAD software project.
The full paper title and primary URL keep the two identities separate.

## Corrections and evidence boundaries

Eight existing README records were updated: DualBrep, Flatten The Complex,
CME-CAD, CADFS, BrepGaussian, Linkify, DreamCAD, and earthtojake/text-to-cad.
Changes repair authors/venue/year/name information or refresh current tool scope.
Existing paraCAD, TraceCAD, and Chamfer resources were not added again.

Paper entries require a source with identifiable authors, task, and contribution;
they do not certify runnable code or public training/evaluation assets. Several
CVF/Elsevier direct requests returned HTTP 403; official indexed abstracts and
bibliographic metadata supported those entries. Full-text review is not claimed.
Other paper records were checked on arXiv or publisher abstract pages.
No paper experiment or third-party project was executed in this pass.

For the ECCV challenge, public training STEP files, public-test input paths,
evaluation examples, and the hosted evaluation route were inspected in its
dataset card. Official counts are 8,344 training samples and 927 public-test
inputs; private targets are not represented as public data. The release has
per-asset license restrictions, rather than one assumed blanket license.
ABC-1M is the processed Autodesk release, distinct from the original ABC paper.

## Deferred, excluded, and duplicate leads

| Candidate | Decision and reason |
|---|---|
| RealCADBench / `epsilonlee/RealCADBench-V1.0.sub` | Deferred: a concrete dataset lead was discovered, but its page returned HTTP 401; public availability and association could not be established. |
| `markov-ai/cad-environments` | Deferred: real task files and native-output paths are visible; reuse/license terms were not established during this pass. |
| `Ericcsr/OpenCADHarness` | Deferred from the open-source section: source, tests, and installation instructions exist, but no root license was found. |
| `autonomous-ai/openharness` | Deferred: connector transport failed before source inspection. |
| BRepAssembler | Deferred: author-page description exists, but the inspected page exposed no working paper/code links for this item. |
| Text2CSG / SelfSketch2CAD | Retained as journal leads: title-level discovery succeeded, but author/contribution metadata was not sufficiently verified for insertion in this pass. |
| IndustrialCAD-1400 | Excluded from this increment: the inspected abstract describes Blender geometry programs/scenes; editable CAD-native output was not established. |
| ParaCAD / TraceCAD / Chamfer | Existing entries; no duplicate addition. |
| nurb | Included as a source-available AI-native platform, explicitly FSL-1.1-MIT; not classified as open source. |
| CAD 100K car-damage results / EDA-only results | Excluded as outside the catalog's CAD-native scope. |

## Validation

New README entries and registry records were deduplicated against both sources
using arXiv ID, normalized title, source URL, and manual alias checks. All existing
README entries remain present; only the eight declared entries change content.
Metadata, badges, AGENTS counts, and validator expectations agree. The validator
uses sorted-file first-occurrence semantics for historical duplicate records.
`python3 scripts/validate_catalog.py` and `git diff --check` pass.

The new [maintenance source inventory](../maintenance_sources.json) and
[maintenance procedure](../maintenance_sources.md) make this broader discovery
coverage reusable for later updates. They do not create a scheduled automation.
