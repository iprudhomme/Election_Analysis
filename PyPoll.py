#  The data we need to retrieve
#  1. Total number of votes cast
#  2. A complete list of candidates who received votes
#  3. Total number of votes each candidate received
#  4. Percentage of votes each candidate won
#  5. The winner of the election based on popular vote
import csv
import os

# Initialize the vote counter 
total_votes = 0 
# Initialize the candidate list
candidate_options = []
# Declare the empty candidate dictionary.
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and Analyze the data
    file_reader = csv.reader(election_data)

    # Get the headers from the first line in the file reader
    headers = next(file_reader) 

    for row in file_reader:
        #Add to the total vote count
        total_votes += 1 

        # Get the candidate name from each row
        candidate_name = row[2]
        
        
        if candidate_name not in candidate_options: 
            # Add the candidate name to the candidate options list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        
for candidate in candidate_options:
    votes = candidate_votes[candidate]
    vote_percentage = float(votes)/float(total_votes) *100
    print (f"Candidate: {candidate} Votes: {vote_percentage:.2f}% ({votes:,} votes)") 

    # Check if the current candidate's votes and percent are higher then the previous ones
    if winning_count < votes and winning_percentage < vote_percentage: 
        # Set the new winning count and percentages
        winning_count = votes 
        winning_percentage = vote_percentage
        # Set the winning candidate's name
        winning_candidate = candidate 

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# Using the open() function with the "w" mode we will write the data to the file
with open(file_to_save, "w") as outfile: 
    #Write some data to the file.
    outfile.write("Total Votes:" + str(total_votes))
  
  