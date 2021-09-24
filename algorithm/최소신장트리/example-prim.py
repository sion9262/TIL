from collections import defaultdict
from heapq import *

edges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (7, 'B', 'D'), (8, 'B', 'E'),
    (5, 'C', 'E'),
    (6, 'D', 'F'), (7, 'D', 'E'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

def prim(start_node, edges):
    mst = []
    adjacent_edges = defaultdict(list)
    for weight, node_v, node_u in edges:
        adjacent_edges[node_v].append((weight, node_v, node_u))
        adjacent_edges[node_u].append((weight, node_u, node_v))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, node_v, node_u = heappop(candidate_edge_list)
        if node_u not in connected_nodes :
            connected_nodes.add(node_u)
            mst.append((weight, node_v, node_u))

            for edge in adjacent_edges[node_u]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    return mst


print(prim('A', edges))