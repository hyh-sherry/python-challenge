# Create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

import os
import csv

budget_csv = os.path.join(os.path.dirname( __file__ ), "..","Resources","budget_data.csv")

with open(budget_csv, "r") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(header)

    #the total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    months = []
    profit_losses = []

    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))
    
    num_of_month = len(months)
    net_total = sum(profit_losses)
    max_increase = max(profit_losses)
    min_increase = min(profit_losses)

    #The average of the changes in "Profit/Losses" over the entire period
    changes = []
    i = 0
    while i < len(profit_losses)-1:
        num = profit_losses[i+1]-profit_losses[i]
        changes.append(num)
        i += 1
    print(changes)
    avg_changes = round(sum(changes)/(len(months)-1),2)
    
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period
    for i in range(len(profit_losses)):
        if profit_losses[i] == max_increase:
            max_month = months[i]
        if profit_losses[i] == min_increase:
            min_month = months[i]

    #Print Result
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {num_of_month}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${avg_changes}")
    print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
    print(f"Greatest Increase in Profits: {min_month} (${min_increase})")

    #Write a txt file with results
    result_file = open("Pybank/PyBank_Results.txt","w+")
    print("Financial Analysis", file = result_file)
    print("----------------------------", file = result_file)
    print(f"Total Months: {num_of_month}", file = result_file)
    print(f"Total: ${net_total}", file = result_file)
    print(f"Average Change: ${avg_changes}", file = result_file)
    print(f"Greatest Increase in Profits: {max_month} (${max_increase})", file = result_file)
    print(f"Greatest Increase in Profits: {min_month} (${min_increase})", file = result_file)
    result_file.close()
