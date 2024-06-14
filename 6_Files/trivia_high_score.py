import sys

TRIVIA_FILE = "6_Files/trivia_high_score.txt"
TRIVIA_FILE_PERSIST = "6_Files/trivia_high_score_persist.txt"

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    points = next_line(the_file)

    return category, question, answers, correct, explanation, points

def welcome(title):
    """Welcome the player"""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")

def save_high_score(player_name, player_score):
    #store in dictionary
    with open(TRIVIA_FILE_PERSIST, "r") as file:
        high_score_list = {}
        for line in file:
            high_score_list[line.split(":")[0]] = int((line.split(":")[1]).strip())

    #order dictionary ascending
    high_score_list = dict(sorted(high_score_list.items(), key=lambda item: item[1]))

    #append score to dictionary ifapplicable
    if len(high_score_list) < 5:
        high_score_list[player_name] = player_score
    else:
        for key, value in high_score_list.copy().items():
            if player_score >= value:
                if key == player_name:
                    high_score_list[key] = player_score
                    break
                else:
                    del high_score_list[key]
                    high_score_list[player_name] = player_score
                    break
	
    #clear file
    open(TRIVIA_FILE_PERSIST, 'w').close()    

    #order dictionary desc
    high_score_list = dict(sorted(high_score_list.items(), key=lambda item: item[1], reverse=True))        

    #overwrite file
    with open(TRIVIA_FILE_PERSIST, "a") as file:
        for key, value in high_score_list.items():
            file.write(key + ": " + str(value) + "\n")

    #print high scores
    print("\nHigh score list\n")
    with open(TRIVIA_FILE_PERSIST, "r") as file:
        for line in file:
            print(line)
      
def main():
    trivia_file = open_file(TRIVIA_FILE, "r")
    title = next_line(trivia_file)
    welcome(title)

    player_name = input("Enter your name: ")
    score = 0
 
    # get first block
    category, question, answers, correct, explanation, points = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(points)
        else:
            print("\nWrong.", end=" ")
        print(explanation)

        # get next block
        category, question, answers, correct, explanation, points = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You scored:", score)

    save_high_score(player_name, score)
    
main()
input("\nPress the enter key to exit.")