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


#* The total number of votes cast



 # * A complete list of candidates who received votes

  #* The percentage of votes each candidate won

  #* The total number of votes each candidate won

  #* The winner of the election based on popular vote.

#from Taylor Stack
#def percent(x):
 #   num = x/total_votes
  #  percentage = "{:.2%}".format(num)
   # return(percentage)





# Print Results

# Print Results 

# print (f"    Election Results")
# print (f"-------------------------------")
# print (f"Total_Votes: {Total_Votes}")
# print (f"-------------------------------")
# print("candidate1: "  " (percentage candidate1) "   " (votes candidate1))
# print("candidate2: "  " (percentage candidate2) "   " (votes candidate2))
# print("candidate3: "  " (percentage candidate3) "   " (votes candidate3))
# print("candidate4: "  " (percentage candidate4) "   " (votes candidate4))
# print (f"-------------------------------")
# print("Winner:()")
# print (f"-------------------------------")



# print("   Election Results")
# print("----------------")
# print("Total Votes: ()")
# print("----------------"
# print(f"candidate1: "  " (percentage candidate1) "   " (votes candidate1))
# print(f"candidate2: "  " (percentage candidate2) "   " (votes candidate2))
# print(f"candidate3: "  " (percentage candidate3) "   " (votes candidate3))
# print(f"candidate4: "  " (percentage candidate4) "   " (votes candidate4))
# print("----------------"
# print(f"Winner:()")
# print("----------------") 




# Output Results to TXT FILE 

# output = open("Analysis.txt", "w")



# output_path = os.path.join( "..", "Analysis", "Analysis.txt")
# with open(output_path, "w") as txtfile:

#  #    txtfile.write(Analysis)


#       txtfile.write (f"\n    Financial Analysis")
#       txtfile.write (f"\n-------------------------------")
#       txtfile.write (f"\nTotal_Months: {Total_Months}")
#       txtfile.write (f"\n-------------------------------")
#       txtfile.write (f"\nTotal:  ${PnL_Total}")
#       txtfile.write (f"\nAverage Change:  ${Average_Change}")
#       txtfile.write (f"\nGreatest Increase in Profits: {MAX_Increase_Date} (${MAX_Increase_PNL})")
#       txtfile.write (f"\nGreatest Decrease in Profits: {MIN_Increase_Date} (${MIN_Increase_PNL})")
#       txtfile.write (f"\n-------------------------------") 
#       txtfile.wrint( )
#       txtfile.write (f"\n-------------------------------")
