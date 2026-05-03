# Random Forest Training Pipeline

Enterprise-style ML repository for decision tree/random forest experimentation with script and notebook workflows.

## Structure
- `code/`: algorithm helpers and notebooks.
- `data/`: reusable example datasets.
- `scripts/run_pipeline.py`: scripted smoke pipeline over datasets.
- `scripts/run_pipeline.sh`: shell entrypoint.
- `configs/`, `docs/`: operational scaffolding.

## Quickstart
```bash
./scripts/bootstrap.sh
python3 -m pip install pandas
./scripts/run_pipeline.sh
```

## Notebook Examples
- `code/random forest from scratch.ipynb`
- `code/Data_Preprocessing.ipynb`
- `code/UE17CS303-ASSIGNMENT-026_110_139_208.ipynb`

## Example Datasets
- `data/Iris.csv`
- `data/Titanic.csv`
- `data/winequality-red.csv`
