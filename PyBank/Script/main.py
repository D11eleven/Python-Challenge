#Module
# ref 2-8,2-9
import os
import csv

csvpath = os.path.join("..","Resources","budget_data.csv")

#Variables 
Total_Months = 0
PnL_Total = 0 

#Average_Change
# val2 -val1  = change
PnL_Value1 = 0
Total_PnL_Change = 0

#MAX_Increase_PNL
#MIN_Increase_PNL 
date = []
PnL_Change = []  

with open (csvpath, newline='', encoding='utf-8') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
# add encode and new line 2-12
    # print(csvreader)

#read header row first 2-8,3-1
#similar to vba assignment to assign value since no change for first entry
     csv_header = next(csvreader)
     first_row = next(csvreader)
     PnL_Value1 = int(first_row[1])
     date.append(first_row[0])
     
#read each row of data after header 2-8
     for row in csvreader:
         #print(row)

# extract and save data from each row into seperate lists 
#  Date[] & Profit/Losses (PnL[])  2-12 udemy     


# open the data file and start analysis



# Total Number of Months Included in the DataSet
# **  need beginning date and ending date; count, find difference(inclusive)
# number of rows - header (next does this) = number of months 
#one method to count months
#Total_Months = Total_Months + 1

# create list of months ; use len for number of entries >>>>  number of months 
          date.append(row[0])
          Total_Months =len(date)
#Put months in list 


# Net Total Amount of "Profit/Losses" over Entire Period
# **Sum PnL column
          PnL_Total = PnL_Total + int(row[1])


# Calculate the Changes in "PnL" over the Entire Period, 
# then Find the Average of those Changes
# ** Take Difference of Row I+1 and I and store as separate value for each row I; 
# ** then add those values and divide by number of entries   
          PnL_Value2 = int(row[1])
          change = PnL_Value2 - PnL_Value1

          #Total_PnL_Change = T
          PnL_Change.append(change)

          #def Average(value):
               #return sum(PnL_Change) / len(PnL_Change)

          Total_PnL_Change = Total_PnL_Change + change
          Average_Change = (Total_PnL_Change / (len(PnL_Change)))

                    
          PnL_Value1 = PnL_Value2


# The Greatest Increase in Profits (Date and Amount) over the Entire Period
# **Find MAX in PnL changes and match its date

          MAX_Increase_PNL = max(PnL_Change)
          MAX_Increase_Date = date[PnL_Change.index(MAX_Increase_PNL)]


# The Greatest Decrease in Profits (Date and Amount) over the Entire Period
# **Find MIN in PnL changes and match its date

          MIN_Increase_PNL = min(PnL_Change)
          MIN_Increase_Date = date[PnL_Change.index(MIN_Increase_PNL)]



# Print Results 

print (f"    Financial Analysis")
print (f"-------------------------------")
print (f"Total_Months: {Total_Months}")
print (f"Total:  ${PnL_Total}")
print (f"Average Change:  ${round(Average_Change)}")
print (f"Greatest Increase in Profits: {MAX_Increase_Date} (${MAX_Increase_PNL})")
print (f"Greatest Decrease in Profits: {MIN_Increase_Date} (${MIN_Increase_PNL})")




# Output Results to TXT FILE 

output_path = os.path.join( "..", "Analysis", "Analysis.txt")
with open(output_path, "w") as txtfile:


     txtfile.write (f"\n    Financial Analysis")
     txtfile.write (f"\n-------------------------------")
     txtfile.write (f"\nTotal_Months: {Total_Months}")
     txtfile.write (f"\nTotal:  ${PnL_Total}")
     txtfile.write (f"\nAverage Change:  ${round(Average_Change)}")
     txtfile.write (f"\nGreatest Increase in Profits: {MAX_Increase_Date} (${MAX_Increase_PNL})")
     txtfile.write (f"\nGreatest Decrease in Profits: {MIN_Increase_Date} (${MIN_Increase_PNL})")






# TXT File Format
# Financial Analysis
# Total Months: 86
# Total: $38382578
# Average Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
