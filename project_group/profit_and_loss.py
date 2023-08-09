import csv

def find_highest_profit_deficit(csv_file):
    max_deficit = 0
    max_deficit_day = None

    with open('project_group\csv_reports\profit-and-loss-usd(final).csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            net_profit = int(row['Net Profit'])
            if net_profit < max_deficit:
                max_deficit = net_profit
                max_deficit_day = int(row['Day'])

    return max_deficit_day, max_deficit

def find_profit_surplus_each_day(csv_file):
    surplus_data = []

    with open('project_group\csv_reports\profit-and-loss-usd(final).csv', 'r') as file:
        reader = csv.DictReader(file)
        prev_cash_amount = 0
        for row in reader:
            cash_amount = int(row['Cash Amount'])  # Replace with the actual column name
            if cash_amount > prev_cash_amount:
                surplus_data.append((int(row['Day']), cash_amount))
            prev_cash_amount = cash_amount

    return surplus_data

def profit_and_loss_function():
    csv_file = 'project_group\csv_reports\profit-and-loss-usd(final).csv'  # Replace with your CSV file's path
    max_deficit_day, max_deficit = find_highest_profit_deficit(csv_file)
    if max_deficit_day is not None:
        return [(max_deficit_day, max_deficit)]
    else:
        return find_profit_surplus_each_day(csv_file)
