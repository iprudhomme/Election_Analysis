#  The data we need to retrieve
#  1. Total number of votes cast
#  2. A complete list of candidates who received votes
#  3. Total number of votes each candidate received
#  4. Percentage of votes each candidate won
#  5. The winner of the election based on popular vote
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read and Analyze the data
    file_reader = csv.reader(election_data)

    for row in file_reader:
        print(row[0])


    # Using the open() function with the "w" mode we will write the data to the file
    with open(file_to_save, "w") as outfile: 
        #Write some data to the file.
        outfile.write("Hello World 2\n")
        outfile.write("Next Text\n")
        outfile.write("Next Text 2")
