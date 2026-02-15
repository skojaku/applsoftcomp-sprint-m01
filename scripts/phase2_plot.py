import pandas as pd
import matplotlib.pyplot as plt

# Load merged tidy data
df = pd.read_csv("data/preprocessed/merged_data.csv")

# Ensure correct types
df["year"] = df["year"].astype(int)

# Optional: focus on modern period for readability
df = df[df["year"] >= 1960]

# Create scatter plot
plt.figure()
plt.scatter(df["gdpcapita"], df["mortality_rate"], alpha=0.5)

plt.xlabel("GDP per capita")
plt.ylabel("Child mortality rate")
plt.title("Child Mortality vs GDP per Capita")

plt.show()

