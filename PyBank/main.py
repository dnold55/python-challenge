import os
import csv

csv_file = os.path.join('budget_data.csv')

total_months = 0
net_total = 0
previous_profit = 0
profit_changes = []
months = []

with open(csv_file, newline='') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)  
    
    for row in csv_reader:
        date = row[0]
        profit = int(row[1])
        
       
        total_months += 1
        net_total += profit
        
       
        if total_months > 1:
            change = profit - previous_profit
            profit_changes.append(change)
            months.append(date)
        
        previous_profit = profit

average_change = round(sum(profit_changes) / len(profit_changes), 2)
greatest_increase = max(profit_changes)
greatest_increase_date = months[profit_changes.index(greatest_increase)]
greatest_decrease = min(profit_changes)
greatest_decrease_date = months[profit_changes.index(greatest_decrease)]

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

output_file = "financial_analysis.txt"
with open(output_file, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("--------------------------\n")
    output.write(f"Total Months: {total_months}\n")
    output.write(f"Total: ${net_total}\n")
    output.write(f"Average Change: ${average_change}\n")
    output.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    output.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
