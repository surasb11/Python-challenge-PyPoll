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
	winner_candidate = ""
	candidates = 0
	votes_percentage = 0
	winner_candidate_summary = 0

	greatest_votes = ["", 0]
	candidates_list = []
	candidate_votes = {}


	with open(election_data_path) as election_data:
		reader = csv.reader(election_data)
		header = next (reader)
		
		for row in reader:
			total_votes = total_votes + 1
			candidates_name = row[2]
			
			if candidates_name not in candidates_list:
				
				candidates_list.append(candidates_name)

				candidate_votes[candidates_name] = 0
				
			
			candidate_votes[candidates_name] = candidate_votes[candidates_name] + 1
	 
	print(candidate_votes)

	with open (outputFileName, "w") as txt_file:
		election_results = (
		f"Election Results\n"
		f"-------------------------\n"
		f"Total Votes {total_votes}\n"
		f"-------------------------\n")
		print(election_results, end="")
		txt_file.write(election_results)

		for candidate in candidate_votes:
			votes = candidate_votes.get(candidate)
			
			vote_precentage = float(votes)/float(total_votes)*100
			if (votes > winner):
				winner = votes
				winner_candidate = candidate
			voter_output = f"{candidate}: {vote_precentage:.3f}% ({votes})\n"
			print(voter_output, end="")
			txt_file.write(voter_output)
			
		winning_candidate_summary = (
		f"-------------------------\n"
		f"Winner: {winner_candidate}\n"
		f"-------------------------\n")
		print(winning_candidate_summary)
		txt_file.write(winning_candidate_summary)