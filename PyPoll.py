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

#open and read the file in this csv file
with open(file_to_load) as election_results:

    #ToDo: read teh data using reader for doing analysis
    election_results_reader = csv.reader(election_results)

    headers = next(election_results_reader)
    print(headers)
    for row in election_results_reader:
        print(row)
    

#filename to write the analysis
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open a file for writing
with open(file_to_save, 'w') as election_analysis:
    
    #ToDo: write the ananlysis to the file
    election_analysis.write("Counties in the election\n")
    election_analysis.write("-----------------------------\n")
    election_analysis.write("Arapahoe \nDenver \nJefferson")