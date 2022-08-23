from distutils.text_file import TextFile
from fileinput import filename
import os
import csv
from tkinter import N


os.chdir(os.path.dirname(__file__))

#-----------------------------------------------------

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')
outpath=os.path.join('Analysis', 'election_data.txt')

#initialize a total vote counter.
total_votes=0
winning_counts=0
#define candidate_list for each candidate name and canidates_vote is a dictionary for all candidates and their votes
candidate_list=[]
candidates_vote={}

#open the files and read it:
with open (csvpath) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        header= next(csvreader)
       
        #for each row in csvreader, total vote adds up with each row including the first row
        for row in csvreader:
            total_votes= total_votes+1
            candidate =str(row[2]) 
            # if the candidate name is not in the candidate list, add candidate in the list, 
            
            if candidate not in candidate_list:
             # candidate name adds  to the candidate list 
                candidate_list. append(candidate)
             #each candidate's votes start with "0"   
                candidates_vote[candidate]=0
            # within each row loop, the candidate's votes add up
            candidates_vote[candidate] += 1
print(total_votes)                    
print(candidate_list) 
print(candidates_vote) 

#start writing the output file with our total votes that we calculated 


with open(outpath, "w") as txt_file:

    output_content=(f"Election Result\n\n"
    f"-----------------------------------\n"
    f"Total Votes:{total_votes}\n\n"
     f"-----------------------------------\n")
    txt_file.write(output_content)


#Design a look to work out each candidat's vote number and their vote percentage and write out to the textfile

    for candidate in candidates_vote:
        vote=(candidates_vote).get(candidate)
        candidate_percentage= float(vote)/float(total_votes) *100
        candidate_result=(f"{candidate}:{candidate_percentage:.3f}% ({vote})\n")
        
        print(candidate_result)
        txt_file.write(f"{candidate_result}\n")
    #
    # Use a if loop to work out which candidate has the most votes and output the winner candidate   
    
        if (vote> winning_counts):
                winning_counts=vote
                winning_candidate=candidate
    


    print(f"Winning Candidate:{winning_candidate}")
    winning=(f"-----------------------------------\n"
        f"Winning Candidate:{winning_candidate}\n\n"
     f"-----------------------------------\n")
    txt_file.write(winning)



    
    
    



       

 





