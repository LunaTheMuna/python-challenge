import os
import csv
import sys
import pprint


# In[11]:


class Logger(object):
    def __init__(self,logfile):
        self.terminal = sys.stdout
        self.log = open(logfile, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        #this flush method is needed for python 3 compatibility.
        #this handles the flush command by doing nothing.
        #you might want to specify some extra behavior here.
        pass    

log="election_results.txt"
sys.stdout = Logger(log)

csv_path = os.path.join("/Users/johnarmstrong/RUBootcamp/GitHub/python-challenge/pyPoll", "Resources", "election_data.csv")



with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    vote_tally = { }
    
    allVoteCounter = 0

    for row in csv_reader:

        voterID = row[0]
        county = row[1]
        candidate = row[2]

        if(candidate == "Candidate"): continue

        allVoteCounter = allVoteCounter + 1
        
        if candidate in vote_tally:
            vote_tally[candidate] = int(vote_tally[candidate]) + 1
        else:
            vote_tally[candidate] = 1


    vote_percentage = {}
    print(f'There were ' + str(allVoteCounter) + ' votes cast' )
    
    winner = ""
    winnerVotes = int(max(vote_tally.values()))
    for candidate in vote_tally :
       vote_percentage[candidate] = vote_tally[candidate] / allVoteCounter * 100
       if(vote_tally[candidate] == winnerVotes) :
           winner = candidate

    for k,v in vote_percentage.items() : 
        print (f'Candidate: ' + k, str(v) + '% ('+ str(vote_tally[k]) + ')')

    print('And the winner is: '+ winner)

    