# ICU Sentinel

Multimodal deep learning system for early sepsis risk assessment in ICU patients.

## Mission

ICU Sentinel predicts whether a patient will develop sepsis within a future
prediction horizon, given a fixed observation window of physiological,
laboratory, and demographic data.

## Project Structure

- `src/icu_sentinel/` - core package (data, features, models, training, evaluation, interpretability, utils)
- `configs/` - experiment and task configuration files
- `data/` - raw, processed, and windowed datasets (not tracked in git)
- `experiments/` - experiment outputs and results
- `notebooks/` - exploratory analysis
- `tests/` - unit and integration tests
- `docs/` - architecture, data pipeline, experiments, model cards

## Status

Project foundation phase - repository skeleton, package scaffolding, and
configuration setup. No models implemented yet.

## Roadmap

See `ICU_Sentinel_Project_ROADMAP.md` for the full phase-by-phase plan.
