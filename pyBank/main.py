import os
import csv
import sys

from statistics import mean 

def average (list): 
    if not list : return 0
    return sum(list) / len (list)


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

csv_path = os.path.join("/Users/johnarmstrong/git/python-challenge", "pyBank", "budget_data.csv")

with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    for row in csv_reader:
        budget_dict = {rows[0]:rows[1] for rows in csv_reader}
    

    pnl_delta = {}
    pnl_delta_abs= {}
  
    prev_month=""
    pnl_delta_value=0
    pnl_delta_by_delta = {}
    for month in budget_dict.keys():
    
        tPnl = int(budget_dict[month])
        if prev_month != "":
            pnl_delta_value=tPnl-int(budget_dict[prev_month])
            pnl_delta[month]= pnl_delta_value
            pnl_delta_abs[month] = abs(pnl_delta_value)
            pnl_delta_by_delta[pnl_delta_value]=month
        prev_month=month
 
  
    print ("Financial Analysis\n-----------------------")
    print(f'Total Months {len(budget_dict)}')

    totalpnl=0

    for pnl in budget_dict.values() :
        totalpnl += int(pnl)
    print(f'Net PnL :' + str(totalpnl))

    print(f'The average monthly PnL delta is ' + str(average(pnl_delta_abs.values())) ) 


    maxPnl = max(pnl_delta.values())
    minPnl = min(pnl_delta.values())

    print(f'greatest monthly pnl increase is ' + str(maxPnl) + " which occurred in " + pnl_delta_by_delta[maxPnl])
    print(f'greatest monthly pnl decrease is ' + str(minPnl) + " which occurred in " + pnl_delta_by_delta[minPnl])

print(f'Results also written to ' + log)