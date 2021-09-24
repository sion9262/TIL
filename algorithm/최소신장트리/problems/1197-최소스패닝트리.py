import sys
input = sys.stdin.readline
V, E = map(int, input().split())
edges = []
parents = [i for i in range(V+1)]
rank = [0 for i in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))


def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parents[root2] = root1
    else:
        parents[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruskal(edges):
    mst = []
    total = 0

    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge

        if find(node_v) != find(node_u):
            union(node_v, node_u)
            total += weight
    return total

print(kruskal(edges))
