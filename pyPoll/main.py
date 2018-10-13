
# coding: utf-8

# In[10]:


# Import Dependencies
import pandas as pd
import os
import csv
import sys


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

log="results.txt"
sys.stdout = Logger(log)


# In[12]:


# Create a reference the CSV file desired
csv_path = "Resources/election_data.csv"

# Read the CSV into a Pandas DataFrame
election_df1 = pd.read_csv(csv_path)

# How many votes were cast?

num_votes =  election_df1["Voter ID"].count()

print("There were " + str(num_votes) + " votes cast.")


# In[13]:


# list the candidates 
candidates = election_df1["Candidate"].unique()
candidates


# In[14]:


# total votes by candidate
candidate_vote_counts = election_df1["Candidate"].value_counts()
candidate_vote_counts.head()


# In[15]:


# The percentage of votes by candidate
candidate_percentage = candidate_vote_counts / num_votes * 100
print("The vote percentages were ") 
print(candidate_percentage)


# In[16]:


# Winner based on popular vote
vote_tally = pd.DataFrame(candidate_vote_counts)

vote_tally.rename(columns={'Candidate': 'Votes'}, inplace=True)
vote_tally.sort_values("Votes",ascending=False)
winner= vote_tally[:1].index[0]
print ("And the winner is " + winner ) 

