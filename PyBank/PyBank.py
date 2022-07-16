#Enable python to be able to import and read files
import os
import csv

#Declare the path of where csv file is
csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as budget_data:
    
     #Definitions of list       
    num_month_count = []
    profit = []
    change_in_profit = []
    #how to divide up the file
    csvreader = csv.reader(budget_data, delimiter=',')
    next(csvreader)

    for row in csvreader:
        num_month_count.append(row[0])
        profit.append(int(row[1]))
        # print(row)

print(num_month_count)
print(profit)

#change in profit loop
prevprofit = profit[0]
for i in range(len(profit)-1):
    #take the next profit/loss line and subtract it from the one you are on
    change_in_profit.append(profit[i+1]-prevprofit)
    prevprofit = profit[i+1]

#find the biggest profit
#look at the new column change_in_profit and take the biggest one
Biggest_profit= max(change_in_profit)

#find the biggest loss
Biggest_loss= min(change_in_profit)

#How do I get it to show the month with the max and min?
#is this it?
Biggest_month_increase= change_in_profit.index(max(change_in_profit))+1
Biggest_month_decrease= change_in_profit.index(min(change_in_profit))+1
#
#

#print out your results
print("Financial Analysis")
print("------------------------")
#len returns the number of items in a list
print(f"Total Months: {len(num_month_count)}")
print(f"Total $ {sum(profit)}")
print(f"Average Change: " + str(round(sum(change_in_profit)/len(change_in_profit),2)))
#add date to biggest profit and loss
print(f"Greatest increase in Profits: {num_month_count[Biggest_month_increase]} (${(str(Biggest_profit))})")
print(f"Greatest Decrease in Profits: {num_month_count[Biggest_month_decrease]} (${(str(Biggest_loss))})")


