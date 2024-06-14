import random

WORDS = ["python", "jumble", "easy", "difficult", "answer", "piano"]
word = random.choice(WORDS)

print("The random word has", len(word), "characters")
for i in range(5):
    character = input("Guess a letter in the word: ")
    if character in word:
        print("yes")
    else:
        print("no")

guess = input("Guess the word: ")

if guess == word:
    print("You got it!")
else:
    print("Not this time")

print("Thank's for playing")