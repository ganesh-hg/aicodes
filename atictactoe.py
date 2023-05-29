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



''' The print_board function takes a 2D list board representing the Tic-Tac-Toe board and prints it in a visually appealing format. It uses a nested loop to iterate over each row in the board and prints the elements separated by | using the join function. After printing each row, it prints a horizontal line of dashes to separate the rows.

The check_winner function takes a 2D list board and checks for a winning condition. It checks for three in a row in rows, columns, and diagonals. It uses nested loops to iterate over the rows and columns of the board and checks if the elements in a row, column, or diagonal are equal and not equal to "_". If a winning condition is found, it returns the winning player's symbol ("X" or "O"). Otherwise, it returns None to indicate that there is no winner yet.

The is_board_full function takes a 2D list board and checks if the board is full (i.e., all positions are filled with symbols). It uses a nested loop to iterate over the board and checks if any position contains "_". If there is any "_", it returns False to indicate that the board is not full. Otherwise, it returns True to indicate that the board is full.

The play_game function is the main function that runs the Tic-Tac-Toe game. It initializes the board as a 2D list representing the Tic-Tac-Toe board, with all positions initially filled with "_". It also initializes the current_player variable with the symbol of the current player ("X" or "O").

The game is played in an infinite loop until a winner is found or the board is full. Inside the loop:

The print_board function is called to display the current state of the board.
The current player is displayed.
The user is prompted to enter the row and column numbers (0-2) for their move.
The code checks if the chosen position is already occupied. If it is, an error message is displayed, and the loop continues to the next iteration.
If the chosen position is valid and available, the symbol of the current player is placed in that position on the board.
The check_winner function is called to check if the current player has won. If a winner is found, the current state of the board is displayed, and a message is printed indicating the winner. The loop is then exited.
If there is no winner, the is_board_full function is called to check if the board is full. If it is, the current state of the board is displayed, and a message is printed indicating a draw. The loop is then exited.
If the game is not over yet, the turn is switched to the other player by updating the current_player variable.
The play_game() function is called to start the Tic-Tac-Toe game.

Overall, the code provides a basic implementation of a command-line Tic-Tac-Toe game. Players take turns entering their moves, and the code checks for a winning condition or a draw after each move. The game continues until a winner is found or the board is full. '''
