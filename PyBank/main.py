from fileinput import filename
import os
import csv


os.chdir(os.path.dirname(__file__))

#-----------------------------------------------------

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')
outpath = os.path.join('Analysis', 'budget.txt')
#define total month, profit start with "0", net change list is a list gathers all the monthly changes 
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
    
        for row in csvreader:
                total_month=total_month+1
                total_profits= total_profits+int((row[1]))
                month_of_change+= [row[0]]
    
                profit_change=int(row[1])-previous_profit
                previous_profit= int(row[1])
                net_change_list += [profit_change]
                
        
                if profit_change> greatest_increase[1]:
                        greatest_increase[0]=row[0]
                        greatest_increase[1]=profit_change
                if profit_change<greatest_decrease[1]:
                        greatest_decrease[0]=row[0]
                        greatest_decrease[1]=profit_change

total_net_change=sum(net_change_list)  
average_change= total_net_change/len(net_change_list)
print(f"Total Month:{total_month}")
print(f"Total Profits:${total_profits}\n")
print(f"Average Change:${average_change:.2f}\n")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")



               










                




        
        

            
       



