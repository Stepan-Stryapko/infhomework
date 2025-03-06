def BFS(start_node, adj_list, visited=None):
    queue = [(start_node, 0)]
    if visited is None:
        visited = set()
    while len(queue) > 0:
        curr_node, dist = queue.pop(0)
        visited.add(curr_node)
        for adj_node in adj_list[curr_node]:
            if adj_node not in visited:
                queue.append((adj_node, dist + 1))
    return visited


def count_components(adj_list):
    nodes = set()
    for i in range(len(adj_list)):
        nodes.add(i)
    visited = set()
    x = 0
    while visited != nodes:
        visited = BFS(adj_list((nodes - visited).pop(), adj_list))
        x += 1
    return x



