# Catalog Increment Review

Review date: 2026-07-27

## Scope

- Previous catalog maintenance boundary: 2026-05-30.
- Sources checked: arXiv and publisher metadata, official project pages, official vendor announcements, and public GitHub repositories.
- Curation boundary: parametric CAD, B-rep/CSG, engineering drawings, CAD agents, CAD-native benchmarks, and manufacturing-aware CAD loops. Pure mesh generation, generic 3D vision, generic BIM, and unreleased product promises were excluded.

## Result

| Decision | Count |
|---|---:|
| New work first published after 2026-05-30 | 28 |
| Earlier high-relevance omissions backfilled | 4 |
| Existing entries updated in place | 2 |
| Net new README entries | 32 |

The README catalog therefore moves from 523 to 555 entries. The historical JSONL registry remains at 638 deduplicated records because this maintenance slice updates the public curated catalog and does not rewrite the separately sourced registry snapshot.

## Added arXiv Records

`2606.01702`, `2606.05058`, `2606.05515`, `2606.06405`, `2606.07024`, `2606.07198`, `2606.13368`, `2606.16797`, `2606.16806`, `2606.17696`, `2606.21378`, `2606.30429`, `2606.31252`, `2606.31579`, `2607.01205`, `2607.02448`, `2607.04119`, `2607.05123`, `2607.05573`, `2607.05750`, `2607.08891`, `2607.11339`, `2607.12678`, `2607.17093`, `2607.18997`, `2607.20642`, `2607.21928`, `2605.30794`, `2605.19717`, `2605.10873`, and `2603.27448`.

The non-arXiv addition is the open-source Chamfer CAD agent harness. FllumaOne and its 100K dataset release are represented by one catalog entry rather than duplicated as a paper and a tool.

## In-Place Updates

- Replaced Pointer-CAD v1 (`2603.04337`) with Pointer-CAD v2 (`2606.29301`), which explicitly identifies itself as the successor version and changes the method and authors.
- Updated Dassault Systemes Virtual Companions to the vendor's 2026-07-23 availability announcement.

## Deferred or Excluded

- Onshape Labs: current early-access capabilities are rendering and simulation integration; the CAD agent, drawing checker, and FeatureScript MCP capabilities are still described as expected soon.
- SUFLECA (`2607.15058`): CAD-to-image pose alignment rather than CAD design representation, generation, or editing.
- CADAM: already present; recent activity did not define a distinct new catalog item.
- Early repositories without a durable release or sufficient public evidence remain candidates for a later maintenance cycle.
