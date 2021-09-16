import heapq
import sys

input = sys.stdin.readline
N = int(input())
M = int(input())

INF = 987654321
distances = [INF for i in range(N + 1)]
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

start, end = map(int, input().split())

distances[start] = 0


def dijk(graph, start):
    queue = []

    heapq.heappush(queue, [distances[start], start])

    while queue:
        now_distance, now_node = heapq.heappop(queue)

        if now_distance > distances[now_node]:
            continue

        for next_data in graph[now_node]:
            distance = next_data[1] + now_distance
            if distance < distances[next_data[0]]:
                distances[next_data[0]] = distance
                heapq.heappush(queue, [distance, next_data[0]])


dijk(graph, start)
print(distances[end])
