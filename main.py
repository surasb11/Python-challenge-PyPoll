import os
import csv

election_data_path = os.path.join('election_data.csv')

with open(election_data_path, newline='') as election_data:
	
	csvreader = csv.reader(election_data, delimiter=',')

	print(csvreader)

	election_data_header = next(csvreader)
	print(f"CSV Header: {election_data_header}")
	
	
inputFileName = "election_data.csv"
outputFileName = "election_data_script.txt"

total_votes = 0
winner = 0
candidates = 0
votes_percentage = 0

greatest_votes = ["", 0]
candidates_list = []
candidate_votes = {}


with open(election_data_path) as election_data:
	reader = csv.DictReader(election_data)
	
	
	for row in reader:
		total_votes = total_votes + 1
		total_candidates = row["Candidate"]
		
		if row["Candidate"] not in candidates_list:
			
			candidates_list.append(row["Candidate"])

			candidate_votes[row["Candidate"]] = 1
			
		else:
			candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

	print("Election Results")
	print("Total Votes " + str(total_votes))   

	
import pandas as pd
import numpy as np

inputFileName_df = pd.read_csv(inputFileName)
inputFileName_df.head(10)

total_votes = inputFileName_df["Voter ID"].count()
inputFileName_df["Voter ID"].count()

total_candidates = inputFileName_df['Candidate'].value_counts()

unique_candidate = inputFileName_df["Candidate"].unique()
unique_candidate

from collections import OrderedDict
from operator import itemgetter

print()
print()
print()
print("Election Results")
print("-------------------------")
print("Total Votes " + str(total_votes))
print("-------------------------")


for candidate in candidate_votes:
	print(candidate + " " + str(round(((candidate_votes[candidate]/total_votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
	candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/total_votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
	
	
	candidate_votes
	winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)
	print("-------------------------")
	print("Winner: " + str(winner[0]))
	print("-------------------------")

with open(outputFileName, "w") as txt_file:
	txt_file.write("Election Results")
	txt_file.write("\n")
	txt_file.write("-------------------------")
	txt_file.write("\n")
	txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/total_votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
	txt_file.write(str(winner))
	txt_file.write("\n")
	txt_file.write("-------------------------")
	txt_file.write("\n")
	txt_file.write("Winner: " + str(winner[0]))
	txt_file.write("\n")
	txt_file.write("Total Votes " + str(total_votes))