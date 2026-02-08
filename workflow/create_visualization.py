import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('data/preprocessed/data.csv')

x = data['gdpcapita'].to_list()
y = data['mortality_rate'].to_list()
years = data['year'].to_list()
year_range = max(years)-min(years)
colors = []

for index,row in data.iterrows():
    year_percent = (row['year'] - min(years)) / year_range
    g_num = 255*year_percent
    b_num = 255 - 255*year_percent
    g_hex = "{:02x}".format(g_num)
    b_hex = "{:02x}".format(b_num)
    colors.append('#00'+g_hex+b_hex)

plt.scatter(x, y, c=colors)
plt.xlabel("GDP Per Capita")
plt.ylabel("Child Mortality Rate")
