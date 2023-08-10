import csv
import cash_on_hand
import overheads
import profit_and_loss 

def main():
    overhead_category, overhead_percentage = overheads.overhead_function()
    cash_deficit_data = cash_on_hand.cash_on_hand_function()
    profit_surplus_data = profit_and_loss.profit_and_loss_function()

    with open('project_group/summary_report.txt', 'w') as file:
        file.write(f"[HIGHEST OVERHEAD] {overhead_category.upper()}: {overhead_percentage:.2f}%\n")

        if profit_surplus_data:
            max_surplus_day, max_surplus = max(profit_surplus_data, key=lambda x: x[1])
            if max_surplus > 0:
                label = "HIGHEST PROFIT SURPLUS"
                file.write(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
            else:
                label = "HIGHEST PROFIT DEFICIT"
            file.write(f"[{label}] DAY:{max_surplus_day}, AMOUNT: USD{max_surplus}\n")

        
        if cash_deficit_data:  
            for day, cash_amount in cash_deficit_data:  
                file.write(f"[CASH DEFICIT] DAY:{day}, AMOUNT: USD{cash_amount}\n")

if __name__ == "__main__":
    main()
