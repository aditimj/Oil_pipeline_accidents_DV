import pandas as pd

# read data into a pandas dataframe
df = pd.read_csv("heatmap.csv")

# group by Accident State and sum the Unintentional Release (Barrels)
grouped = df.groupby("Accident State")["Unintentional Release (Barrels)"].sum()

# sort the groups by the sum of unintentional release in descending order
sorted_groups = grouped.sort_values(ascending=False)

# take the top 5 states with the maximum unintentional release
top_states = sorted_groups.head(10)

# print the top 5 states with their sum of unintentional release
print(top_states)