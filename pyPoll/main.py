
# coding: utf-8

# In[1]:


# Import Dependencies
import pandas as pd


# In[2]:


# Create a reference the CSV file desired
csv_path = "Resources/election_data.csv"

# Read the CSV into a Pandas DataFrame
election_df1 = pd.read_csv(csv_path)

# How many votes were cast?

num_votes =  election_df1["Voter ID"].count()

print("There were " + str(num_votes) + " votes cast.")


# In[3]:


# list the candidates 
candidates = election_df1["Candidate"].unique()
candidates


# In[4]:


# total votes by candidate
candidate_vote_counts = election_df1["Candidate"].value_counts()
candidate_vote_counts.head()


# In[9]:


# The percentage of votes by candidate
candidate_percentage = candidate_vote_counts / num_votes * 100
print("The vote percentages were ") 
print(candidate_percentage)


# In[6]:


# Winner based on popular vote
vote_tally = pd.DataFrame(candidate_vote_counts)

vote_tally.rename(columns={'Candidate': 'Votes'}, inplace=True)
vote_tally.sort_values("Votes",ascending=False)
winner= vote_tally[:1].index[0]
print ("And the winner is " + winner ) 

