# Task b: Find the day and amount of the highest increment in Cash-on-Hand
def compute_profit_deficit_surplus(cash_differences):
    deficit_data = [(day, -amount) for day, amount in cash_differences if amount < 0]
    if deficit_data:
        return deficit_data
    else:
        return [(day, -amount) for day, amount in cash_differences if amount > 0]

def profit_and_Loss_function():
    # Assuming cash_differences is available from previous calculations
    cash_differences = [(1, 100), (2, 50), (3, -20), (4, 120), (5, -80)]
    profit_data = compute_profit_deficit_surplus(cash_differences)
