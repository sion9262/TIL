# 사과나무(BFS)
import sys
import queue
#sys.stdin = open("input.txt", "rt")

"""
가운데 부터 상하좌우를 보면서 감.
깊이는 n//2 까지 가야함.
"""


def solve(n, maps):
    answer = 0
    q = queue.Queue()
    visited = [[0] * n for _ in range(n)]
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    start = n // 2
    q.put((start, start))
    answer += maps[start][start]
    visited[start][start] = 1
    L = 0
    while True:
        if L == n // 2:
            break
        
        size = q.qsize()
        # size를 사전에 받는 이유는. -> 계속 추가되면 안되기때문.
        for _ in range(size):
            x, y = q.get()
            
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]

                if visited[nx][ny] == 1:
                    continue
                else:
                    visited[nx][ny] = 1
                    answer += maps[nx][ny]
                    q.put((nx, ny))
        L += 1

    print(answer)

if __name__ == "__main__":

    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    solve(n, maps)
 