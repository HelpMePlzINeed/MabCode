import csv

def read_jonas_data():
    jonas_data = []
    with open('project_group/csv_reports/profit-and-loss-usd(final).csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            day = int(row['Day'])
            operating_expense = int(row['Operating Expense'])
            jonas_data.append((day, operating_expense))
    return jonas_data

def jonasdeficit_amount_function():
    jonas_data = read_jonas_data()
    return jonas_data

