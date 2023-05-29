import copy
from heapq import heappush, heappop

n = 3
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]

class priorityQueue:
	def __init__(self):
		self.heap = []

	def push(self, k):
		heappush(self.heap, k)

	def pop(self):
		return heappop(self.heap)

	def empty(self):
		if not self.heap:
			return True
		else:
			return False

class node:
	def __init__(self, parent, mat, empty_tile_pos, cost, level):				
		self.parent = parent
		self.mat = mat
		self.empty_tile_pos = empty_tile_pos
		self.cost = cost
		self.level = level

	def __lt__(self, nxt):
		return self.cost < nxt.cost

def calculateCost(mat, final) -> int:
	count = 0
	for i in range(n):
		for j in range(n):
			if ((mat[i][j]) and
				(mat[i][j] != final[i][j])):
				count += 1
				
	return count

def newNode(mat, empty_tile_pos, new_empty_tile_pos, level, parent, final) -> node:			
	new_mat = copy.deepcopy(mat)
	x1 = empty_tile_pos[0]
	y1 = empty_tile_pos[1]
	x2 = new_empty_tile_pos[0]
	y2 = new_empty_tile_pos[1]
	new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]
	cost = calculateCost(new_mat, final)
	new_node = node(parent, new_mat, new_empty_tile_pos, cost, level)
	return new_node

def printMatrix(mat):
	for i in range(n):
		for j in range(n):
			print(mat[i][j], end = " ")
			
		print()

def isSafe(x, y):	
	return x >= 0 and x < n and y >= 0 and y < n

def printPath(root):	
	if root == None:
		return
	
	printPath(root.parent)
	printMatrix(root.mat)
	print()

def solve(initial, empty_tile_pos, final):
	pq = priorityQueue()
	cost = calculateCost(initial, final)
	root = node(None, initial,
				empty_tile_pos, cost, 0)

	pq.push(root)

	while not pq.empty():
		minimum = pq.pop()
		if minimum.cost == 0:
			printPath(minimum)
			return

		for i in range(4):
			new_tile_pos = [
				minimum.empty_tile_pos[0] + row[i],
				minimum.empty_tile_pos[1] + col[i], ]
				
			if isSafe(new_tile_pos[0], new_tile_pos[1]):				
				child = newNode(minimum.mat,
								minimum.empty_tile_pos,
								new_tile_pos,
								minimum.level + 1,
								minimum, final,)

				pq.push(child)

initial = [[ 1, 2, 3 ],
			    [ 5, 6, '_' ],
			    [ 7, 8, 4 ]]

final = [[ 1, 2, 3 ],
		    [ 5, 8, 6 ],
		    [ '_', 7, 4 ]]

empty_tile_pos = [ 1, 2 ]
solve(initial, empty_tile_pos, final)


# Output


''' The code begins by importing the necessary modules and defining the size of the puzzle grid (n) and the possible movements for each tile represented by row and col arrays.
The priorityQueue class is defined to implement a priority queue using a heap.
The node class represents a node in the search tree. Each node contains information such as its parent, the state of the puzzle (mat), the position of the empty tile (empty_tile_pos), the cost, and the level of the node in the search tree.
The calculateCost function calculates the number of misplaced tiles (count) in the current puzzle state compared to the final state.
The newNode function creates a new node by swapping the empty tile position with a neighboring tile. It calculates the cost of the new state and returns the new node.
The printMatrix function is used to print the current state of the puzzle grid.
The isSafe function checks if a given position (x, y) is within the puzzle grid boundaries.
The printPath function prints the path from the initial state to the goal state by recursively traversing the parent nodes.
The solve function takes the initial state of the puzzle, the position of the empty tile, and the final state as input. It initializes a priority queue (pq) and creates the root node using the initial state. The cost of the root node is calculated.
The root node is pushed into the priority queue.
The main loop continues until the priority queue is empty. In each iteration, the node with the minimum cost is popped from the priority queue (minimum).
If the cost of the minimum node is 0, it means the goal state has been reached. The printPath function is called to print the path from the initial state to the goal state.
If the goal state is not reached, the code generates the child nodes by swapping the empty tile with its neighboring tiles (up, left, down, right). It creates a new node for each valid swap and calculates the cost of the new state.
The child nodes are pushed into the priority queue.
The process continues until the goal state is reached or the priority queue is empty.
The code defines the initial and final states of the puzzle and the position of the empty tile.
The solve function is called with the initial state, empty tile position, and final state to solve the 8-puzzle problem.
The code finds the solution path from the initial state to the final state using the A* algorithm and prints each step of the path.  '''
