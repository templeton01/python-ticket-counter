#creating an else if programme
age = int(input("Enter age :"))
VIP_ticket = input("Do you have a VIP ticket? (yes/no)").lower()

if age >= 18 and VIP_ticket == "yes":
    print("Welcome to the VIP Area !!!!")
elif age >= 18:
    print("Welcome to the general area !!!!")
else:
 print("Access is not granted tsamo rota o robale!!!!!")