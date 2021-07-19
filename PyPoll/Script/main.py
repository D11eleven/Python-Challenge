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
