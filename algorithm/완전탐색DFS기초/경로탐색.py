# 경로탐색 (그래프 dfs)
import sys

#sys.stdin = open("input.txt", "rt")

"""
인접행렬 생성
방문체크 visited
"""


def solve(n, m, edges):
    answer = 0
    maps = [[0] * (n+1) for _ in range(n+1)]
    visited = [0] * (n+1)

    for edge in edges:
        maps[edge[0]][edge[1]] = 1

    def dfs(v):
        nonlocal answer
        if v == n:
            answer +=1
        else:
            for i in range(1, n+1):
                if maps[v][i] == 1 and visited[i] == 0:
                    visited[i] = 1
                    dfs(i)
                    visited[i] = 0
    visited[1] = 1
    dfs(1)
    print(answer)

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    solve(n, m, edges)
 