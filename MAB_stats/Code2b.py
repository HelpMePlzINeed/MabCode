# Task b: Find the day and amount of the highest increment in Cash-on-Hand
def find_highest_increment(data):
    max_increment = max(data, key=lambda x: x[1])
    max_day = int(max_increment[0])
    max_amount = max_increment[1]
    return max_day, max_amount

if __name__ == "__main__":
    cash_differences = [(1, 100), (2, 50), (3, -20), (4, 120), (5, -80)]
    max_deficit_day, max_deficit_amount = find_highest_increment(cash_differences)
    print(f"Max deficit day: {max_deficit_day}, Amount: {max_deficit_amount}")