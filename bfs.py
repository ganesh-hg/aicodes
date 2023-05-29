graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)
    print(m, end='\n')

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("BFS:")
bfs(visited, graph, '5')


'''The code defines a dictionary called graph that represents an undirected graph. Each key in the dictionary corresponds to a node in the graph, and the associated value is a list of its neighboring nodes. The graph is represented using an adjacency list.

The code initializes two empty lists: visited and queue. The visited list keeps track of the nodes that have been visited during the BFS traversal, and the queue list is used to store the nodes that are yet to be explored.

The bfs function takes three parameters: visited, graph, and node. It performs the following steps:

It starts by appending the node parameter to the visited list and the queue list.
It enters a while loop that continues until the queue is empty. This loop is the core of the BFS algorithm.
Inside the loop, it pops the first element from the queue using queue.pop(0) and assigns it to the variable m.
It then prints the value of m, which represents the node being visited, using print(m, end='\n').
Next, it iterates over the neighbors of m by accessing the corresponding list in the graph dictionary using graph[m].
For each neighbor neighbour in the list, it checks if neighbour has not been visited. If neighbour is not in the visited list, it appends neighbour to both the visited list and the queue list. This ensures that unvisited neighbors are added to the queue for further exploration.
The code includes an example usage part where the bfs function is called with an initial node '5' to perform a BFS traversal of the graph. The traversal starts from node '5' and visits all connected nodes in a breadth-first manner.

During the BFS traversal, each visited node is printed on a new line using print(m, end='\n').

Overall, the code demonstrates a basic implementation of the BFS algorithm for traversing a graph represented by an adjacency list. It explores the graph in a breadth-first manner, visiting all the nodes reachable from the initial node and printing them in the order they are encountered.'''
