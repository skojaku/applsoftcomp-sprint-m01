# Phase 3: Documentation — Data Cleaning + Visualization Notes

## Goal
The goal of this project is to transform messy raw CSV files into a tidy merged dataset and create a visualization showing the relationship between child mortality (Y-axis) and GDP per capita (X-axis), with color indicating year.

---

## Data cleaning strategy (Phase 1)
### Inputs
- Raw datasets were provided in the `data/` folder (mortality + GDP).

### Cleaning approach
1. **Standardized column names and schema**
   - Ensured the final merged dataset uses consistent column meanings across sources.
   - Final columns: `geo`, `name`, `year`, `mortality_rate`, `gdpcapita`.

2. **Converted data types**
   - Converted `year` to an integer to support filtering and consistent plotting.

3. **Handled messy formatting**
   - Removed/cleaned non-data rows and formatting artifacts.
   - Ensured each observation corresponds to one country (`geo`) and one year.

### Merge logic
- The cleaned mortality and GDP datasets were merged into one tidy table keyed by:
  - `geo` (country code) and `year`
- Output saved to:
  - `data/preprocessed/merged_data.csv`

---

## Visualization choices (Phase 2)
### Plot design
- **Scatter plot** of:
  - **X-axis:** GDP per capita (`gdpcapita`)
  - **Y-axis:** child mortality rate (`mortality_rate`)
- **Color encodes year** to show how the relationship changes over time.

### Why this design?
- A scatter plot is the clearest way to show the relationship between two continuous variables.
- Coloring by year adds a time dimension without creating multiple separate plots.

### Output
- The plot is saved to:
  - `paper/figs/child_mortality_vs_gdp.png`

---

## Key insights
- There is a strong negative relationship: countries with higher GDP per capita generally have lower child mortality.
- The color progression suggests improvements over time (more recent years tend to be associated with lower mortality for many countries).
- The relationship is not perfectly linear, especially at lower GDP levels where mortality varies widely.

---

## How to reproduce
- Run the Phase 2 script to regenerate the figure:
  - `uv run python scripts/phase2_plot.py`
- The output figure should appear in `paper/figs/`.

