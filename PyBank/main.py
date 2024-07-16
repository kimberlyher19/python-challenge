import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #print the header
    print("Financial Analysis")
    #print the dashes
    print("-------------------------------")

    first_row = next(csv_reader)
    second_row = next(csv_reader)

    date_count = 1
    total_list = []
    total_list.append(int(second_row[1]))
    

    for date in csv_reader:
        date_count += 1
        total_list.append(int(date[1]))
        

    print(date_count)
    print(sum(total_list))
    


