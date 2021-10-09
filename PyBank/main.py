import os
import csv

num_month = 0
total = []
changes = []
average =0
month=[]

budget_data = os.path.join('Resources', 'budget_data.csv')
with open (budget_data) as csvfile:
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    #print(csv_header)
    for row in csvreader:
       
        # The total number of months includes in the dataset
        num_month = num_month + 1

        # The net total amount of "Profit/Losses" over the entire period
        values = row[1]
        month.append(row[0])
        total.append(int(values))
        

    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    for i in range(1,len(total)):
        changes.append(total[i]-total[i-1])

    average = sum(changes)/len(changes)

    # The greatest increase in profits (date and amount) over the entire period
    max_in = max(changes)
    pos_max_in = changes.index(max_in)
    month_in = month[int(pos_max_in) + 1]

    # The greatest decrease in profits (date and amount) over the entire period
    max_de = min(changes)
    pos_max_de = changes.index(max_de)
    month_de = month[int(pos_max_de) + 1]
    
    
    # Print results
    print("Financila Analysis")
    print("---------------------------")
    print(f'Total Months: {num_month}')
    print(f'Total: ${sum(total)}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {month_in} (${max_in})')
    print(f'Greatest Decrease in Profits: {month_de} (${max_de})')

# Create a Text File
output_path = os.path.join("analysis", "analysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write("Financila Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f'Total Months: {num_month}\n')
    txtfile.write(f'Total: ${sum(total)}\n')
    txtfile.write(f'Average Change: ${average}\n')
    txtfile.write(f'Greatest Increase in Profits: {month_in} (${max_in})\n')
    txtfile.write(f'Greatest Decrease in Profits: {month_de} (${max_de})\n')