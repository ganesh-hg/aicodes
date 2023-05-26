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

#Output