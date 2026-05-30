# Agent Guide for Awesome AI for CAD

This repository is a curated AI+CAD research catalog.
Optimize for evidence, reproducibility, and small diffs.

## Start Here

1. Read `README.md` for the public catalog and navigation.
2. Read this file before making maintenance changes.
3. Use `scripts/validate_catalog.py` before and after editing catalog metadata.
4. Treat `research/papers/*.jsonl` and `README.md` as catalog inputs.
5. Treat `research/catalog_audit/` as the catalog-confidence evidence trail.

## Source of Truth

| Artifact | Purpose | Notes |
|---|---|---|
| `README.md` | Public catalog and human navigation | Contains 552 Markdown catalog entries. |
| `research/papers/*.jsonl` | Machine-readable registry | Deduplicates to 638 unique records in the current snapshot. |
| `research/catalog_audit/` | Catalog confidence audit | Documents per-entry verification status and manual source checks. |

## Data Confidence Contract

- Use exact counts only when they are directly reproducible from local files or a cited external source.
- Do not describe the catalog with an undefined rounded paper count. Use:
  - `552 Markdown catalog entries`
  - `638 deduplicated JSONL registry records`
- Do not introduce projected counts, inferred percentages, or market/workflow statistics without a source and a note about the denominator.
- If a number comes from an individual paper and has not been independently checked, phrase it as a reported result.

## Maintenance Commands

Run the catalog validator:

```bash
python3 scripts/validate_catalog.py
```

## Editing Rules

- Keep changes surgical. Do not reorder large catalog sections unless the task is explicitly taxonomy cleanup.
- Preserve the entry format: `- **Title** - Authors. *Venue Year*. [[Paper](URL)]`.
- Prefer arXiv links when available; otherwise use DOI, publisher, or official project URLs.
- Avoid local absolute paths.
- Do not commit cache directories, virtual environments, or generated Python bytecode.
