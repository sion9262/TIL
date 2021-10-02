import sys
"""
첫 배추 발견시 dfs 돌면서 인접 배추 방문 체크
"""
# 재귀 깊이 늘리기
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]


def dfs(i, j):
    visited[i][j] = 1
    for k in range(4):
        nx, ny = i + dx[k], j + dy[k]
        if nx < 0 or nx == M or ny < 0 or ny == N:
            continue
        if MAP[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)


for _ in range(T):
    M, N, K = map(int, input().split())
    cnt = 0
    MAP = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    for _ in range(K):
        i, j = map(int, input().split())
        MAP[i][j] = 1

    for i in range(M):
        for j in range(N):
            if MAP[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1

    print(cnt)