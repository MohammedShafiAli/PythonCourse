
#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    print(
    """
    Welcome to Tic Tac Toe

    Make you move known by entering 0 - 8

    0 | 1 | 2
    ---------
    3 | 4 | 5
    ---------
    6 | 7 | 8
    """
    )

def ask_yes_no(question):
    #"Ask a yes or no question
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
    
def ask_number(question, low, high):
    #Ask for a number within a range
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    #Determine if the player or computer goes first
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print("You go first \n")
        human = X
        computer = O
    else:
        print("I'll go first \n")
        human = O
        computer = X
    return computer, human

def new_board():
    #Create new board
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print("\n\t", board[0], " | ", board[1], " | ", board[2])
    print("\t", "-------------")
    print("\n\t", board[3], " | ", board[4], " | ", board[5])
    print("\t", "-------------")
    print("\n\t", board[6], " | ", board[7], " | ", board[8])

def legal_moves(board):
    #Create list of legal moves
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    #Determine the game winner
    WAYS_TO_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        
    if EMPTY not in board:
        return TIE
    
    #the game is incomplete
    return None

def human_move(board, human):
    #Get human move
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nThat square is already occupied. Choose another.\n")
    print("Fine...")
    return move  

def computer_move(board, computer, human):
    #Make computer move

    #make a copy since function will be changing the list
    board = board[:]

    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I shall take square number ")

    #if computer can win take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY

    #if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY

    #since no one can win on the next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move
        
def next_turn(turn):
    #Swith turns
    if turn == X:
        return O
    else:
        return X
    
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("You humans are weak!")
    elif the_winner == human:
        print("You tricked me human")
    elif the_winner == TIE:
        print("We will go again") 

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

#start program
main()
input("\n\nPress any key to quit")