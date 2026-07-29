# Creatign the calculator bill system
bill = float(input("Enter the amount due: R"))
tip = 0.15

#Process of the bill calculator
amount_due = bill * tip
total_amount = bill + amount_due

#Output of the tip calculator
print(f"Here is the your amount due: R{amount_due}")
print(f"Here is your total amount_due: R{round(amount_due, 2)}")
print(f"Here is your total amount: R{total_amount}")
print(f"Here is your total amount: R{round(total_amount, 2)}")