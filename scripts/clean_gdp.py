import pandas as pd

gdp = pd.read_csv("data/raw/gdp-data.csv")

gdp_tidy = gdp.melt(
    id_vars=["geo", "name"],
    var_name="year",
    value_name="gdpcapita"
)

gdp_tidy.to_csv("data/preprocessed/gdp_tidy.csv", index=False)
print("Saved data/preprocessed/gdp_tidy.csv")


