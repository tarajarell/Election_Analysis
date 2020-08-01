
# Write down the names of all the candidates.
# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.

# Open the data file/add our dependencies.
import csv
import os

# Assign a variable for the file to load from a path (3.4.2)
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path (3.4.2)
flie_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file (3.4.2)
with open(file_to_load) as election_data:

    #Read the CSV
    csvread = csv.reader(election_data, delimiter=',')

    #Read the first row as header
    csv.header = next(csvread)

    #Establish values for all candidates at once
    candidate_options = []
    candidate_votes = {}


#Using the opan()function with the "w" mode we will write data to the file
with open(file_to_save, "w") as txt_file
    