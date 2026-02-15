import pandas as pd

# Read raw mortality data
mort = pd.read_csv("data/raw/child-mortality.csv")

# Convert wide format to tidy (long) format
mort_tidy = mort.melt(
    id_vars=["geo", "name"],
    var_name="year",
    value_name="mortality_rate"
)

# Save tidy output
mort_tidy.to_csv(
    "data/preprocessed/child_mortality_tidy.csv",
    index=False
)

print("Saved data/preprocessed/child_mortality_tidy.csv")

