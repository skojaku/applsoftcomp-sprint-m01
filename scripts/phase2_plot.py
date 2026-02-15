import os
import pandas as pd
import matplotlib.pyplot as plt

# Make sure output folder exists
os.makedirs("paper/figs", exist_ok=True)

# Load merged tidy data
df = pd.read_csv("data/preprocessed/merged_data.csv")

# Ensure correct types
df["year"] = df["year"].astype(int)

# Optional: focus on modern period for readability
df = df[df["year"] >= 1960]

# Scatter plot: mortality (Y) vs GDP per capita (X), colored by year
plt.figure(figsize=(8, 6))
plt.scatter(
    df["gdpcapita"],          # <-- this matches your actual column name
    df["mortality_rate"],
    c=df["year"],
    alpha=0.7
)

plt.xlabel("GDP per Capita")
plt.ylabel("Child Mortality Rate")
plt.title("Child Mortality vs GDP per Capita")

# Save figure
plt.savefig("paper/figs/child_mortality_vs_gdp.png", dpi=300, bbox_inches="tight")
plt.show()

