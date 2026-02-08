#!/usr/bin/env python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in [0,1,2]:
                return value
            else:
                print("Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Enter a number 0, 1, or 2.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    winner = None

    while not winner and any(" " in row for row in board):
        print_board(board)
        print(f"Player {player}'s turn.")
        row = get_int_input("Enter row (0, 1, or 2): ")
        col = get_int_input("Enter column (0, 1, or 2): ")
        if board[row][col] == " ":
            board[row][col] = player
            winner = check_winner(board)
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
