import pandas as pd

# read the CSV file into a pandas dataframe
df = pd.read_csv("monthNew.csv")

# group the dataframe by year and count the number of accidents in each group
count_by_year = df.groupby("Month").size().reset_index(name="AccidentCount")

# rename the "AccidentYear" column to "Year"
count_by_year = count_by_year.rename(columns={"Accident Month": "Year"})

# save the result as a new CSV file
count_by_year.to_csv("monthCnt.csv", index=False)
