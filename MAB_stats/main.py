import csv
import os
print(os.getcwd())
from Code1a import compute_cash_difference
from Code2b import find_highest_increment
from Code3c import find_highest_overhead_category

# Task a: Read Cash-on-Hand data from CSV
cash_data = []
with open('MAB_stats/CSVs Real/cash-on-hand-usd(final).csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cash_data.append(row)

# Task a: Compute the day-to-day difference in Cash-on-Hand
cash_differences = compute_cash_difference(cash_data)

# Task b: Find the day and amount of the highest deficit in Cash-on-Hand
deficit_data = [(day, amount) for day, amount in cash_differences if amount > 0]
max_deficit_day, max_deficit_amount = find_highest_increment(deficit_data)

# Task c: Find the highest overhead category
overhead_data = []
with open('MAB_stats/CSVs Real/overheads.csv', 'r', newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        overhead_data.append(row)

highest_overhead_category = find_highest_overhead_category(overhead_data)

# Write the computed results to a text file
with open('MAB_stats/summary_report.txt', 'w') as file:
    file.write(f"[HIGHEST OVERHEAD] {highest_overhead_category.upper()}: {max(overhead_data, key=lambda x: float(x['Overheads']))['Overheads']}%\n")
    file.write(f"[CASH DEFICIT] DAY:{max_deficit_day}, AMOUNT: USD{max_deficit_amount}\n")

    # Additional logic for profit deficit/surplus
    deficit_data = [(day, -amount) for day, amount in cash_differences if amount < 0]
    if deficit_data:
        for day, deficit_amount in deficit_data:
            file.write(f"[PROFIT DEFICIT] DAY:{day}, AMOUNT: USD{deficit_amount}\n")
    else:
        surplus_data = [(day, -amount) for day, amount in cash_differences if amount > 0]
        for day, surplus_amount in surplus_data:
            file.write(f"[PROFIT SURPLUS EVERYDAY] DAY:{day}, AMOUNT: USD{surplus_amount}\n")