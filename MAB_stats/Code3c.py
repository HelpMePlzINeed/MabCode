import csv

def find_highest_overhead_category(overheads):
    max_overhead = max(overheads, key=lambda x: float(x['Overheads']))
    return max_overhead['Category'].strip()

if __name__ == "__main__":
    overhead_data = []
    with open('MAB_stats/CSVs Real/overheads.csv', 'r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            overhead_data.append(row)

    highest_overhead_category = find_highest_overhead_category(overhead_data)
    print(f"Highest overhead category: {highest_overhead_category}")