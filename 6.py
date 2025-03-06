def Ford_Bellman(N, edge_list, start_node, finish_node):
    #N - количество вершин
    distances = [float("inf") for _ in range(N)]
    distances[start_node] = 0
    for i in range(N):
        for edge in edge_list:
            if distances[edge[i]] + edge[i+2] < distances[edge[i+1]]:
                distances[edge[i+1]] = distances[edge[i]] + edge[i+2]
    return distances[finish_node]
