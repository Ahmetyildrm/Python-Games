import sys
import os
# board
# display board
# play game
# handle turn
# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player

number_board = ["1", "2", "3",
                "4", "5", "6",
                "7", "8", "9"]

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_nuboard():
    print(number_board[0] + " | " + number_board[1] + " | " + number_board[2])
    print(number_board[3] + " | " + number_board[4] + " | " + number_board[5])
    print(number_board[6] + " | " + number_board[7] + " | " + number_board[8])
    print(" ")
    print(" ")

def dispay_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():

    handle_turn_X()
    check_win()
    check_tie()
    handle_turn_O()
    check_win()
    check_tie_end()

def handle_turn_X():
    position = input("Choose a position from 1-9(X): ")
    position = int(position) - 1
    if board[position] != "-":
        print("That place is not empty.")
        handle_turn_X()
    else:
        board[position] = "X"
        print(("\n" * 100))
        display_nuboard()
        dispay_board()

def handle_turn_O():
    position = input("Choose a position from 1-9(O): ")
    position = int(position) - 1
    if board[position] != "-":
        print("That place is not empty.")
        handle_turn_O()
    else:
        board[position] = "O"
        print(("\n" * 10))
        display_nuboard()
        dispay_board()

def check_win():
    check_rows()
    if check_rows() != False:
        sys.exit()
    check_columns()
    if check_columns() != False:
        sys.exit()
    check_diagonals()
    if check_diagonals() != False:
        sys.exit()

def check_rows():
    if board[0] == board[1] == board[2] != "-":
        print(board[0],"won the game")
        sys.exit()
    elif board[3] == board[4] == board[5] != "-":
        print(board[3],"won the game")
        sys.exit()
    elif board[6] == board[7] == board[8] != "-":
        print(board[6],"won the game")
        sys.exit()
    else:
        return False

def check_columns():
    if board[0] == board[3] == board[6] != "-":
        print(board[0],"won the game")
        sys.exit()
    elif board[1] == board[4] == board[7] != "-":
        print(board[1],"won the game")
        sys.exit()
    elif board[2] == board[5] == board[8] != "-":
        print(board[2],"won the game")
        sys.exit()
    else:
        return False

def check_diagonals():
    if board[0] == board[4] == board[8] != "-":
        print(board[0],"won the game")
        sys.exit()
    elif board[2] == board[4] == board[6] != "-":
        print(board[2],"won the game")
        sys.exit()
    else:
        return False

def check_tie():
    if "-" not in board:
        if check_rows() == False and check_columns() == False and check_diagonals() == False:
            print("Tie Game")
            sys.exit()

def check_tie_end():
    if "-" not in board:
        if check_rows() == False and check_columns() == False and check_diagonals() == False:
            print("Tie Game")
            sys.exit()
    else:
        play_game()

display_nuboard()
dispay_board()
play_game()