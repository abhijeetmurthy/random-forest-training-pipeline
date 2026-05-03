#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if command -v python3 >/dev/null 2>&1; then
  python3 --version
fi
if command -v java >/dev/null 2>&1; then
  java -version || true
fi
if command -v mvn >/dev/null 2>&1; then
  mvn -v | head -n 1
fi

echo "Bootstrap checks complete for $ROOT_DIR"
