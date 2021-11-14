# 미로 탐색 (DFS)
import sys
#sys.stdin = open("input.txt", "rt")

"""
재귀 돌릴때 maps[nx][ny] = 1으로 두어 벽이라 인식하게하기
돌린 후 다시 maps[nx][ny] = 0으로 두어 복구
"""



def solve(maps):
    answer = 0
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    def dfs(x, y):
        nonlocal answer
        if x == 6 and y == 6:
            answer += 1
        else:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0<=nx<=6 and 0<=ny<=6 and maps[nx][ny] == 0:
                    maps[nx][ny] = 1
                    dfs(nx, ny)
                    maps[nx][ny] = 0
    maps[0][0] = 1
    dfs(0, 0)
    print(answer)

if __name__ == "__main__":

    maps = [list(map(int, input().split())) for _ in range(7)]
    solve(maps)
 