import os
import csv


os.chdir(os.path.dirname(__file__))
# Optional: print the current working directory
print("This program is running from: " + os.getcwd())
#-----------------------------------------------------

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')
#define changes and have it accept the 
total_votes=0


with open (csvpath) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        header= next(csvreader)
        for row in csvfile:
            total_votes= total_votes+1 
            