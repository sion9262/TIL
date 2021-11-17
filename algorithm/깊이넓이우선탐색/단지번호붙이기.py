# 단지 번호 붙이기(DFS, BFS)
import sys
#sys.stdin = open("input.txt", "rt")

"""
visited -> n * n

이중 포문으로 조건 체크
1. 이미 방문한 적이 있는가
2. 집이 없는 곳인가
-> 아니면 dfs순회
-> 1개의 그룹 생성

dfs
해당 지점부터 연결되있는 모든 집을 순회
"""



def solve(n, maps):
    answer = 0
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    visited = [[0] * n for _ in range(n)]
    groups = []
    def dfs(x, y):
        group = 1
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if maps[nx][ny] == 0:
                continue
            group += dfs(nx, ny)
        return group

    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                continue
            if maps[x][y] == 0:
                continue
            groups.append(dfs(x, y))
            answer += 1
    print(answer)
    groups.sort()
    for group in groups:
        print(group)

if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input())) for _ in range(n)]
    solve(n, maps)
 