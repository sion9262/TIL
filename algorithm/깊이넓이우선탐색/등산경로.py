# 등산경로 (DFS)
import sys
#sys.stdin = open("input.txt", "rt")

"""
1. 최소 최대 높이 구하기.
2. DFS 실행
    max_point 까지.

"""



def solve(n, maps):
    answer = 0
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    min_value, max_value = 9875654321, -1
    max_point_x, max_point_y = 0, 0
    min_point_x, min_point_y = 0, 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] > max_value:
                max_value = maps[i][j]
                max_point_x = i
                max_point_y = j
            if maps[i][j] < min_value:
                min_value = maps[i][j]
                min_point_x = i
                min_point_y = j


    def dfs(x, y):
        nonlocal answer
        if x == max_point_x and y == max_point_y:
            answer += 1
        else:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if maps[x][y] >= maps[nx][ny]:
                    continue
                dfs(nx, ny)

    dfs(min_point_x, min_point_y)
    
    print(answer)

if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    solve(n, maps)
 