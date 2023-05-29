INF = 9999999
N = 5
G = [[0, 19, 5, 0, 0],
    [19, 0, 5, 9, 2],
    [5, 5, 0, 1, 6],
    [0, 9, 1, 0, 1],
    [0, 2, 6, 1, 0]]

selected_node = [0, 0, 0, 0, 0]
no_edge = 0
minimumCost = 0
selected_node[0] = True

print("Edge : Weight")
while (no_edge < N - 1):
  minimum = INF
  a = 0
  b = 0
  for m in range(N):
    if selected_node[m]:
      for n in range(N):
        if ((not selected_node[n]) and G[m][n]):
          if minimum > G[m][n]:
            minimum = G[m][n]
            a = m
            b = n

  print (" " + str(a) + "-" + str(b) + " " + ":" + " " + str(G[a][b])) 
  minimumCost = minimumCost + G[a][b]
  selected_node[b] = True
  no_edge += 1
print("\nMinimum Spanning Tree: ", minimumCost)

# Output:

'''The code defines a constant INF with a large value (9999999) to represent infinity. This value is used to initialize the minimum variable later.

The variable N represents the number of nodes in the graph. In this case, it is set to 5.

The 2D list G represents the weighted adjacency matrix of the graph. Each element G[i][j] represents the weight of the edge between node i and node j.

The list selected_node is initialized with all elements set to 0, indicating that no nodes have been selected yet.

The variable no_edge keeps track of the number of edges included in the minimum spanning tree. It is initialized to 0.

The variable minimumCost stores the total weight of the minimum spanning tree. It is initialized to 0.

The first node (node 0) is selected by setting selected_node[0] to True.

The code enters a while loop that continues until no_edge reaches N - 1, which is the number of edges in a minimum spanning tree with N nodes.

Inside the while loop, the code searches for the minimum weight edge that connects a selected node with an unselected node.

The variables minimum, a, and b are initialized to INF, 0, and 0, respectively. These variables will store the minimum weight, the nodes connected by the minimum weight edge, and the minimum weight itself.

The code uses nested loops to iterate over all possible edges. The outer loop iterates over the selected nodes, and the inner loop iterates over the unselected nodes.

If an edge between a selected node m and an unselected node n is found (G[m][n] is nonzero), the code checks if the weight of this edge is smaller than the current minimum weight. If so, it updates the minimum, a, and b variables with the new minimum weight and the nodes m and n.

After finding the minimum weight edge, the code prints the edge and its weight.

The minimum weight is added to minimumCost.

The node b is marked as selected by setting selected_node[b] to True.

The number of edges (no_edge) is incremented.

The while loop continues until no_edge reaches N - 1, ensuring that the minimum spanning tree is complete.

Finally, the code prints the total weight of the minimum spanning tree.

In summary, the code uses Prim's algorithm to find the minimum spanning tree of a graph represented by an adjacency matrix. It iteratively selects the minimum weight edge that connects a selected node with an unselected node and includes it in the minimum spanning tree. The process continues until all nodes are selected, and the total weight of the minimum spanning tree is calculated and printed.'''
