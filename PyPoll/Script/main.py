#Module

import os
import csv

csvpath = os.path.join("..","Resources","election_data.csv")

#Variables, Lists, Dictionaries

Total_Votes = 0

Candidate_List = []

with open(csvpath, newline='', encoding='utf-8') as csvfile:

  csvreader = csv.reader(csvfile, delimiter=',')

     #print(csvreader)

  csv_header = next(csvreader)
     #print(f"CSV Header: {csv_header}")

  for row in csvreader:
         #print(row)print(f"    Election Results")


      Total_Votes = Total_Votes + 1


print(f"-------------------------------")
print(f"Total_Votes: {Total_Votes}")
print(f"-------------------------------")
# print("candidate1: "  " (percentage candidate1) "   " (votes candidate1))
# print("candidate2: "  " (percentage candidate2) "   " (votes candidate2))
# print("candidate3: "  " (percentage candidate3) "   " (votes candidate3))
# print("candidate4: "  " (percentage candidate4) "   " (votes candidate4))
# print(f"-------------------------------")
# print("Winner:()")
# print(f"-------------------------------")

# Output Results to TXT FILE 

output_path = os.path.join( "..", "Analysis", "Analysis.txt")
with open(output_path, "w") as txtfile:

#  #    txtfile.write(Analysis)

  txtfile.write(f"\n    Financial Analysis")
  txtfile.write(f"\n-------------------------------")
  txtfile.write(f"\nTotal_Votes: {Total_Votes}")
  txtfile.write(f"\n-------------------------------")
#       txtfile.write (f"\nTotal:  ${PnL_Total}")
#       txtfile.write (f"\nAverage Change:  ${Average_Change}")
#       txtfile.write (f"\nGreatest Increase in Profits: {MAX_Increase_Date} (${MAX_Increase_PNL})")
#       txtfile.write (f"\nGreatest Decrease in Profits: {MIN_Increase_Date} (${MIN_Increase_PNL})")
  txtfile.write(f"\n-------------------------------") 
#       txtfile.wrint( )
  txtfile.write(f"\n-------------------------------")


#* The total number of votes cast

#Total_Votes = Total_Votes + 1

# * A complete list of candidates who received votes
 #Run through loop to append candidate name that is not in Candidate_List
 # Candidate_List[]
 # vote  county  candidate
 # if row [2] not in Candidate_List:
 #    Candidate_List.append(row[2])
   # else .... 


  #* The percentage of votes each candidate won
#  sum each candidates votes then divide by Total_Votes put in % format(*100) store
#  dictionary ?     {"CandidateX": "candidateX_Votes", ...}

  #* The total number of votes each candidate won
# append each CandidatesX_Votes

  #* The winner of the election based on popular vote.
   # The Max of CandidateX_Votes is Winner
   # need to display each candidates name, percentage of votes, total votes 


   #

#    Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------


#from Taylor Stack
#def percent(x):
 #   num = x/total_votes
  #  percentage = "{:.2%}".format(num)
   # return(percentage)

