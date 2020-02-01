#creates a list with county based summary and largest voter turnout county details
def getConsolidatedCountySummary(county_votes):
    largest_turnout_county = ""
    largest_vote = 0

    #Determine the percentage of votes by each county
    #1. Initialize the county_summary
    counties_summary = list()
    #write the county based voter turnout header
    county_header = f"\nCounty Votes:\n"
    counties_summary.append(county_header)

    summary = ""
    #2. Iterate through county list
    for county in county_votes:
        #3. Retrieve the vote count by count
        county_vote = county_votes[county]
        #4. Calculate teh percentage of votes 
        county_percentage_votes = (float (county_vote) / float (total_votes)) * 100
        #5. Create a county based summary with percentage of vote cast and total votes cast
        summary = f"{county}: {county_percentage_votes:.1f}% ({county_vote:,})\n"
        counties_summary.append(summary)
        #6.find the county with largest vote cast for the election
        if (county_vote > largest_vote):
            largest_vote = county_vote
            largest_turnout_county = county

    #write the count with largest turnout for this election
    largest_turnout = (
        f"\n-------------------------------------\n"
        f"Largest County Turnout: {largest_turnout_county}"
        f"\n-------------------------------------\n"
    )
    counties_summary.append(largest_turnout)
    return counties_summary

#creates consolidated summary for candidates and winning candidates details
def getConsolidateCandidateSummary(candidate_votes):
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

    
    # create winning candidate summary
    winning_candidate_summary = (
        f"-------------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_votes_count:,}\n"
        f"Winning Percentage: {winning_percentage_of_votes:.1f}%\n"
    )
    #add winnning candidate summary to candidate summary to make it consolidated summary
    candidates_summary.append(winning_candidate_summary)

    return candidates_summary



#the data we need to retrieve
#1. Total number of votes cast
#2. Complete list of all he candidates who received votes
#3. Percentage of votes each candidate won
#4. Total number of votes each candidate won
#5. Winner of the election based on popular vote
#6. Find the voter turnout for each county
#7. Determine the percentage of votes cast by each county
import csv
import os

#filename to be loaded
file_to_load = os.path.join("Resources", "election_results.csv")

#Initialize total vote counter
total_votes = 0

# Candidate Options
candidate_options = list()

# Unique list of county
county_options = [] 

# initialize a dictionary to store candidate and number of votes
candidate_votes = dict()

#initialize a dictionary to store county wise number of votes
county_votes = dict()

#open and read the file in this csv file
with open(file_to_load) as election_results:

    #ToDo: read teh data using reader for doing analysis
    election_results_reader = csv.reader(election_results)

    #get the headers from cvs file
    headers = next(election_results_reader)

    #loop over each rows except headers
    for row in election_results_reader:
        #get the candidate name from the csv
        candidate_name = row[2]
        #get the county name from the csv
        county_name = row[1]
        #add the unique candidate names to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #add entry to dictionary for the candidate with votes initialized
            candidate_votes[candidate_name] = 0
        #add the unique county name to the list if its new county
        if county_name not in county_options:
            county_options.append(county_name)
            #add entry to dictionary for county based vote count
            county_votes[county_name] = 0

        #increment the candidate votes as we iterate through each row
        candidate_votes[candidate_name] += 1
        #increment the vote count for the county
        county_votes[county_name] += 1

        #increment total_votes for every row of record in csv
        total_votes += 1

consolidated_counties_summary = getConsolidatedCountySummary(county_votes)
consolidated_candidates_summary = getConsolidateCandidateSummary(candidate_votes)

#filename to write the analysis
file_to_save = os.path.join("analysis", "election_analysis_challenge.txt")

#open a file for writing
with open(file_to_save, 'w') as election_analysis:
    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------------------\n"
        f"Total Votes: {total_votes: ,}\n"
        f"-------------------------------------\n"
    )
    print(election_results)
    #write the total votes count to the file
    election_analysis.write(election_results)
    
    
    #write county summary with county name, percentage_votes and total number of voter turnout
    #write the count with largest turnout for this election
    for county_summary in consolidated_counties_summary:
        print(county_summary)
        election_analysis.write(county_summary)

    #write candidate summary with candidate name, percentage_votes and total number of votes they got
    #finally write the winning candidate details
    for candidate_summary in consolidated_candidates_summary:
        print(str(candidate_summary))
        election_analysis.write(candidate_summary)
    