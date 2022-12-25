import random


board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
presentPlayer = "X"
champion = None
gameRunning = True

# game board for tic tac toe
def tictactoe_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# taking input from player
def playerInput(board):
    inp = int(input("Select a spot in tictactoe board 1-9: "))
    if board[inp-1] == "-":
        board[inp-1] = presentPlayer
    else:
        print("Oops player is already at that spot.")


# checking for win or tie in game
def checkHorizontle(board):
    global champion
    if board[0] == board[1] == board[2] and board[0] != "-":
        champion = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        champion = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        champion = board[6]
        return True

def checkRow(board):
    global champion
    if board[0] == board[3] == board[6] and board[0] != "-":
        champion = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        champion = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        champion = board[3]
        return True


def checkDiag(board):
    global champion
    if board[0] == board[4] == board[8] and board[0] != "-":
        champion = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        champion = board[2]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontle(board):
        tictactoe_board(board)
        print(f"The champion is player {champion}!")
        gameRunning = False

    elif checkRow(board):
        tictactoe_board(board)
        print(f"The champion is player {champion}!")
        gameRunning = False

    elif checkDiag(board):
        tictactoe_board(board)
        print(f"The champion is player {champion}!")
        gameRunning = False


def checkIfTie(board):
    global gameRunning
    if "-" not in board:
        tictactoe_board(board)
        print("It is a tie!")
        gameRunning = False


# switching the players
def switchPlayer():
    global presentPlayer
    if presentPlayer == "X":
        presentPlayer = "O"
    else:
        presentPlayer = "X"


def computerplayer(board):
    while presentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


while gameRunning:
    tictactoe_board(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computerplayer(board)
    checkIfWin(board)
    checkIfTie(board)