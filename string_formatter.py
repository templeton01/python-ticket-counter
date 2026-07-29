# creating Username and formattor
firstname = input("Enter your firstname:")
lastname = input("Enter your lastname:")
bio_message = input("please write your message at the bio:").replace("i am", "I'm")

# processing the data
username = f"{firstname [0]}{lastname}".lower()

# The formmat Output
print(f"your Firstname: {firstname.title()} Lastname: {lastname.title()} bio: {len(bio_message.strip())} username: {username.lower()}")
print(f"Firstname: {firstname}")
print(f"Lastaname: {lastname}")
print(f"bio: {bio_message}")
print(f"username: {username}")