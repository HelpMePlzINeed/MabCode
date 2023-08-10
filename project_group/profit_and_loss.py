import csv

def find_highest_profit_deficit(csv_file):
    max_deficit = 0
    max_deficit_day = None

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            net_profit = int(row['Net Profit'])
            if net_profit < max_deficit:
                max_deficit = net_profit
                max_deficit_day = int(row['Day'])

    return max_deficit_day, max_deficit

def find_profit_surplus_each_day(csv_file):
    surplus_data = []

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        prev_net_profit = 0
        for row in reader:
            net_profit = int(row['Net Profit'])
            if net_profit > prev_net_profit:
                surplus_data.append((int(row['Day']), net_profit))
            prev_net_profit = net_profit

    return surplus_data

def profit_and_loss_function():
    csv_file = 'project_group\csv_reports\profit-and-loss-usd(final).csv'
    
    max_deficit_day, max_deficit = find_highest_profit_deficit(csv_file)
    
    if max_deficit_day is not None:
        return [(max_deficit_day, max_deficit)]
    else:
        surplus_data = find_profit_surplus_each_day(csv_file)
        if surplus_data:
            max_surplus_day, max_surplus = max(surplus_data, key=lambda x: x[1])
            return [(max_surplus_day, max_surplus)]
        else:
            return []
