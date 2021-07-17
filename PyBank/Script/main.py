#Module

import os
import csv


csvpath = os.path.join("..","Resources","budget_data.csv")
# # '..', 'Resources',

with open (csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')

     print(csvreader)

     csv_header = next(csvreader)
     print(f"CSV Header: {csv_header}")

     for row in csvreader:
         print(row)


# Total Number of Months Included in the DataSet
# **  need beginning date and ending date; count, find difference(inclusive)



# Net Total Amount of "Profit/Losses"("PnL") over Entire Period
# **Sum PnL column





# Calculate the Changes in "PnL" over the Entire Period, 
# then Find the Average of those Changes
# ** Take Difference of Row I+1 and I and store as separate value for each row I; 
# ** then add those values and divide by number of entries






# The Greatest Increase in Profits (Date and Amount) over the Entire Period
# **Find MAX in PnL and match its date


# The Greatest Decrease in Profits (Date and Amount) over the Entire Period
# **Find MAX in PnL and match its date



# Output to Txt File
















# TXT File Format
# Financial Analysis
# Total Months: 86
# Total: $38382578
# Average Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
