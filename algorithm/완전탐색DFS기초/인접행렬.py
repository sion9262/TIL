# 인접행렬(가중치 방향그래프)
import sys

sys.stdin = open("input.txt", "rt")

"""
 n+1 by n+1 배열 생성
 해당 maps[v1][v2] = w
"""


def solve(n, m, edges):
    
    maps = [[0] * (n+1) for _ in range(n+1)]

    for edge in edges:
        maps[edge[0]][edge[1]] = edge[2]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(maps[i][j], end=" ")
        print()
if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    solve(n, m, edges)
 