# Dependencies
import os
import csv

# Specify path to csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

# Define variables for calculating and storing values
profit_loss_total = 0
profit_loss_change = []
current_row_profit_loss = 0
previous_row_profit_loss = 0
greatest_decrease_profit = 0

# Open and read data excluding header
with open(budget_csv) as data:
    reader = csv.reader(data, delimiter=",")
    header = next(reader)
    first_row = next(reader)
    profit_loss_total += int(first_row[1])
    previous_row = int(first_row[1])
    total_months = []

    for row in reader:
        total_months.append(row[0])
        profit_loss = int(row[1])
        profit_loss_total += profit_loss
        profit_loss_change_value = profit_loss - previous_row
        profit_loss_change.append(profit_loss_change_value)
        previous_row = int(row[1])

greatest_increase_profit = max(profit_loss_change)
greatest_decrease_profit = min(profit_loss_change)

month_increase = profit_loss_change.index(max(profit_loss_change))
month_decrease = profit_loss_change.index(min(profit_loss_change))
average_change = round(sum(profit_loss_change)/len(profit_loss_change), 2)


# Print Analysis
print("Financial Analysis")
print("---------------------------------")
print(f"Total Months: {len(total_months)+1}")
print(f"Total: ", "$", profit_loss_total)
print(f"Average Change: $", average_change)
print(f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(greatest_increase_profit))})")
print(f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(greatest_decrease_profit))})")

# Write data output to txt file
PyBank_output = open('PyBank.txt', 'w')
PyBank_output.write('Financial Analysis\n')
PyBank_output.write('-----------------------------\n')
PyBank_output.write(f"Total Months: {len(total_months)+1}\n")
PyBank_output.write(f"Total: ${int(profit_loss_total)}\n")
PyBank_output.write(f"Average Change: ${round(sum(profit_loss_change)/len(profit_loss_change),2)}\n")
PyBank_output.write(f"Greatest Increase in Profits: {total_months[month_increase]} (${(str(greatest_increase_profit))})\n")
PyBank_output.write(f"Greatest Decrease in Profits: {total_months[month_decrease]} (${(str(greatest_decrease_profit))})\n")