# 미로의 최단거리 통로(BFS)
import sys
import queue
#sys.stdin = open("input.txt", "rt")

"""
L -> 계층 정보
visited -> 987654321로 설정해서 그것보다 작으면 L대입.
qsize -> 0 이 될떄까지 순회
"""


def solve(maps):
    answer = 0
    q = queue.Queue()
    n = len(maps)
    visited = [[987654321] * n for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    visited[0][0] = 0
    q.put((0, 0))
    L = 1
    while q.qsize():
        size = q.qsize()
        for _ in range(size):
            x, y = q.get()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if maps[nx][ny] == 1:
                    continue
                if visited[nx][ny] > L:
                    visited[nx][ny] = L
                    q.put((nx, ny))
        L += 1
    
    if visited[n-1][n-1] == 987654321:
        print("-1")
    else:
        print(visited[n-1][n-1])

if __name__ == "__main__":

    maps = [list(map(int, input().split())) for _ in range(7)]
    solve(maps)
 