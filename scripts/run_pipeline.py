#!/usr/bin/env python3
import os
import csv

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")


def describe_dataset(path):
    with open(path, newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return {"rows": 0, "cols": 0, "columns": []}
    header = rows[0]
    return {
        "rows": max(len(rows) - 1, 0),
        "cols": len(header),
        "columns": header[:6],
    }


def main():
    datasets = [
        os.path.join(DATA_DIR, "Iris.csv"),
        os.path.join(DATA_DIR, "Titanic.csv"),
        os.path.join(DATA_DIR, "winequality-red.csv"),
    ]

    print("Random Forest Training Pipeline - dataset smoke run")
    for dataset in datasets:
        if not os.path.exists(dataset):
            print(f"- Missing dataset: {dataset}")
            continue
        info = describe_dataset(dataset)
        print(f"- {os.path.basename(dataset)}: rows={info['rows']} cols={info['cols']} sample_cols={info['columns']}")

    print("Notebook examples are available under code/*.ipynb")


if __name__ == "__main__":
    main()
