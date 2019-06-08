# Create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


import os
import csv

budget_csv = os.path.join("..","Resources","budget_data.csv")

with open(budget_csv, "r") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(header)

    #the total number of months included in the dataset
    months = []
    for row in csvreader:
        months.append(row[0])
    num_of_month = len(months)

    #The net total amount of "Profit/Losses" over the entire period
    profit_losses = []
    for row in csvreader:
        profit_losses.append(int(row[1]))
    net_total = sum(profit_losses)

    #The average of the changes in "Profit/Losses" over the entire period
    changes = []
    i = 0
    while i < len(profit_losses):
        num = profit_losses[i+1]-profit_losses[1]
        changes.append(num)
        i += 1
    avg_changes = sum(changes)/months
    
    #The greatest increase in profits (date and amount) over the entire period
    max_increase = max(profit_losses)
    for row in csvreader:
        if int(row[1]) == max_increase:
            max_month = row[0]

    #The greatest decrease in losses (date and amount) over the entire period
    min_increase = min(profit_losses)
    for row in csvreader:
        if int(row[1]) == min_increase:
            min_month = row[0]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {num_of_month}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${avg_changes}")
    print(f"Greatest Increase in Profits: {max_month} (${max_increase})")
    print(f"Greatest Increase in Profits: {min_month} (${min_increase})")
