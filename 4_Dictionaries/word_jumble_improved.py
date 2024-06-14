import random

WORDS = {
    "python": "a programming language", 
    "jumble": "another word for mix", 
    "easy": "opposite of hard", 
    "difficult": "opposite of easy", 
    "answer": "ask a question and expect a ...", 
    "piano": "a instrument"}

word = random.choice(list(WORDS.keys()))
hint = WORDS[word]
correct = word

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

print("Welcome to Word Jumble")
print("Enter 'hint' if stuck")
print("Press any key at the prompt to quit")
print("\nGuess the jumble:", jumble)

hint_used = False
guess_count = 0

guess = "?"

while guess != correct and guess != "":
    guess = input("Your guess: ")
    if guess == "hint":
        print("hint:", hint)
        hint_used = True
        continue
    guess_count += 1

if guess == correct:
    print("That's it! You guessed it!\n")

    #getting the score
    score = 0
    if guess_count == 1:
        score = 10
    elif guess_count == 2:
        score = 8
    elif guess_count == 3:
        score = 6
    else:
        score = 2

    #score adjustment if hint used
    if hint_used:
        score = score/2

    print("You scored:", score)

print("Thanks for playing.")
input("Press any key to exit.")