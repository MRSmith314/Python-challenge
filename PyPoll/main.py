# Import Dependencies
import os
import csv

# Specify path to csv data file
poll_data = os.path.join("Resources", "election_data.csv")
output_results = os.path.join("analysis", "PyPoll_results.txt")

# Define variables for calculating and holding values
total_votes = 0           # Start count for total number of votes
candidate_votes = {}      # Dictionary for candidate votes each candidate received
candidates = []           # List of candidates
winning_candidate = ""
winning_count = 0         # Winning count tracker

# Open and read in csv data excluding header
with open(poll_data) as data:
    reader = csv.reader(data, delimiter=",")
    header = next(reader)

# Loop to calculate votes and candidates
    for row in reader:
        total_votes = total_votes + 1    # Adds to the total vote count
        candidate_name = row[2]          # Retrieve candidate names

        if candidate_name not in candidates:
            candidates.append(candidate_name)   # Add the name to the candidates list
            candidate_votes[candidate_name] = 0     # Track the candidate votes
        # Add vote to each candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(output_results, "w") as results_file:
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")

# Print Total Votes
    print(election_results, end="")
    results_file.write(election_results)

# Loop to retrieve vote count and percentage
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percent_votes = float(votes) / float(total_votes) * 100

# Retrieve winning vote count and winning candidates
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
        vote_results = f"{candidate}: {percent_votes:.3f}% ({votes})\n"

# Print Candidate Results
        print(vote_results, end="")
        results_file.write(vote_results)

    winning_candidate_summary = (
        f"---------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"---------------------------------\n")
# Print Winner
    print(winning_candidate_summary)
    results_file.write(winning_candidate_summary)
    