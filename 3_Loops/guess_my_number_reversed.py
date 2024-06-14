import random

the_number = int(input("Input a number 1 and 100 for the computer to guess: "))
lower = 1
upper = 101
guess = (upper - lower)//2 + lower 
tries = 1

while(guess != the_number):
    print("Incorrect guess:", guess)
    if guess > the_number:
        upper = guess
    else:
        lower = guess

    guess = (upper - lower)//2 + lower 
    tries += 1

print("The computer guessed it! The number was", the_number)
print("It took", tries, "tries!")

input("Press any key to exit.")