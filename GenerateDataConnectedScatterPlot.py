import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('oil.csv')

# Group the DataFrame by year and sum the net loss values for each year
yearly_totals = df.groupby('Accident Year')['Net Loss (Barrels)'].sum()

# Create a new DataFrame with two columns: "Year" and "SUM(Net Loss (Barrels))"
new_df = pd.DataFrame({'Year': yearly_totals.index, 'value': yearly_totals.values})

# Save the new DataFrame to a new CSV file
new_df.to_csv('yearly_net_loss_totals.csv', index=False)