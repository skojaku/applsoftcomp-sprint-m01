import pandas as pd
import os

os.makedirs("data/preprocessed", exist_ok=True)

mortality = pd.read_csv("data/raw/child-mortality.csv")

mortality_tidy = mortality.melt(
    id_vars=["geo", "name"],
    var_name="year",
    value_name="mortality_rate"
)

mortality_tidy.to_csv(
    "data/preprocessed/mortality_tidy.csv",
    index=False
)

print("Saved data/preprocessed/mortality_tidy.csv")


