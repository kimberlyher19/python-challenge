import os
import csv
from datetime import datetime

budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Print the header
    print("Financial Analysis")
    print("-------------------------------")

    # Skip the header row
    header = next(csv_reader)
    
    # Initialize variables
    date_count = 0
    total_list = []
    changes_list = []
    dates = []
    
    # Read the first row (to initialize the first month's value)
    first_row = next(csv_reader)
    date_count += 1
    first_month = int(first_row[1])
    total_list.append(first_month)
    first_month_date = first_row[0] 

    # Initialize variables to track the greatest increase and decrease
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}
    
    # Read through the rest of the file
    for row in csv_reader:
        date_count += 1
        second_month = int(row[1])
        total_list.append(second_month)
        
        # Calculate the change and add it to the changes list
        change = second_month - first_month
        changes_list.append(change)
        dates.append(second_month)

        # Check if this change is the greatest increase or decrease
        if change > greatest_increase["amount"]:
            greatest_increase["amount"] = change
            greatest_increase["date"] = row[0]
        
        if change < greatest_decrease["amount"]:
            greatest_decrease["amount"] = change
            greatest_decrease["date"] = row[0]
        
        # Update the first month
        first_month = second_month
    
    # Calculate the total profit/loss
    total_profit_loss = sum(total_list)
    
    # Calculate the average change in profit/loss
    average_change = sum(changes_list) / len(changes_list)
    
    # Format the dates for the greatest increase and decrease
    greatest_increase_date = datetime.strptime(greatest_increase["date"], '%b-%y').strftime('%b-%y')
    greatest_decrease_date = datetime.strptime(greatest_decrease["date"], '%b-%y').strftime('%b-%y')

    # Print the results
    print(f"Total Months: {date_count}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease['amount']})")
