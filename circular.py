import pandas as pd

# Read in the original CSV file
df = pd.read_csv("circular.csv")

# Group the data by state and calculate the sum for each column
grouped_df = df.groupby("State").sum()

# Write the grouped data to a new CSV file
grouped_df.to_csv("summed.csv", index=True)
