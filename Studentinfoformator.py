# Creating a student formator app
name = input("please enter your name:")
Surname = input("please enter your surname:")
age_in_years = int(input("please enter your age in years:"))
favourite_number = float(input("please enter your favorite number:"))

# Calcaulate age in months
age_in_months = age_in_years * 12

# displaying output information
print(f"your profile information is as follows Name: {type(name)} Surname: {type(Surname.upper())} Age in Months: {type(age_in_months)} Favourite Number: {favourite_number:.2f}")