import os
import csv

#create dictionary
poll = {}
#set variables
total_votes = 0
#creating lists
candidates = []
num_votes = []
vote_percentage = []
winner_list = []
#find file
csvpath = os.path.join('..','PyPoll','election_data.csv')
#get data in file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CVS Header: {csv_header}")

#setting the dictionary based on unique candidates and counts votes
    for row in csvreader:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1   

# takes values from dictionary and puts into the pre-created lists
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

#vote percentage being put into list
for n in num_votes:
    vote_percentage.append(round(n/total_votes*100, 1))

#zipping lists
clean_data = list(zip(candidates, num_votes, vote_percentage))

# winner list updated
for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])
winner = winner_list[0]

# sets and opens the output destination in write mode and prints the summary
file = '../PyPoll/input.txt'
with open(file,'w') as writefile:
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Poll Election Results\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total amount of Votes: ' + str(total_votes) + '\n')
    writefile.writelines('----------------------------' + '\n')
    for entry in clean_data:
        writefile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('The Winner is: ' + winner + '!!!!!' '\n')
    writefile.writelines('----------------------------' + '\n')

# opens the output file in r mode and prints to terminal
with open(file, 'r') as readfile:
    print(readfile.read())

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# Election Results
#------------------------------
# Total Votes: 3521001
#------------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
#------------------------------
# Winner: Khan
#------------------------------

