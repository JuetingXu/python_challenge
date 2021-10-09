import os
import csv

total_votes = 0
votes = 0
votes_list = []
candidate = []
percentage = []

election_data = os.path.join('Resources', 'election_data.csv')
with open (election_data) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)
    for row in csvreader:
        # The total number of votes cast
        total_votes = total_votes + 1
       
        # A complete list of candidates who received votes
        # The total number of votes each candidate won
        if row[2] not in candidate:
            candidate.append(row[2])
            # start the count at 1 for candidate
            votes_list.append(1)
        else:
            # find which index of votes_list to add to
            candidate_index = candidate.index(row[2])
            votes_list[candidate_index] = votes_list[candidate_index] + 1
            
    # The percentage of votes each candidate won
    for number in votes_list:
        percentage.append(number/int(total_votes)*100)
    # The winner of the election based on popular vote.
    max_votes = max(votes_list)
    pos_max_votes = votes_list.index(max_votes)
    winner = candidate[pos_max_votes]
   
    
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {total_votes}')
    print("-------------------------")
    
    for i in range(0,len(candidate)):
        print(f'{candidate[i]}: {percentage[i]}% ({votes_list[i]})')

    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")

# Create a Text File
output_path = os.path.join("analysis", "analysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write("-------------------------\n")
    
    for i in range(0,len(candidate)):
        txtfile.write(f'{candidate[i]}: {percentage[i]}% ({votes_list[i]})\n')

    txtfile.write("-------------------------\n")
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write("-------------------------\n")