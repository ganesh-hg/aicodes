def aStarAlgo (start_node, stop_node):
  open_set = set(start_node)
  closed_set = set()
  g = {} 
  parents = {}
  g[start_node] = 0
  parents[start_node] = start_node
  while len (open_set) > 0:
    n= None
    for v in open_set:
      if n == None or g[v] + heuristic(v) < g[n] + heuristic (n):
        n = v
    if n == stop_node or Graph_nodes[n] == None:
      pass
    else:
      for (m, weight) in get_neighbors(n):
        if m not in open_set and m not in closed_set:
          open_set.add(m)
          parents[m] = n
          g[m] = g[n] + weight
        else:
          if g[m] > g[n] + weight:
            g[m] = g[n] + weight
            parents [m] = n
            if m in closed_set:
              closed_set.remove(m) 
              open_set.add(m)

    if n == None :
      print('Path does not exist!')
      return None
    if n == stop_node:
      path = []
      while parents[n] != n:
        path.append(n)
        n = parents[n]
      path.append(start_node)
      path.reverse()
      print('Path found:')
      return path
    open_set.remove(n)
    closed_set.add(n)

def get_neighbors (v):
  if v in Graph_nodes:
    return Graph_nodes[v]
  else:
    return None

def heuristic(n):
  H_dist = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0,
  }
  return H_dist[n]

Graph_nodes = {
  'A': [('B', 2), ('E', 3)],
  'B': [('C', 1),('G', 9)], 
  'C': None,
  'E': [('D', 6)],
  'D': [('G', 1)],
}

aStarAlgo('A', 'G')

# Output:


''' The aStarAlgo function takes a start_node and a stop_node as input and performs the A* algorithm to find the shortest path. It initializes an open_set with the start_node and an empty closed_set.
It initializes dictionaries g and parents to keep track of the cost from the start node (g) and the parent nodes (parents) of each node in the graph. It sets the cost of the start_node to 0 and assigns itself as its parent.
The main loop runs as long as there are nodes in the open_set.
Inside the loop, it selects the node n with the lowest g value plus the heuristic value using the heuristic function. The heuristic function provides an estimated distance from n to the stop_node.
If the selected node n is the stop_node or there are no neighbors for n in the Graph_nodes, it proceeds to the next iteration.
Otherwise, it iterates over the neighbors of n using the get_neighbors function.
For each neighbor m and its corresponding weight, it checks if m is not in the open_set and not in the closed_set. If so, it adds m to the open_set, assigns n as its parent, and calculates its g value by adding the weight to the g value of n.
If m is already in the open_set or closed_set, it checks if the new path to m has a lower g value. If so, it updates the g value and assigns n as its parent. If m is in the closed_set, it removes it from the closed_set and adds it back to the open_set to consider the updated g value.
If no path is found (n is None), it prints "Path does not exist!" and returns None.
If the stop_node is reached, it reconstructs the path by following the parents dictionary from the stop_node to the start_node. The path is reversed and returned.
Finally, the selected n is removed from the open_set and added to the closed_set.
The get_neighbors function returns the neighbors of a given node v from the Graph_nodes dictionary. If v is not found in Graph_nodes, it returns None.
The heuristic function returns a heuristic value for a given node n. In this code, it uses a pre-defined dictionary H_dist that assigns heuristic values to specific nodes.
The Graph_nodes dictionary represents the graph where the keys are nodes, and the values are lists of tuples representing the neighbors and their corresponding weights. '''
