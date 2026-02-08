# M01 Sprint Documentation

## Data Cleaning

### Original Data Structure

The raw files had 301 columns: `geo,name,1800,1801,1802,...,2100`. Each year was a separate column. Afghanistan's mortality data looked like: `afg,Afghanistan,468.58,468.58,468.58,...`. Empty cells appeared in countries like Andorra for years before the 1950s.

### Transformation

We converted both files from wide to long format.

**Child Mortality:**
- Melted year columns into a single `year` column
- Moved values into `child-mortality` column
- Replaced empty cells with 0.0
- Final output: `geo, name, year, child-mortality` (58,695 rows)

**GDP Data:**
- Applied same transformation to year columns
- Moved values into `value` column
- Final output: `geo, name, year, value` (58,695 rows)

Both datasets now share `geo` and `year` columns for merging.

## Visualization Choices

### Implementation

We used matplotlib for visualization. We wrote `create_visualization.py` to read `data/preprocessed/data.csv` and create a scatter plot:
- X-axis: `gdpcapita`
- Y-axis: `mortality_rate`
- Colors: Year-based gradient 

The color calculation normalizes years to a 0-1 range. Older years (1800s) get more blue, newer years (2000s) get more green. The code loops through each row, calculates the hex color, and passes the color list to `plt.scatter()`.

We chose a scatter plot to show the relationship between GDP and mortality. Each point represents one country-year observation. The color gradient adds temporal information without requiring separate plots.


## Key Insights 

### Economic-Health Relationship

The data shows a clear inverse correlation between GDP and child mortality. Afghanistan in 1800 had mortality of 468.58 with GDP of 560.89. These baseline values represent high mortality and low economic output.

Historical data points (blue) cluster at low GDP and high mortality. Recent data points (green) spread across higher GDP and lower mortality ranges. This pattern demonstrates how economic development correlates with improved child health outcomes.

### Data Coverage The dataset contains 195 countries across 301 years, giving us 58,695 observations. Countries like Andorra show zeros for early years where we replaced missing data with 0.0. This happened because some nations didn't exist or keep records in the 1800s.

## Bottom Line

We turned two completely unusable wide-format CSV files into proper tidy data. Now instead of having 301 columns of years, we have one year column and actual data columns. This makes merging, filtering, and plotting actually possible. The visualization shows how economic development and child health are connected across the last 200+ years of global data.
