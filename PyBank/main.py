import os
import csv

#Function which prints the analysis to the terminal
def analysis_term(info):
    print("Financial Analysis")
    print("------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_money}")
    print(f"Average Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in profits: {max_date} (${greatest_increase})")
    print(f"Greatest Decrease in profits: {min_date} (${greatest_decrease})") 
    
#Function which prints the analysis to an output text file then closes it
def analysis_txt(info):
    with open(r"analysis/analysis.txt", "w") as analysis_file:
        print("Financial Analysis", file = analysis_file)
        print("------------------------------------", file = analysis_file)
        print(f"Total Months: {total_months}", file = analysis_file)
        print(f"Total: ${total_money}", file = analysis_file)
        print(f"Average Change: ${round(average_change, 2)}", file = analysis_file)
        print(f"Greatest Increase in profits: {max_date} (${greatest_increase})", file = analysis_file)
        print(f"Greatest Decrease in profits: {min_date} (${greatest_decrease})", file = analysis_file)
    analysis_file.close()

#Function to call analysis prints
def analysis(info):
    analysis_txt(info)
    analysis_term(info)

#Create our variables
total_months = total_money = average_change = greatest_increase = greatest_decrease = i = 0
max_date = min_date = str()
totals = []
change = []
dates = []
info = []

#Read in the csv data file
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    #We keep track of number of months, profits/losses each month, and the dates
    for row in csvreader:
        total_months+=1
        totals.append(int(row[1])) #Here we cast row[1] as an integer to be able to do math later
        dates.append(row[0])
        
    #We find the profit difference each month and store it in a list to manipulate later        
    for i in range(total_months-1):
        change.append(totals[i+1]-totals[i])
        
csvfile.close() #Always good practice to close files when done with them  


total_money = sum(totals)  #Here we sum every month's total
average_change = sum(change) / len(change) #Here we find the average change in profit

#Find the index at which the min/max change occurs then read its date and value
#The + 1 to the change index accounts for change having 1 less index than the number of dates
min_index = change.index(min(change)) + 1
min_date = dates[min_index]
greatest_decrease = min(change)

max_index = change.index(max(change)) + 1
max_date = dates[max_index]
greatest_increase = max(change)

#Gather all useful information in one list
info = [total_months, total_money, average_change, greatest_increase, greatest_decrease, max_date, min_date]

#Utilize the list of gathered info to call our analysis function
analysis(info)

