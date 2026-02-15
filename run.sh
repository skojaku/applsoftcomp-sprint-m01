#!/usr/bin/env bash
set -e

echo "Installing dependencies..."
uv sync

echo "Running Phase 1 data cleaning..."
uv run python scripts/clean_gdp.py
uv run python scripts/clean_phase1.py

echo "Merging datasets..."
uv run python scripts/merge_phase1.py

echo "Generating visualization..."
uv run python scripts/phase2_plot.py

echo "Pipeline complete."

