global N
N = int(input("Enter the value of N: "))

def printSolution(board):
	for i in range(N):
		for j in range(N):
			print ('|',board[i][j],end=' ')
		print('|')

def isSafe(board, row, col):
	for i in range(col):
		if board[row][i] == 'Q':
			return False

	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 'Q':
			return False

	for i, j in zip(range(row, N, 1), range(col, -1, -1)):
		if board[i][j] == 'Q':
			return False

	return True

def solveNQUtil(board, col):
	if col >= N:
		return True

	for i in range(N):
		if isSafe(board, i, col):
			board[i][col] = 'Q'

			if solveNQUtil(board, col + 1) == True:
				return True

			board[i][col] = ' '

	return False

def solveNQ():
	board = [[' ']*N for _ in range(N)]

	if solveNQUtil(board, 0) == False:
		print ("Solution does not exist")
		return False

	printSolution(board)
	return True

solveNQ()


''' The code begins by taking input from the user for the value of N, which represents the size of the chessboard and the number of queens to be placed.

The printSolution function is defined to print the final placement of queens on the chessboard.

The isSafe function checks if it is safe to place a queen at a particular position (row, col) on the chessboard. It checks for conflicts with previously placed queens in the same row, diagonal, and anti-diagonal.

The solveNQUtil function is the main recursive function that tries to solve the N-Queens problem. It takes the chessboard board and the current column col as parameters. It uses backtracking to explore all possible placements of queens column-wise.

If the col value exceeds or equals N, it means all queens have been successfully placed, and the function returns True to indicate a valid solution.

The function iterates through all rows i in the current column col. For each row, it checks if it is safe to place a queen at position (i, col). If it is safe, it places a queen at that position and recursively calls solveNQUtil for the next column (col + 1).

If the recursive call returns True, it means a solution has been found, and the function returns True.

If the recursive call returns False, it means the current placement of queens leads to conflicts or doesn't lead to a solution. In that case, it backtracks by removing the queen from the current position (i, col) and tries the next row.

If no valid placement is found for the current column, the function returns False.

The solveNQ function initializes the chessboard board as an empty NxN grid.

It calls the solveNQUtil function to solve the N-Queens problem starting from the first column (col = 0).

If solveNQUtil returns False, it means no solution exists, and it prints "Solution does not exist."

If solveNQUtil returns True, it means a solution has been found, and it calls printSolution to print the final placement of queens on the chessboard.

Finally, it returns True to indicate that a solution has been found.

Overall, the code solves the N-Queens problem by systematically exploring all possible placements of queens on the chessboard using backtracking. It prints the first valid solution it finds or reports that no solution exists. '''
