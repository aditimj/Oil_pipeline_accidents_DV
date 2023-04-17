import pandas as pd

# Read in the original csv file
df = pd.read_csv('donut.csv')

# Create a pivot table to sum the number of liquid types for each year
pivot_table = pd.pivot_table(df, index='Year', columns='LiquidType', aggfunc='size', fill_value=0)

# Save the pivot table to a new csv file
pivot_table.to_csv('donut_final.csv')
