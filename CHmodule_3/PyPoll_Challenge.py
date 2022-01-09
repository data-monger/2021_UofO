# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
# -------------------------------Section 1---------------------------------------------------------
import csv
import os
import sys                  # this is from another solution i created in a production environment
                            # for a client. the absolute path works in my home\machine\environment
                            # and the proposed solution provided by os.path.join will probably work
                            # in future production environments

from datetime import date
today = date.today()


#file_to_load = sys.argv[1]
#file_to_save = sys.argv[2]

# Load file
# -------------------------------Section 2---------------------------------------------------------
# Add a variable to load a file from a path. // none of the below seem to work...
#file_to_load = os.path.join(os.getcwd(), "Resources", "election_results.csv")
#file_to_load = os.path.join("Resources", "election_results.csv")
file_to_load = r'C:\Users\grego\Box\Education\_Work\_3\CHmodule_3\Resources\election_results.csv'

# Add a variable to save the file to a path. // none of the below seem to work...
#file_to_save = os.path.join(os.getcwd(), "Analysis", "election_analysis.txt")
#file_to_save = os.path.join("Analysis", "election_analysis.txt")
file_to_save = r'C:\Users\grego\Box\Education\_Work\_3\CHmodule_3\Analysis\election_analysis.txt'

# Variables
# -------------------------------Section 3---------------------------------------------------------
# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
#candidate_options = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
#county_options = ['Jefferson', 'Denver', 'Arapahoe']
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
county_max = ""
county_voters = 0

# datablock headers
county_header = (
    f"County Votes:\n")

candidate_header = (
    f"Candidate Votes:\n")

# Read File
# -------------------------------Section 4---------------------------------------------------------
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] =0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

# Print to Term and Write to File
# -------------------------------Section 5---------------------------------------------------------
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print Header 
    header = (
        f"\nResults Tabulated on: {today:}\n")

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")

    print(header)
    print(election_results, end="")
    txt_file.write(header)
    txt_file.write(election_results)


# County Level
# -------------------------------Section 6---------------------------------------------------------
    # clear shared vars'
    winning_count = 0
    winning_percentage = 0

    txt_file.write(county_header)

    # 6a: Write a for loop to get the county from the county dictionary.

    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes)/float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # 6d: Print the county results to the terminal.
        print(county_results)

        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_county = county_name
            winning_percentage = vote_percentage

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Winner: {winning_county}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
        f"\n")
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

# Candidate Level
# -------------------------------Section 7---------------------------------------------------------
    # clear shared vars'
    winning_count = 0
    winning_percentage = 0

    txt_file.write(candidate_header)
    
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
        f"\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
