import heapq

graph = {
    'A' : {'B' : 8, 'C' : 1, 'D' : 2},
    'B' : {},
    'C' : {'B' : 5, 'D' : 2},
    'D' : {'E' : 3, 'F' : 5},
    'E' : {'F' : 1},
    'F' : {'A' : 5}
}

def dijksta(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []

    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue
        for node, distance in graph[current_node].items():
            new_distance = current_distance + distance
            if new_distance < distances[node]:
                distances[node] = new_distance
                heapq.heappush(queue, [new_distance, node])
    return distances
print(dijksta(graph, 'A'))