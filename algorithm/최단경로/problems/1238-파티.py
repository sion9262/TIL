import heapq
import sys
"""
X에서 시작하는 (돌아가는) 값을 구함.
각 노드에서 X까지의 거리를 구함.
X[각 노드] + 각 노드[X] 값이 큰 것을 print
 
"""
input = sys.stdin.readline
INF = 987654321
N, M, X = map(int, input().split())
answer = -1
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijk(graph, start):
    queue = []
    distances = [INF for i in range(N + 1)]
    distances[start] = 0

    heapq.heappush(queue, [0, start])
    while queue:
        now_distance, now_node = heapq.heappop(queue)

        if now_distance > distances[now_node]:
            continue

        for next_data in graph[now_node]:
            distance = next_data[1] + now_distance
            if distance < distances[next_data[0]]:
                distances[next_data[0]] = distance
                heapq.heappush(queue, [distance, next_data[0]])

    return distances


x_start = dijk(graph, X)

for i in range(1, N + 1):
    if i == X: continue
    i_start = dijk(graph, i)
    res = i_start[X] + x_start[i]
    if answer < res: answer = res

print(answer)
