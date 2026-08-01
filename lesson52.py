# Creatig a guessing game

secret_name = "python"

while True :
    guess = input("Guess the name of the languege we are using: ").lower()
    
    if guess == secret_name:
        print("you are right!!!!!")
        break
    else:
        print("please try again later!!!!!!")
