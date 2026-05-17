# Contributing to Awesome AI for CAD

Thank you for contributing! This list aims to be the most comprehensive resource for AI+CAD research.

## Adding a Paper

### Entry Format

```markdown
- **Paper Title** - Author1, Author2, Author3 et al.. *Venue Year*. [[Paper](URL)]
```

Rules:
- Use the official paper title (no abbreviations)
- List up to 3 authors, then "et al."
- Venue = conference/journal name + year (e.g., `*CVPR 2025*`, `*arXiv 2025*`)
- Link to arXiv when available; otherwise use DOI or official publisher URL
- Sort by year (newest first) within each subsection
- Run `python3 scripts/validate_catalog.py` before opening a PR

### Where to Place It

Choose the most specific subsection that fits. If unsure, open an issue to discuss.

| Category | Scope |
|---|---|
| 2D CAD and Drawing Intelligence | Symbol detection, drawing parsing, floor plans, P&ID, schematics |
| 3D CAD Generation and Reconstruction | Sequence models, diffusion, LLM-based, B-Rep/CSG generation |
| CAD Understanding and Retrieval | Feature recognition, retrieval, segmentation, representation learning |
| Simulation and Design Optimization | FEA surrogates, CFD, topology optimization, PINNs |
| Manufacturing-Aware Design | DFM, DFAM, assembly planning, CAD/CAM |
| Datasets and Benchmarks | New datasets, evaluation metrics, benchmark challenges |
| Tools and Platforms | Commercial tools, open-source frameworks, deployment research |

### Adding a Dataset

Place it under **Datasets and Benchmarks > Dataset Papers** with the same entry format.

## Reporting Issues

- **Dead link**: Open an issue with the paper title and broken URL
- **Wrong category**: Open an issue explaining the suggested move
- **Duplicate entry**: Open an issue pointing to both locations

## Pull Request Process

1. Fork the repository
2. Create a branch (`add/paper-name` or `fix/description`)
3. Make your changes following the format above
4. Run `python3 scripts/validate_catalog.py`
5. Submit a PR with a one-line description of what you added/fixed

PRs are typically reviewed within a few days.

## Code of Conduct

Be respectful. This is an academic resource — focus on the work, not the people.
