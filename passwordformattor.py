# The security password hint
password = input("Please enter yor password: ")

# processing the password hint
last_first = f"{password[0].upper()}{password[-1].lower()}".strip()

# Output the password hint
print(f"your password hint is: {last_first}")
