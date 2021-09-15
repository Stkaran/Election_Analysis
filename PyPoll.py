# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Getting Candidate Names
candidate_options = []
# Vote count with name as key and votes as value
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Grab 3rd value in each row
        candidate_name = row[2]
        # Add to name list and check if already there 
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            # Track vote count based on name
            candidate_votes[candidate_name] = 0

         # Add 1 each time name appears
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]
        percent_of_vote = float(votes)/ float(total_votes) * 100
        
        print(f"{candidate_name}: {percent_of_vote:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (percent_of_vote > winning_percentage):
            winning_count = votes
            winning_percentage = percent_of_vote
            winning_candidate = candidate_name

    winning_candidate_results = (
        f"--------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}\n"
        f"--------\n")

    print(winning_candidate_results)

    