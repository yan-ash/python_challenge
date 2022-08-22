import os
import csv


os.chdir(os.path.dirname(__file__))

#-----------------------------------------------------

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')
outputpath=os.path.join('Analysis', 'election_data.txt')

#initialize a total vote counter.
total_votes=0
winning_counts=0
#define candidate_list(name) and canidates_vote
candidate_list=[]
candidates_vote={}


with open (csvpath) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        header= next(csvreader)
       
        
        for row in csvreader:
            total_votes= total_votes+1
            candidate =str(row[2]) 
            # if the candidate name is not in the candidate list, add candidate in the list
            if candidate not in candidate_list:
              
                candidate_list. append(candidate)
                
                candidates_vote[candidate]=0

                candidates_vote[candidate] += 1
print(total_votes)                    
print(candidate_list) 
print(candidates_vote) 
 
with open(outputpath, 'w') as csvtxt:
            Election_results= print("Election Results")
            total_votes=print(f'Total Votes: {total_votes}')
for candidate in candidates_vote:
        vote=(candidates_vote).get(candidate)
        candidate_percentage= float(vote)/float(total_votes) *100
        candidate_result=(f"{candidate}:{candidate_percentage:.3f}%\n")
        if vote> winning_counts:

            print(f"Winning Candidate:{candidate}")

print(candidate_result)



       

 





