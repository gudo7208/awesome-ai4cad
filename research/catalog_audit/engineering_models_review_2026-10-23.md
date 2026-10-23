# Engineering CAD/BIM models follow-up — 2026-10-23

## Scope and outcome

This pass follows the user's request to find work analogous to SKY-001, extending
beyond arXiv to model developers' research posts, commercial agent-native CAD/BIM
platforms, release notes, technical model cards, and evaluation reports. It
prioritizes current engineering generation/execution capability and backfills
older omissions exposed by these sources. It is not an exhaustive survey.

- 14 new README entries and 14 new registry records: seven papers, three
  research-preview/technical-blog reports, and four platform/workflow entries.
- Three existing entries enriched: Zoo → Zoo Design Studio/Zookeeper; MecAgent
  → V2; IndustryForge-27B → author-linked model card and actual weight listing.
- Live README entries: 644 → 658; registry records: 676 → 690; records dated
  2024–2026: 534 → 548. Existing registry snapshots remain unchanged.

## Additions and timing

SGS-1 is a September 2025 backfill. Shape and Ishigaki work are April–June 2026
backfills. Other explicitly dated work spans June–October 2026; do not describe
all additions as new this month. ClassCAD.ai and Adam Migrations have no verified
launch date in the reviewed pages; the 2026 label is a current review snapshot.

| Work | Publication/release evidence | Type | Source |
|---|---|---|---|
| Introducing SGS-1 | 2025-09-15 | research-preview | [Primary source](https://www.spectrallabs.ai/research/SGS-1) |
| A Turing Test for Physical Engineering | 2026-10-14 | technical-report | [Primary source](https://www.spectrallabs.ai/research/cswp-turing-test) |
| Quartz: CAD Software Built for Machine Intelligence | 2026-10-19 | technical-report | [Primary source](https://www.spectrallabs.ai/research/building-cad-for-machine-intelligence) |
| ClassCAD.ai | Undated; reviewed 2026-10-23 | platform | [Primary source](https://classcad.ai/) |
| Motif Design: Agent-Native BIM Modeling | 2026-09-09 | platform | [Primary source](https://motif.io/design/ai) |
| BIMLOGIQ Argus: CAD-to-MEP and Parametric Revit Modeling | 2026-09-12 | platform | [Primary source](https://bimlogiq.com/whats-new/september-2026) |
| Adam Parametric CAD Migrations | Undated; reviewed 2026-10-23 | platform | [Primary source](https://adam.new/migrations) |
| Shape: A Self-Supervised 3D Geometry Foundation Model for Industrial CAD Analysis | 2026-04-19 | paper | [Primary source](https://arxiv.org/abs/2604.22826) |
| BIMVLM: A vision-language model for iterative generation of component BIM models | 2026-06-10 | paper | [Primary source](https://doi.org/10.1016/j.eswa.2026.131765) |
| A Dual-Head Self-Reflective Framework for Text-to-CAD Generation | 2026-10-11 | paper | [Primary source](https://doi.org/10.1016/j.eswa.2026.134693) |
| Text2CSG: Generating CAD models from natural language via constructive solid geometry | 2026-10 | paper | [Primary source](https://doi.org/10.1016/j.cad.2026.104127) |
| Ishigaki-IDS: An Open-Weight Verifier-Aware Model for Information Delivery Specification Drafting in Building Information Modeling | 2026-06-07 | paper | [Primary source](https://arxiv.org/abs/2606.08545) |
| Ishigaki-IDS-Bench: A Benchmark for Generating Information Delivery Specification from BIM Information Requirements | 2026-05-21 | paper | [Primary source](https://arxiv.org/abs/2605.22079) |
| Assessing the CAD Capabilities of General-Purpose AI Models: A Case Study of GPT-6 Astra | 2026-10-17 | paper | [Primary source](https://arxiv.org/abs/2610.24451) |

## Important distinctions verified

- SGS-1's official blog links a Hugging Face Space. A demo is not a verified
  weight release, and a STEP part is not a native feature-tree history.
- SGS-Mk2 is a model orchestrated by a VLM through Quartz tools. Its technical
  report distinguishes 45 internal QA tasks from the live CSWP certification;
  the QA sampling criterion is not identical to single-answer timed exams.
  The report discloses a local answer-store flaw and says live certification
  agents had no shell, file, or database access. Claims remain vendor-reported.
- Quartz's October 19 report describes an execution/training environment built
  around a commercial kernel. Public self-serve availability and model weights
  were not verified. It is cataloged as a technical report, not an open tool.
- ClassCAD.ai has inspectable packages, MCP integration, scripts and tests.
  Repository-wide license metadata is absent; its underlying engine has separate
  licensing. The public site distinguishes free private/evaluation usage from
  commercial plans and plan-dependent exports. No open-source-engine claim.
- Motif Design access is mediated by the team, separately licensed from Motif
  Review; the help center says no self-serve trial or in-app upgrade path.
- Argus September 12 releases describe DWG/DXF-to-Revit MEP generation and room
  fit-out. Product output and compliance checks were not independently run.
- Adam Migrations describes stepwise geometry checking and destination history
  reconstruction, subject to representative-model review. It does not establish
  arbitrary feature support across every named source/destination pairing.
- Shape is representation/analysis work, not CAD program generation; its README
  says supervised task heads are disabled in this release. The associated
  repository, README, license metadata and source tree were inspected.
- Ishigaki-IDS generates standards-based BIM requirements, not 3D geometry.
  The 8B card declares CC BY 4.0 but requires contact-sharing agreement for file
  access. The gate was not crossed; the paper and public card are evidence.
- Text2CSG was deferred in the earlier sweep for incomplete metadata. Official
  indexed author/title/DOI evidence now resolves that gap; its promised code/data
  release remains unverified and is not linked as an available asset.
- Direct Elsevier page extraction failed (403 or inaccessible DOI redirect).
  Official indexed bibliographic metadata, abstracts and highlights were used for
  Text2CSG, BIMVLM and the dual-head paper. Full-text review is not claimed.
- MecAgent's own release log dates V2.0.0 to September 30 and October 7 to later
  patches. Use the primary dates rather than copying the press coverage.
- Zoo's October 8 KCL 3 post describes improved operations; its KCL 4 assembly
  constraints are roadmap. Zookeeper updates the existing product entry.
- IndustryForge's author-linked model repository has 12 Safetensors shards and
  an Apache-2.0 declaration. Its card and paper use different base-model names;
  leave that unresolved rather than inventing reconciliation. Public files were
  inspected but not downloaded; no inference was run.

## Deduplication and unresolved scope

[Candidate ledger](engineering_models_candidates_2026-10-23.json) preserves every
addition, update, primary URL, availability observation, and limitation.
VisCAD, IndustryForge, Arko-T, CADReasoner, CADENA, Backflip, and SKY-001 were already
present. Their rediscovery is not counted as a new addition. VisCAD-M1's author-
associated downloadable weights were not verified; no model URL was guessed.
Generic mesh generators and CAD software without a concrete learned CAD/BIM
contribution are not added merely to increase coverage counts.

## Validation

`python3 scripts/validate_catalog.py` and `git diff --check` passed. New titles,
arXiv IDs and source URLs were checked against README and historical JSONL inputs.
No downloaded model/project was executed, no paid access was purchased, and no
vendor performance result was independently reproduced.
