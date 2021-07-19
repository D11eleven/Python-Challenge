#Module
# ref 2-8,2-9
import os
import csv


csvpath = os.path.join("..","Resources","budget_data.csv")
# # '..', 'Resources',

with open (csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
# add encode and new line?
     print(csvreader)

#read header row first 2-8
     csv_header = next(csvreader)
     print(f"CSV Header: {csv_header}")
#read each row of data after header 2-8
     for row in csvreader:
         print(row)


#Total_Months
#Total
#Average_Change
#MAX_Increase_PNL
#MIN_Increase_PNL 
# months
# pnl         


# Total Number of Months Included in the DataSet
# **  need beginning date and ending date; count, find difference(inclusive)



# Net Total Amount of "Profit/Losses"("PnL") over Entire Period
# **Sum PnL column





# Calculate the Changes in "PnL" over the Entire Period, 
# then Find the Average of those Changes
# ** Take Difference of Row I+1 and I and store as separate value for each row I; 
# ** then add those values and divide by number of entries  ???
#  need clarification 






# The Greatest Increase in Profits (Date and Amount) over the Entire Period
# **Find MAX in PnL changes and match its date


# The Greatest Decrease in Profits (Date and Amount) over the Entire Period
# **Find MIN in PnL changes and match its date



# Print Results 

#print ("    Financial Analysis")
#print ("-------------------------------")
#print ("Total_Months: xxxx")
#print ("Total: xxxxxxxxxx")
#print ("Average Change: $ xxxxxxxxxxxx")
#print ("Greatest Increase in Profits: (xxxxxxxx))
#print ("Greatest Decrease in Profits: (xxxxxxxxxx))



# Output Results to TXT FILE 

#output_path = os.path.join("..", "Resources", "Analysis.txt")
#with open(output_path, "w", newline='') as csvfile
#from 2-10

#output ("    Financial Analysis")
#prvvvvnt ("-------------------------------")
#prvvvint ("Total_Months: xxxx")
#pvvvrint ("Total: xxxxxxxxxx")
#prvvvint ("Average Change: $ xxxxxxxxxxxx")
#prvvvint ("Greatest Increase in Profits: (xxxxxxxx))
#pvvvvrnt ("Greatest Decrease in Profits: (xxxxxxxxxx))
















# TXT File Format
# Financial Analysis
# Total Months: 86
# Total: $38382578
# Average Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
