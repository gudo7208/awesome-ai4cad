# Multi-source CAD catalog maintenance

The machine-readable source inventory is [maintenance_sources.json](maintenance_sources.json).
Use this inventory for future maintenance. An arXiv keyword sweep alone is not
adequate coverage of this catalog.

## Discovery passes

1. Search arXiv by task and representation, including abstracts and category/month
   listings. Separate B-rep, CAD programs, sketches/constraints, editing, assembly,
   drawings, manufacturing, and evaluation; do not use only `text-to-CAD`.
2. Review official conference programs and proceedings. Check CVPR workshops as
   well as the main conference; inspect ECCV and SIGGRAPH programs, publishers,
   and author pages for material indexed late or without an arXiv record.
3. Review Computer-Aided Design and Computer Aided Geometric Design publisher
   indexes. DOI and abstract metadata can qualify a paper even if full text is
   paywalled. Explicitly record whether full text was inspected.
4. Follow active authors' and labs' publication pages to official projects, code,
   model weights, and datasets. Follow references from newly verified papers.
5. Search GitHub repositories and topics independently of paper discovery. Include
   `FreeCAD`, `CadQuery`, `build123d`, `OpenSCAD`, `BRep`, `STEP`, `CAD MCP`,
   `CAD harness`, and `CAD agent`. Search both recently created and recently
   updated repositories; stars and README claims are not quality certificates.
6. Review Hugging Face dataset/model cards and file listings. Verify the uploader,
   available splits/files, task definition, evaluation access, and license notes.
7. Read first-party CAD/CAM vendor release notes. Distinguish available features,
   beta access, demos, and roadmap claims; record concrete native-CAD capability.
8. Diff specialist curated lists and use DBLP/Crossref-style indexes to discover
   omissions, then verify candidates against first-party sources.

## Scope and evidence

- Prioritize the interval after the previous maintenance boundary, with indexing
  overlap. Also backfill older current-year work exposed by new source families.
  Report backfills separately from claims of newly published work.
- Include editable CAD, B-reps, CSG/programs, sketches/constraints, CAD-native
  drawings/assemblies, manufacturing workflows, and domain-specific evaluation.
  A CAD acronym, a generic mesh generator, or EDA-only content is insufficient.
- A paper entry and a runnable asset have different evidence requirements.
  Record an accessible paper without claiming code/data availability. Link code
  only after inspecting its actual repository and its association with the work.
- For software, inspect source paths, package/installation information, examples
  or tests, and the license. Do not classify source-available licenses as open
  source. Do not execute downloaded projects solely to curate the catalog.
- Deduplicate by unversioned arXiv ID, DOI, normalized title, and project URL.
  Check both README and the historical JSONL registry. Use aliases to avoid
  duplicates when a paper title differs from its model/framework name.
- Keep an auditable candidate ledger: discovery source, primary source,
  decision, reason, limitations, and review date. Revisit deferred records when
  an official asset release or missing metadata becomes available.
- Recompute counts with the repository validator's sorted-file, first-occurrence
  deduplication semantics. Historical duplicate records may disagree on year;
  counting any occurrence in a year range gives a different denominator.

## Verification limits

Publisher search snapshots can expose official bibliographic metadata and an
abstract when a direct page fetch returns HTTP 403. Record that limitation;
do not claim full-text review. A source-level curation check is not independent
reproduction of a paper's reported results or a product's reliability.

No single source family, query, or pass establishes exhaustive coverage. Report
the actual source families checked and preserve unresolved gaps.
