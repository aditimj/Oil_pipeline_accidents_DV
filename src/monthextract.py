import csv
from datetime import datetime


# open the input CSV file
with open('month.csv', 'r') as infile:
    reader = csv.reader(infile)
    # skip the header row
    next(reader)
    
    # open the output CSV file and write the header row
    with open('monthNew.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Month'])
        
        # iterate over the input rows, extract the month information, and write to the output file
        for row in reader:
            # parse the date string into a datetime object and extract the month information
            month = datetime.strptime(row[0], '%m/%d/%y %H:%M').strftime('%m')
            # write the month information to the output file
            writer.writerow([month])
