import csv

def read_cash_on_hand_data():
    cash_on_hand_data = []
    with open('project_group/csv_reports/cash-on-hand-usd(final).csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            day = int(row['Day'])
            cash_amount = int(row['Cash On Hand'])
            cash_on_hand_data.append((day, cash_amount))
    return cash_on_hand_data

def jonas_cash_on_hand_function():
    cash_on_hand_data = read_cash_on_hand_data()
    return cash_on_hand_data