import csv
import cash_on_hand
import overheads
import profit_and_loss

def main():
    overhead_category, overhead_percentage = overheads.overhead_function()
    cash_deficit_data = cash_on_hand.cash_on_hand_function()
    profit_deficit_data = profit_and_loss.profit_and_loss_function()

    with open('project_group/summary_report.txt', 'w') as file:
        file.write(f"[HIGHEST OVERHEAD] {overhead_category.upper()}: {overhead_percentage:.2f}%\n")

        if cash_deficit_data:
            max_deficit_day, max_deficit_amount = max(cash_deficit_data, key=lambda x: x[1])
            file.write(f"[CASH DEFICIT] DAY:{max_deficit_day}, AMOUNT: USD{-max_deficit_amount}\n")

        if profit_deficit_data:
            for day, deficit_amount in profit_deficit_data:
                file.write(f"[PROFIT DEFICIT] DAY:{day}, AMOUNT: USD{-deficit_amount}\n")
        else:
            surplus_data = [(day, amount) for day, amount in cash_deficit_data if amount > 0]
            for day, surplus_amount in surplus_data:
                file.write(f"[PROFIT SURPLUS EVERYDAY] DAY:{day}, AMOUNT: USD{surplus_amount}\n")

if __name__ == "__main__":
    main()
