# Architecture

## Objective
This repository is organized as a production-style pipeline project with clear execution scripts, configuration templates, and operational documentation.

## Standard Layout
- `configs/`: environment and runtime templates.
- `scripts/`: operational entrypoints such as bootstrap and pipeline runners.
- `docs/`: architecture and operations notes.
- Existing source and data directories are preserved to avoid breaking legacy workflows.

## Operational Flow
1. Run `./scripts/bootstrap.sh` to validate local tooling.
2. Run `./scripts/run_pipeline.sh` (or a mode argument where supported).
3. Review generated artifacts in repository output locations.

## Notes
- Current datasets are treated as example datasets.
- Existing notebooks remain supported as exploratory modules.
