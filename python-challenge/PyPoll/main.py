import os
import csv

#Initialize our variables
total_votes = i = j = cand_vote = perc = 0
winner_index = -1 #List indices are positive so if this does not update then something went wrong
cand_name = []
cand_perc = []
unique = []

#Read in the csv data file
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    #Get total number of votes and read every voters choice of candidate
    for row in csvreader:
        total_votes+=1
        cand_name.append(row[2])
csvfile.close() #Close csv file

#Create output text file for analysis
#Prints both to terminal and output file
with open(r"analysis/analysis.txt", "w") as analysis_file:

    print("Election Results", file = analysis_file)
    print("--------------------------", file = analysis_file)
    print(f"Total Votes: {total_votes}", file = analysis_file)
    print("--------------------------", file = analysis_file)
    
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_votes}")
    print("--------------------------")
    
    #Searches through every candidate and creates a unique list of names
    for candidate in cand_name:
        if candidate not in unique:
            unique.append(candidate)
    
    #For each unique candidate we read every vote and tally up
    for i in range(len(unique)):
        cand_vote = 0
        for j in range(total_votes):
            if cand_name[j]==unique[i]:
                cand_vote+=1
        perc = round(cand_vote / total_votes * 100, 3) #Changes each i
        cand_perc.append(perc) #A list of percentages so we may take the max later
        print(f"{unique[i]}: {cand_perc[i]}% ({cand_vote})")
        print(f"{unique[i]}: {cand_perc[i]}% ({cand_vote})", file = analysis_file)
        
        
    winner_index = cand_perc.index(max(cand_perc)) #The index of the winner
    print("--------------------------")
    print(f"Winner: {unique[winner_index]}")
    print("--------------------------")
    
    print("--------------------------", file = analysis_file)
    print(f"Winner: {unique[winner_index]}", file = analysis_file)
    print("--------------------------", file = analysis_file)
analysis_file.close() #Close output file
            

