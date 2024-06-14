import random

WORDS = ["python", "jumble", "easy", "difficult", "answer", "piano"]
word = random.choice(WORDS)
correct = word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Welcome to Word Jumble")
print("Press any key at the prompt to quit")
print("Guess the jumble:", jumble)

guess = input("guess: ")
while guess != correct and guess != "":
    guess = input("Incorrect, guess again: ")

if guess == correct:
    print("That's it! You guessed it!\n")

print("Thanks for playing.")
input("Press any key to exit.")