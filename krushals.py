graph = []
V = 4

def addEdge(u, v, w):
    graph.append([u, v, w])

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def KruskalMST():
    result = []
    i = 0
    e = 0
    graph.sort(key=lambda item: item[2])
    parent = []
    rank = []
    for node in range(V):
        parent.append(node)
        rank.append(0)

    while e < V - 1:
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)

    minimumCost = 0
    print("Edge : Weight")    
    for u, v, weight in result:
        minimumCost += weight
        print (" " + str(u) + "-" + str(v) + " " + ":" + " " + str(weight)) 
    print("\nMinimum Spanning Tree: ", minimumCost)
 
addEdge(0, 1, 10)
addEdge(0, 2, 6)
addEdge(0, 3, 5)
addEdge(1, 3, 15)
addEdge(2, 3, 4)

KruskalMST()

#Output

''' The code initializes an empty list graph to store the edges of the graph and sets the number of vertices V to 4.

The addEdge function is defined to add an edge to the graph. It takes three parameters: the source vertex u, the destination vertex v, and the weight w of the edge. It appends the edge information as a list [u, v, w] to the graph list.

The find function is a helper function for finding the parent of a vertex in a disjoint set. It uses the path compression technique to optimize the find operation. It takes the parent array and a vertex i as parameters and recursively finds the parent of i. It also performs path compression by updating the parent of i to the root parent.

The union function is a helper function for performing the union operation of two sets. It takes the parent array, rank array, two vertices x and y, and merges the sets containing x and y. It uses the rank array to optimize the union operation by attaching the smaller rank tree to the root of the higher rank tree.

The KruskalMST function implements Kruskal's algorithm to find the Minimum Spanning Tree. It initializes an empty list result to store the edges of the MST.

The graph list is sorted in non-decreasing order based on the edge weights using the sort method and a lambda function as the key.

The parent and rank lists are initialized for the disjoint set data structure. Each vertex is initially its own parent, and the rank is set to 0.

The algorithm iterates through each edge in the sorted graph list. It checks if the source vertex u and destination vertex v are in different sets (i.e., they have different parents). If they are in different sets, it means adding the edge (u, v) to the MST will not create a cycle.

If u and v are in different sets, the edge is added to the result list, and the union operation is performed to merge the sets containing u and v.

The algorithm continues this process until it has added V - 1 edges to the result list, where V is the number of vertices in the graph.

The total weight of the MST is calculated by summing the weights of all the edges in the result list.

The code then prints the edges and their weights in the MST using a loop over the result list.

Finally, it prints the minimum cost of the MST.

The addEdge function is called to add edges to the graph.

The KruskalMST function is called to find the MST and print the results.

In summary, the code demonstrates the implementation of Kruskal's algorithm to find the Minimum Spanning Tree of a graph. It uses a disjoint set data structure to efficiently check for cycles and merge sets during the process. The resulting MST is printed along with its minimum cost.'''
