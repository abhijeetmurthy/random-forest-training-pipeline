#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if ! python3 - <<'PY'
import importlib.util
if importlib.util.find_spec("polars") is None:
    print("Warning: polars not installed; runner will use slower csv fallback.")
PY
then
  true
fi

python3 scripts/run_pipeline.py
