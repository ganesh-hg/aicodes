V = 4
m = 3
graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]

def isSafe(v, colour, c):
    for i in range(V):
        if graph[v][i] == 1 and colour[i] == c:
            return False
    return True

def graphColourUtil(m, colour, v):
    if v == V:
        return True

    for c in range(1, m + 1):
        if isSafe(v, colour, c) == True:
            colour[v] = c
            if graphColourUtil(m, colour, v + 1) == True:
                return True
            colour[v] = 0

def graphColouring(m):
    colour = [0] * V
    if graphColourUtil(m, colour, 0) == None:
        return False
    print("Solution exist and Following are the assigned colours:")
    for c in colour:
        print(c, end=' ')
    return True

graphColouring(m)

#Output

''' The code starts by defining the number of vertices V and the number of colors m.

The graph is a 2D list representing the adjacency matrix of the graph. It indicates whether there is an edge between two vertices. graph[i][j] is 1 if there is an edge between vertex i and vertex j, and 0 otherwise.

The function isSafe checks if it is safe to assign color c to vertex v by checking if any adjacent vertices already have the same color. It iterates over all the vertices and checks if there is an edge between v and the current vertex i and if the color of vertex i is already c. If such an adjacent vertex exists, it means assigning color c to v would violate the graph coloring constraint, so it returns False. Otherwise, it returns True.

The function graphColourUtil is a recursive function that tries to assign colors to vertices one by one. It starts with vertex v = 0 and tries all possible colors c from 1 to m. For each color c, it checks if it is safe to assign that color to the current vertex v using the isSafe function. If it is safe, it assigns color c to v and recursively calls graphColourUtil for the next vertex v + 1. If this recursive call returns True, it means a valid coloring has been found, and it returns True. If the recursive call returns False, it means the current color c doesn't lead to a valid coloring, so it backtracks by resetting the color of v to 0 and tries the next color.

The function graphColouring initializes an array colour of size V to store the assigned colors for each vertex. It calls the graphColourUtil function with m colors, starting from vertex 0. If graphColourUtil returns None, it means a valid coloring doesn't exist, so it returns False. Otherwise, it prints the assigned colors for each vertex.

The graphColouring function is called with m = 3 to find a valid coloring using 3 colors.

If a valid coloring exists, it prints "Solution exists and Following are the assigned colors:" followed by the assigned colors for each vertex.

In summary, the code solves the graph coloring problem by assigning colors to the vertices of a graph in such a way that no two adjacent vertices have the same color. It uses backtracking to explore different color assignments and checks if each assignment is valid using the isSafe function. The output shows whether a valid coloring exists and, if so, the assigned colors for each vertex. '''
