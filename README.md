# Random Forest Training Pipeline

Generic training pipeline for tree-based classification, including notebook-driven experimentation.

## Pipeline Stages

1. Ingest: load tabular datasets from `data/` or `code/`.
2. Preprocess: clean and transform features (notebook/script workflow).
3. Train: build decision trees and random-forest ensembles.
4. Evaluate: compare model performance across datasets.
5. Document: capture experiments in notebooks and exported artifacts.

## Repository Layout

- `code/`: core Python functions and experiment notebooks.
- `data/`: reusable tabular example datasets.
- `images/`: supporting diagrams.

## Example Datasets (Current)

- `data/Iris.csv`
- `data/Titanic.csv`
- `data/winequality-red.csv`
- `code/phl_hec_all_confirmed.csv`
- `code/Cleaned_data1.csv`

## Notebook Examples (Current)

- `code/random forest from scratch.ipynb`
- `code/Data_Preprocessing.ipynb`
- `code/UE17CS303-ASSIGNMENT-026_110_139_208.ipynb`
- `code/UE17CS303-ASSIGNMENT-026_110_139_208 (2).ipynb`

## Script Modules

- `code/decision_tree_functions.py`
- `code/helper_functions.py`
