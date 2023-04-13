import pandas as pd

# Read in the original CSV file
df = pd.read_csv("oil.csv")

# Select the columns you want to keep
selected_columns = ["Year","Property Damage Costs", 'Lost Commodity Costs', 'Public/Private Property Damage Costs','Emergency Response Costs','Environmental Remediation Costs','All Costs']

# Create a new dataframe with only the selected columns
new_df = df[selected_columns]

# Group the data by state and calculate the sum for each column
grouped_df = new_df.groupby("Year").sum()

# Write the grouped data to a new CSV file
grouped_df.to_csv("areaData.csv", index=True)