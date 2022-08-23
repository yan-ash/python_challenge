
import os
import csv

#setting working directory to where this Python file is 
os.chdir(os.path.dirname(__file__))

#-----------------------------------------------------

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')
outpath = os.path.join('Analysis', 'budget.txt')

#define total month, profit start with "0", net change list is a list gathers all the monthly changes 
#set up a list for greastest increase and greatest decrease including the month and profit varible
total_month=0
total_profits=0
month_of_change=[]
net_change_list=[]
greatest_increase=["",0]
greatest_decrease=["",0]
total_net_change=0

#open file and read file 
with open (csvpath) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=',')
        #first row is the header
        header= next(csvreader)
        #next row is the first month profit also should be the totalprofits is the same as the first month profit
        firstprofit=next(csvreader)
        total_profits+=int(firstprofit[1])
        previous_profit=int(firstprofit[1])
        total_month+=1
   
        #Read throught the file through each row and work out the total month and total profits
        #profit change =  current month profit - previous month profit and then put the varible into a list 
        for row in csvreader:
                total_month=total_month+1
                total_profits= total_profits+int((row[1]))
                month_of_change+= [row[0]]
    
                profit_change=int(row[1])-previous_profit
                previous_profit= int(row[1])
                net_change_list += [profit_change]
                
                # use if loop to work out the greatest increase and decrease 
                if profit_change> greatest_increase[1]:
                        greatest_increase[0]=row[0]
                        greatest_increase[1]=profit_change
                if profit_change<greatest_decrease[1]:
                        greatest_decrease[0]=row[0]
                        greatest_decrease[1]=profit_change

#work out the average change is total net change devided by the length of the netlist 
total_net_change=sum(net_change_list)  
average_change= total_net_change/len(net_change_list)
print(f"Total Month:{total_month}")
print(f"Total Profits:${total_profits}\n")
print(f"Average Change:${average_change:.2f}\n")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

#summarize the output text and write the contents into the output text

output_text=(f"Financial Analysis\n"
f"---------------------------\n"
        
        f"Total Month:{total_month}\n\n"
f"Total Profits:${total_profits}\n\n"
f"Average Change:${average_change:.2f}\n\n"
f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n\n"
f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output_text)

with open(outpath, "w") as file:
        file.write(output_text)





               










                




        
        

            
       



