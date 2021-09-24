graph = {
    'vetices' : ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges' : [
        (7, 'A', 'B'), (5, 'A', 'D'),
        (7, 'B', 'A'), (8, 'B', 'C'), (7, 'B', 'D'), (8, 'B', 'E'),
        (8, 'C', 'B'), (5, 'C', 'E'),
        (5, 'D', 'A'), (9, 'D', 'B'), (6, 'D', 'F'), (7, 'D', 'E'),
        (7, 'E', 'B'), (5, 'E', 'C'), (7, 'E', 'D'), (8, 'E', 'F'), (9, 'E', 'G'),
        (6, 'F', 'D'), (8, 'F', 'E'), (11, 'F', 'G'),
        (9, 'G', 'E'), (11, 'G', 'F')
    ]
}
# 각각의 노드의 부모노드 값을 저장
parent = {}
# 각각의 노드의 번호
rank = {}

def make_set(node):
    parent[node] = node
    rank[node] = 0

# path compression
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]
# union-by-rank
def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def kruskal(graph):
    mst = []

    # union-bt-rank 쓰기 위한 초기화
    for node in graph['vetices']:
        make_set(node)

    # 가중치가 작은 순으로 정렬
    edges = graph['edges']
    edges.sort()

    # 간선 연결
    for edge in edges:
        weight, node_v, node_u = edge
        # 사이클을 확인 후 같지않다면 합침
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)
    return mst

print(kruskal(graph))
print(parent)
print(rank)