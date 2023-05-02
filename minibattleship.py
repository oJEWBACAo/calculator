from random import randint

# Set up the game board
board = []
for i in range(5):
    board.append(["O"] * 5)

# Print the board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Place the ship randomly on the board
def place_ship(board):
    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board[0]) - 1)
    return (ship_row, ship_col)

ship_row, ship_col = place_ship(board)

print("Let's play Battleship!")
print_board(board)

# Play the game
for turn in range(4):
    print(f"Turn {turn + 1}")

    # Get the user's guess
    guess_row = int(input("Guess Row (0-4): "))
    guess_col = int(input("Guess Col (0-4): "))

    # Check if the guess is correct
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print("Game Over")
    print_board(board)
