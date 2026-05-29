# Catalog Entry Verification Summary

Audit date: 2026-05-29

## Scope

- README entries audited: 528
- External source: arXiv Atom API for arXiv-linked entries; HTTP status checks for non-arXiv paper links.
- Confidence is metadata confidence, not a claim that the paper is technically correct.

## Confidence Counts

| Confidence | Count |
|---|---:|
| high | 251 |
| medium | 209 |
| low | 68 |

## Top Review Reasons

| Reason | Count |
|---|---:|
| author_readme_unknown | 122 |
| author_mismatch | 98 |
| title_mismatch | 36 |
| missing_paper_url | 22 |
| non_arxiv_url_metadata_not_checked | 20 |
| year_mismatch | 8 |
| paper_url_check_blocked_or_transient | 4 |
| paper_url_error | 2 |

## Catalog Flags

| Flag | Count |
|---|---:|
| duplicate_arxiv_id | 64 |

## Section Breakdown

| Section | High | Medium | Low |
|---|---:|---:|---:|
| 2D CAD and Drawing Intelligence | 57 | 27 | 7 |
| 3D CAD Generation and Reconstruction | 49 | 46 | 12 |
| CAD Representations and Foundations | 6 | 8 | 1 |
| CAD Understanding and Retrieval | 26 | 25 | 5 |
| Challenges and Future Directions | 27 | 0 | 0 |
| Datasets and Benchmarks | 13 | 19 | 10 |
| Foundational CAD AI Papers | 8 | 0 | 0 |
| Manufacturing-Aware Design | 8 | 29 | 9 |
| Simulation and Design Optimization | 19 | 32 | 13 |
| Surveys | 3 | 2 | 2 |
| Tools and Platforms | 35 | 21 | 9 |

## Next Step

Metadata confidence is fully cleared when `low=0` and `medium=0`. Review `catalog_flags` separately for curation issues such as deliberate cross-section duplicates.
