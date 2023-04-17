import pandas as pd


# Load the data from a CSV file
data = pd.read_csv("updatedheat.csv")

# Group the data by year and state, and sum the unintentional release barrels
grouped_data = data.groupby(["Accident Year", "Accident State"])["Unintentional Release (Barrels)"].sum().reset_index()

# Rename the columns
grouped_data.columns = ["Year", "State", "UnintentionalReleaseBarrels"]

# Save the grouped data to a new CSV file
grouped_data.to_csv("finalHeat.csv", index=False)

