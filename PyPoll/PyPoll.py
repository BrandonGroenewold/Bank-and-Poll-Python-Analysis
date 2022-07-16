#Enable python to be able to import and read files
import os
import csv

#Declare the path of where csv file is
csvpath = os.path.join('Resources','election_data.csv')

#dictionary for canidate and the amount of votes casted for them
canidates_poll = {}
cast_votes = []
canidates = []
percent_votes = []
votes_by_canidates = []

#poll = {"canidate":"cast_votes"}
with open(csvpath) as election_data:
    #how to divide up the file
    csvreader = csv.reader(election_data, delimiter=',')
    next (csvreader)


    total_votes = 0
    for row in csvreader:
        total_votes = total_votes + 1
        canidate_name = row[2]
        
        if canidate_name not in canidates:
            canidates.append(canidate_name)

            canidates_poll[canidate_name]=0

        canidates_poll[canidate_name] +=1
    
    for canidate_name in canidates_poll:
        percentage = (canidates_poll.get(canidate_name))/(total_votes)*100
        percent_votes.append(percentage)
       
    Winner = max(canidates_poll,key=canidates_poll.get)
    

print("Election Results")
print("---------------------")
print(total_votes)
print("---------------------")
print(canidates_poll)
print("---------------------")
print(Winner)
print("---------------------")








    # print(Winner)
# print(percent_votes)

# print(canidates_poll)
# print(canidates_poll)

# print(canidates)


    #print(total_votes)


