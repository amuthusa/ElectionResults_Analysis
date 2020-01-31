#the data we need to retrieve
#1. Total number of votes cast
#2. Complete list of all he candidates who received votes
#3. Percentage of votes each candidate won
#4. Total number of votes each candidate won
#5. Winner of the election based on popular vote
import csv
import os
from datetime import datetime

currentDateTime = datetime.now()
print(f"current date and time is {currentDateTime}")

#filename to be loaded
file_to_load = os.path.join("Resources", "election_results.csv")

#Initialize total vote counter
total_votes = 0

# Candidate Options
candidate_options = list()

# initialize a dictionary to story candidate and number of votes
candidate_votes = dict()

#open and read the file in this csv file
with open(file_to_load) as election_results:

    #ToDo: read teh data using reader for doing analysis
    election_results_reader = csv.reader(election_results)

    #get the headers from cvs file
    headers = next(election_results_reader)
    print(headers)

    #loop over each rows except headers
    for row in election_results_reader:
        #get the candidate name from the csv
        candidate_name = row[2]
        #add the unique candidate names to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #add entry to dictionary for the candidate with votes initialized
            candidate_votes[candidate_name] = 0
        #increment the candidate votes as we iterate through each row
        candidate_votes[candidate_name] += 1

        #increment total_votes for every row of record in csv
        total_votes += 1

print(candidate_votes)    
print (f"Total votes {total_votes}")

#to capture the winning candidate details
winning_candidate = ""
winning_votes_count = 0
winning_percentage_of_votes = 0

#Determine the percentage of votes for each candidate by looping through the counts
#1.Iterate through the list
candidates_summary = list()

for candidate in candidate_votes:
    #2.Retrive the vote count of a candidate
    votes = candidate_votes[candidate]
    #3.calculate the percentage of votes
    percentage_of_votes = (float(votes) / float(total_votes) ) * 100
    #4.Print the percentage of votes for each candidate
    candidates_summary.append(f"{candidate}: {percentage_of_votes:.1f}% ({votes:,})\n")

    #Determine winning candaodate, votes_count and percentage of votes
    #1. determine if votes is greater than winning_votes_count and percentage_of_votes is greater than winning_percentage_of_votes
    if (votes > winning_votes_count and percentage_of_votes > winning_percentage_of_votes):
        #set the current cndidate and votes and percentage_of_votes as winning cndidate
        winning_candidate = candidate
        winning_votes_count = votes
        winning_percentage_of_votes = percentage_of_votes

winning_candidate_summary = (
    f"-------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_votes_count:,}\n"
    f"Winning Percentage: {winning_percentage_of_votes:.1f}%\n"
)

print(winning_candidate_summary)
#filename to write the analysis
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open a file for writing
with open(file_to_save, 'w') as election_analysis:
    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------------------\n"
        f"Total Votes: {total_votes: ,}\n"
        f"-------------------------------------\n"
    )
    #write the total votes count to the file
    election_analysis.write(election_results)
    
    #write candidate summary with candidate name, percentage_votes and total number of votes they got
    for candidate_summary in candidates_summary:
        election_analysis.write(candidate_summary)
    #finally write the winning candidate details
    election_analysis.write(winning_candidate_summary)