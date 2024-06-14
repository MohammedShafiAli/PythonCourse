import random

the_number = random.randint(1,100)
guess = int(input("Guess a number between 1 and 100: "))
tries = 1

while(guess != the_number):
    
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Guess again: "))
    tries += 1

print("You guessed it! The number was", the_number)
print("It took", tries, "tries!")

input("Press any key to exit.")