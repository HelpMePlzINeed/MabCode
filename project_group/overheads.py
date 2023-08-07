import csv

def find_highest_overhead_category(overheads):
    max_overhead = max(overheads, key=lambda x: float(x['Overheads']))
    return max_overhead['Category'].strip()

def overhead_function():
    overhead_data = []
    with open('project_group/csv_reports/overheads.csv', 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            overhead_data.append(row)

    highest_overhead_category = find_highest_overhead_category(overhead_data)
