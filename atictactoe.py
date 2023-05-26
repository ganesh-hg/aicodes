def print_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "_":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "_":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "_":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "_":
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if "_" in row:
            return False
    return True

def play_game():
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]
    current_player = "X"

    while True:
        print_board(board)
        print("Player", current_player)

        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] != "_":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player", winner, "wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

play_game()
