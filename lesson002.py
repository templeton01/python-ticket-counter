#creating a professionalemail address generator
firstname = input("Enter your firstname:").lower()
lastname = input("Enter your lastname: ").lower()

#Processing the input
username =f"{firstname[0]}{lastname}"

# output of the email generator
print(f"you email address is: {username.lower()}@university.co.za")

