# Task a: Compute day-to-day difference in Cash-on-Hand
import csv

def compute_cash_difference(data):
    differences = []
    for i in range(1, len(data)):
        current_cash = int(data[i]['Cash On Hand'])
        previous_cash = int(data[i - 1]['Cash On Hand'])
        difference = previous_cash - current_cash
        differences.append((i, difference))
    return differences

def cash_on_hand_function():
    cash_data = []
    with open('project_group/csv_reports/cash-on-hand-usd(final).csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cash_data.append(row)

    cash_differences = compute_cash_difference(cash_data)
    
    cash_deficits = [(day, amount) for day, amount in cash_differences if amount > 0]
    return cash_deficits
