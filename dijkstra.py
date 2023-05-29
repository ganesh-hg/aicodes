V = 9
graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]]

def printSolution(dist):
    print("Vertex \t Distance from Source")
    for node in range(V):
        print(node, "\t\t", dist[node])

def minDistance(dist, sptSet):
    min = 1e7
    for v in range(V):
        if dist[v] < min and sptSet[v] == False:
            min = dist[v]
            min_index = v

    return min_index

def dijkstra(src):
    dist = [1e7] * V
    dist[src] = 0
    sptSet = [False] * V

    for cout in range(V):
        u = minDistance(dist, sptSet)
        sptSet[u] = True
        for v in range(V):
            if (graph[u][v] > 0 and
                sptSet[v] == False and
                dist[v] > dist[u] + graph[u][v]):
                dist[v] = dist[u] + graph[u][v]

    printSolution(dist)
 
dijkstra(0)

''' The code starts by defining the number of vertices V and the graph graph as a 2D list. Each element graph[u][v] represents the weight of the edge between vertex u and vertex v. If there is no direct edge between two vertices, the weight is set to 0.

The printSolution function is used to print the shortest distances from the source vertex to all other vertices. It iterates over each vertex and prints the vertex index along with its distance from the source.

The minDistance function finds the vertex with the minimum distance value from the set of vertices not yet included in the shortest path tree (sptSet). It iterates over all vertices and checks if the distance of vertex v is smaller than the current minimum (min) and if the vertex v is not already included in the shortest path tree (sptSet[v] == False). If both conditions are met, it updates the minimum value and stores the index of the vertex with the minimum distance.

The dijkstra function implements the main logic of Dijkstra's algorithm. It initializes the distance array dist with a large value (1e7) for all vertices except the source vertex, which is set to 0. It also initializes the shortest path tree set sptSet as a boolean array with all values set to False.

The algorithm iterates V times, where V is the number of vertices in the graph. In each iteration, it selects the vertex u with the minimum distance value from the set of vertices not yet included in the shortest path tree (using the minDistance function). It marks the selected vertex u as included in the shortest path tree by setting sptSet[u] to True.

For each vertex v adjacent to u (where there is an edge between u and v with a non-zero weight), the algorithm checks if including vertex v in the shortest path gives a shorter path to v than the current distance stored in dist[v]. If it does, the distance value is updated to the new shorter distance dist[u] + graph[u][v].

After the algorithm completes, the printSolution function is called to print the shortest distances from the source vertex to all other vertices.

The dijkstra function is called with the source vertex src set to 0.

In summary, the code implements Dijkstra's algorithm to find the shortest path from a source vertex to all other vertices in a weighted graph. It maintains a set of vertices included in the shortest path tree and updates the distance values of adjacent vertices if a shorter path is found. The output shows the shortest distances from the source vertex to all other vertices in the graph. '''

#Output
