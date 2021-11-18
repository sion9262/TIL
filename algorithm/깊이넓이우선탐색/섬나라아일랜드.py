# 섬나라 아일랜드(BFS 활용)
import sys
#sys.stdin = open("input.txt", "rt")

"""
BFS를 활용하여 순회하는데
대각선 여부까지 체크
"""



def solve(n, maps):
    answer = 0
    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]

    visited = [[0] * n for _ in range(n)]
    def bfs(x, y):
        visited[x][y] = 1
        queue = [(x, y)]

        while queue:
            x, y = queue.pop(0)
            for i in range(8):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue
                if maps[nx][ny] == 0:
                    continue
                queue.append((nx, ny))
                visited[nx][ny] = 1

    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                continue
            if maps[x][y] == 0:
                continue
            bfs(x, y)
            answer += 1
    print(answer)

if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    solve(n, maps)
 