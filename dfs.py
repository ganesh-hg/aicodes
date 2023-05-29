graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = []

def dfs(visited, graph, node):
  if node not in visited:
    print(node)
    visited.append(node)
    for neighbour in graph[node]:
      dfs(visited, graph, neighbour)

print("DFS:")
dfs(visited, graph, '5')

# Output:

'''  The code defines a graph using a dictionary called graph, where the keys represent nodes in the graph, and the values are lists of adjacent nodes.

An empty list visited is initialized to keep track of the visited nodes during the DFS traversal.

The dfs function is defined to perform the DFS traversal. It takes three parameters: visited (the list of visited nodes), graph (the adjacency list representation of the graph), and node (the current node being visited).

Inside the dfs function, there is a base condition that checks if the current node is not in the visited list. If it's not visited, it means we have encountered a new node.

The new node is then printed (print(node)) to show the order in which nodes are visited during the DFS traversal. This line can be modified or removed depending on how you want to use the DFS traversal.

The current node is then added to the visited list to mark it as visited.

The function then recursively calls itself for each neighbor of the current node (obtained from the graph dictionary). This recursive call is made only for unvisited neighbors.

The DFS traversal starts by calling the dfs function with the initial node to begin the traversal. In this case, it starts with node '5'.

The output will be the order in which nodes are visited during the DFS traversal.

In summary, the code performs a Depth-First Search (DFS) traversal on a graph represented as an adjacency list. It visits each node in the graph and explores its neighbors recursively until all reachable nodes are visited. The output shows the order in which nodes are visited during the DFS traversal, starting from the given initial node. '''
