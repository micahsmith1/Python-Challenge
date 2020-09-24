import os 
import csv 

election_data = os.path.join("..", "PyPoll", "Resources", "Election_Data.csv")

num_votes = []
candid_votes = []
khan_votes = 0 
correy_votes = 0
li_votes = 0 
otooley_votes = 0 

#Open election data 
with open(election_data, 'r')as elc_results:

    #Read election data  
    csv_reader = csv.reader(elc_results, delimiter = ',')
    csv_header = next(csv_reader)

    for row in csv_reader:

        #Total Number of Votes 
        num_votes.append(row[0])
        votes = len(num_votes)

        #List of Candidates who received votes 
        candid_votes.append(row[2])
        if row[2] == 'Khan':
            khan_votes += 1
        elif row[2] == 'Correy':
            correy_votes +=  1
        elif row[2] == 'Li':
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1 

    #Create a Dictionaries 
    candids = ['Khan', 'Correy', 'Li', "O'Tookey"]
    total_votes = [khan_votes, correy_votes, li_votes, otooley_votes]

    #Zip Dictionaries together 
    dict_ed = dict(zip(candids,total_votes))
    winner = max(dict_ed, key = dict_ed.get)

    #Percentage of votes each Candidate won 
    khan_per = round((khan_votes/votes) * 100, 3)
    correy_per = round((correy_votes/votes) * 100, 3)
    li_per = round((li_votes/votes) * 100 , 3)
    otooley_per = round((otooley_votes/votes) * 100 , 3)

    print(f'Election Results')

    print(f'-------------------------')

    print(f'Total Votes: {votes}')

    print(f'-------------------------')

    print(f'Khan: {khan_per}% ({khan_votes})')

    print(f'Correy: {correy_per}% ({correy_votes})')

    print(f'Li: {li_per}% ({li_votes})')

    print(f"O'Tooley: {otooley_per}% ({otooley_votes})")

    print(f'-------------------------')

    print(f'Winner: {winner}')

    print(f'-------------------------')

    #Output to Text File 
    file = open('output.txt', 'w')

    file.write('Election Results ' + '\n')

    file.write('-------------------------' + '\n')

    file.write(f'Total Votes: {votes}' + '\n')

    file.write('-------------------------' + '\n')

    file.write(f'Khan: {khan_per}% ({khan_votes})' + '\n')

    file.write(f'Correy: {correy_per}% ({correy_votes})' +  '\n')

    file.write(f'Li: {li_per}% ({li_votes})' + '\n')

    file.write(f"O'Tooley: {otooley_per}% ({otooley_votes})" + '\n')

    file.write('-------------------------' + '\n')

    file.write(f'Winner: {winner}' + '\n')

    file.write('-------------------------')


    
        

    