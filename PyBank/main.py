# Create a Python script that analyzes the records to calculate each of the following:

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


import os
import csv

budget_csv = os.path.join("..","Resources", "budget_data.csv")

with open(budget_csv, "r") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    print(header)

    #the total number of months included in the dataset
    months = []
    for row in csvreader:
        months.append(row[0])
    num_of_month = len(months)

    #The net total amount of "Profit/Losses" over the entire period
    net_total = 0
    for row in csvreader:
        net_total += int(row[1])

    #The average of the changes in "Profit/Losses" over the entire period
    
    
    #The greatest increase in profits (date and amount) over the entire period


    #The greatest decrease in losses (date and amount) over the entire period


    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {num_of_month}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ")
    print(f"Greatest Increase in Profits: ")
    print(f"Greatest Increase in Profits: ")
