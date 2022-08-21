import os
import csv


os.chdir(os.path.dirname(__file__))
# Optional: print the current working directory
print("This program is running from: " + os.getcwd())
#-----------------------------------------------------

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

#initialize a total vote counter.
total_votes=0
#define candidate_list(name) and canidates_vote
candidate_list=[]
candidates_vote={}


with open (csvpath) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        header= next(csvreader)
       
        
        for row in csvfile:
            total_votes= total_votes+1
            candidate =(row[2])
            # if the candidate name is not in the candidate list, add candidate in the list
            if candidate not in candidate_list:
              
                candidate_list= candidate_list. append(candidate)
                
                candidates_vote[candidate]=0

            candidates_vote[candidate] += 1

            

 
vote_count_sum=sum(vote_count_list)


print(candidate_list)
print(vote_count_sum)

