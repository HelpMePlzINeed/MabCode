import csv

def find_profit_deficit(profit_data):
    deficit_data = [(day, int(amount)) for day, amount in profit_data if int(amount) < 0]
    return deficit_data

def read_profit_data():
    profit_data = []
    with open('project_group/csv_reports/profit-and-loss-usd(final).csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            profit_data.append((int(row['Day']), int(row['Net Profit'])))
    return profit_data

def profit_and_loss_function():
    profit_data = read_profit_data()
    deficit_data = find_profit_deficit(profit_data)
    return deficit_data
