#Create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv

election_csv = os.path.join(os.path.dirname( __file__ ), "..","Resources","election_data.csv")

with open(election_csv, "r") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    total = 0
    candidates = []
    candidate1_votes = 0
    candidate2_votes = 0
    candidate3_votes = 0
    candidate4_votes = 0
    percent_of_votes = []
    votes_for_each  = []

    #The total number of votes cast
    #A complete list of candidates who received votes
    for row in csvreader:
        total += 1
        if row[2] not in candidates:
            candidates.append(row[2])


    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    with open(election_csv, "r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        for row in csvreader:
            if row[2] == candidates[0]:
                candidate1_votes += 1
            elif row[2] == candidates[1]:
                candidate2_votes += 1
            elif row[2] == candidates[2]:
                candidate3_votes += 1
            else:
                candidate4_votes += 1
        
        votes_for_each.append(candidate1_votes)
        votes_for_each.append(candidate2_votes)
        votes_for_each.append(candidate3_votes)
        votes_for_each.append(candidate4_votes)
        percent_of_votes.append(round(candidate1_votes/total*100,3))
        percent_of_votes.append(round(candidate2_votes/total*100,3))
        percent_of_votes.append(round(candidate3_votes/total*100,3))
        percent_of_votes.append(round(candidate4_votes/total*100,3))
        
        election_list = list(zip(candidates,percent_of_votes,votes_for_each))
        print(election_list)

        #The winner of the election based on popular vote.
        max_votes = max(percent_of_votes)
        for i in range(len(election_list)):
            if election_list[i][1] == max_votes:
                winner = election_list[i][0]
        

        print("Election Results")
        print("-------------------------")
        print(f"Total Votes: {total}")
        print("-------------------------")
        for i in range(len(candidates)):
            print(f"{candidates[i]}: {percent_of_votes[i]}% ({votes_for_each[i]})")
        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")

        #Write a txt file with results
        result_file = open("PyPoll/PyPoll_Results.txt","w+")
        print("Election Results",file = result_file)
        print("-------------------------",file = result_file)
        print(f"Total Votes: {total}",file = result_file)
        print("-------------------------",file = result_file)
        for i in range(len(candidates)):
            print(f"{candidates[i]}: {percent_of_votes[i]}% ({votes_for_each[i]})",file = result_file)
        print("-------------------------",file = result_file)
        print(f"Winner: {winner}",file = result_file)
        print("-------------------------",file = result_file)
        result_file.close()