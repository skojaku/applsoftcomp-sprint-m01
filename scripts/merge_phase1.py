import pandas as pd

mort = pd.read_csv("data/preprocessed/child_mortality_tidy.csv")
gdp = pd.read_csv("data/preprocessed/gdp_tidy.csv")

# make sure year matches
mort["year"] = mort["year"].astype(int)
gdp["year"] = gdp["year"].astype(int)

merged = mort.merge(
    gdp,
    on=["geo", "name", "year"],
    how="inner"
)

merged.to_csv(
    "data/preprocessed/merged_data.csv",
    index=False
)

print("Saved data/preprocessed/merged_data.csv")

