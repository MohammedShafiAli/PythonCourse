import random

words = ["python", "jumble", "easy", "difficult", "answer", "piano"]

while words:
    word = random.choice(words)
    print(word)
    words.remove(word)


