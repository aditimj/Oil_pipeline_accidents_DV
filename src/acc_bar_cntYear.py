import pandas as pd

# read the CSV file into a pandas dataframe
df = pd.read_csv("year_acc_cnt.csv")

# group the dataframe by year and count the number of accidents in each group
count_by_year = df.groupby("Accident Year").size().reset_index(name="AccidentCount")

# rename the "AccidentYear" column to "Year"
count_by_year = count_by_year.rename(columns={"Accident Year": "Year"})

# save the result as a new CSV file
count_by_year.to_csv("yearCnt.csv", index=False)
