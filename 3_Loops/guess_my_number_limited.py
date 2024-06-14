import random

the_number = random.randint(1,100)
tries_allowed = 5
guess = int(input("Guess a number between 1 and 100: "))
tries = 1

while(guess != the_number and tries < tries_allowed):
    
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Guess again: "))
    tries += 1

if(guess == the_number):
    print("You guessed it! The number was", the_number)
    print("It took", tries, "tries!")
else:
    print("You loose. The max number of guesses allowed was", tries_allowed)  
    print("The number was", the_number)

input("Press any key to exit.")