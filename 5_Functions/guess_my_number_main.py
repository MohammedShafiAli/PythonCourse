import random

def ask_number():
    user_input = int(input("Guess number: "))
    return user_input

def main():
    the_number = random.randint(1,100)

    print("Guess a number between 1 and 100")
    guess = ask_number()
    tries = 1

    while(guess != the_number):
        
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")

        guess = ask_number()
        tries += 1

    print("You guessed it! The number was", the_number)
    print("It took", tries, "tries!")

    input("Press any key to exit.")

main()