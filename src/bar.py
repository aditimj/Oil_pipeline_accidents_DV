import pandas as pd

# Load the original CSV file
df = pd.read_csv('bar.csv')

# Group the data by the Operator Name column and sum the Liquid Recovery and Net Loss columns
grouped_df = df.groupby('Operator Name')[['Liquid Recovery (Barrels)', 'Net Loss (Barrels)']].sum().reset_index()

# Sort the data by the total Liquid Recovery in descending order and select the top 10 operators
top_operators = grouped_df.sort_values('Liquid Recovery (Barrels)', ascending=False).head(10)

# Save the top 10 operators and their total Liquid Recovery and Net Loss to a new CSV file
top_operators.to_csv('top_10_operators.csv', index=False)
