# Catalog Entry Verification Summary

Audit date: 2026-05-30

## Scope

- README entries audited: 523
- External source: arXiv Atom API for arXiv-linked entries; HTTP status checks for non-arXiv paper links.
- Confidence is metadata confidence, not a claim that the paper is technically correct.

## Confidence Counts

| Confidence | Count |
|---|---:|
| high | 268 |
| medium | 206 |
| low | 49 |

## Top Review Reasons

| Reason | Count |
|---|---:|
| author_readme_unknown | 120 |
| author_mismatch | 91 |
| title_mismatch | 31 |
| non_arxiv_url_metadata_not_checked | 21 |
| missing_paper_url | 10 |
| year_mismatch | 8 |
| paper_url_check_blocked_or_transient | 4 |

## Catalog Flags

| Flag | Count |
|---|---:|
| None | 0 |

## Section Breakdown

| Section | High | Medium | Low |
|---|---:|---:|---:|
| 2D CAD and Drawing Intelligence | 60 | 27 | 7 |
| 3D CAD Generation and Reconstruction | 60 | 46 | 12 |
| CAD Representations and Foundations | 7 | 5 | 1 |
| CAD Understanding and Retrieval | 29 | 23 | 3 |
| Challenges and Future Directions | 17 | 0 | 0 |
| Datasets and Benchmarks | 20 | 19 | 7 |
| Foundational CAD AI Papers | 8 | 0 | 0 |
| Manufacturing-Aware Design | 13 | 28 | 4 |
| Simulation and Design Optimization | 24 | 33 | 8 |
| Surveys | 3 | 4 | 0 |
| Tools and Platforms | 27 | 21 | 7 |

## Next Step

Metadata confidence is fully cleared when `low=0` and `medium=0`. Review `catalog_flags` separately for curation issues such as deliberate cross-section duplicates.
