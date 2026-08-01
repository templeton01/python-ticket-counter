# Creating ATM Simullator
balance = 500.00
amount = float(input("please Enter the amount you want to withdraw: "))

print("\n========================Smart===ATM===Simulator============================\n")
# calculations for Smart ATM simulator
withdrawal = balance - amount

# conditional statements for smart ATM simulator
if withdrawal <= 500:
    print("Transaction Successful!!!")
elif withdrawal <= 0:
    print("Insufficient funds")
else:
    print("Declined transcaction")

print("you current balance is: " + str(balance))
print("the amount you have withdrawn is: " + str(amount))
print("your Available balance is:" + str(withdrawal))
print("=============================================================================")
