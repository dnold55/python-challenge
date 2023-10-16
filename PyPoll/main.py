import csv

input_file = "election_data.csv"
output_file = "election_results.txt"

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

with open(input_file, 'r') as file:
    csvreader = csv.reader(file)
    
    next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

result_summary = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    result_summary += f"{candidate}: {percentage:.3f}% ({votes})\n"

result_summary += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n")

print(result_summary)

with open(output_file, 'w') as f:
    f.write(result_summary)

print(result_summary)