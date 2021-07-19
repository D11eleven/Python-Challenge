#Module

import os
import csv

csvpath = os.path.join("..","Resources","election_data.csv")


with open(csvpath) as csvfile:
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



# Print Results

# print("   Election Results")
# print("----------------")
# print("Total Votes: ()")
# print("----------------"
# print("candidate1: "  " (percentage candidate1) "   " (votes candidate1))
# print("candidate2: "  " (percentage candidate2) "   " (votes candidate2))
# print("candidate3: "  " (percentage candidate3) "   " (votes candidate3))
# print("candidate4: "  " (percentage candidate4) "   " (votes candidate4))
# print("----------------"
# print("Winner:()")
# print("----------------") 




# Results to TXT FILE

# output("  Election Results")
# output ("----------------"
# output("Total Votes: ()")
# output ("----------------"
# output("candidate1: "  " (percentage candidate1) "   " (votes candidate1))
# output("candidate2: "  " (percentage candidate1) "   " (votes candidate1))
# output("candidate3: "  " (percentage candidate1) "   " (votes candidate1))
# output("candidate4: "  " (percentage candidate1) "   " (votes candidate1))
# output ("----------------"
# output("Winner:()")
# output ("----------------")
