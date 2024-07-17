import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

with open(election_data_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Print header
    print("Election Results")
    print("-------------------------------")

    # Skip header row
    header = next(csv_reader)
    
    # Initialize variables
    Votes_Total = 0
    Candidate_Votes = {}

    # Read through the file and tally votes
    for row in csv_reader:
        Votes_Total += 1
        Candidate_Name = row[2]
        if Candidate_Name in Candidate_Votes:
            Candidate_Votes[Candidate_Name] += 1
        else:
            Candidate_Votes[Candidate_Name] = 1

    # Calculate percentages and find winner
    Candidate_Winner = ""
    Greatest_Votes = 0

    # Print results
    print(f"Total Votes: {Votes_Total}")
    print("-------------------------------")
    for Candidate, Votes in Candidate_Votes.items():
        Vote_Percentage = (Votes / Votes_Total) * 100
        print(f"{Candidate}: {Vote_Percentage:.3f}% ({Votes})")
        if Votes > Greatest_Votes:
            Greatest_Votes = Votes
            Candidate_Winner = Candidate
    
    print("-------------------------------")
    print(f"Winner: {Candidate_Winner}")
    print("-------------------------------")
