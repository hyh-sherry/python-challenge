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

    print(max_increase)
    print(min_increase)

    #The average of the changes in "Profit/Losses" over the entire period
    changes = []
    i = 0
    while i < len(profit_losses)-1:
        num = profit_losses[i+1]-profit_losses[i]
        changes.append(num)
        i += 1
    print(changes)
    avg_changes = sum(changes)/len(months)
    
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period
    #with open(budget_csv, "r") as csvfile:
    #    for row in csvreader:
    #        if int(row[1]) == max_increase:
    #            max_month = row[0]
    #        if int(row[1]) == min_increase:
    #            min_month = row[0]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {num_of_month}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${avg_changes}")
    #print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
    #print(f"Greatest Increase in Profits: {min_month} (${min_increase})")
