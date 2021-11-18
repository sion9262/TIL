# 안전영역(BFS)
import sys
sys.stdin = open("input.txt", "rt")

"""
1. 우선 BFS 사용 1~max_height까지 돌아보기
시간복잡도면에서 이분탐색을 이용하면 더 빠를것 같음.

"""



def solve(n, maps):
    answer = 0
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

    max_height = 0
    for map in maps:
        max_height = max(max_height, max(map))
    
    def bfs(x, y, target):
        visited[x][y] = 1
        queue = [(x, y)]

        while queue:
            x, y = queue.pop(0)
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if visited[nx][ny]:
                    continue
                if maps[nx][ny] <= target:
                    continue
                queue.append((nx, ny))
                visited[nx][ny] = 1

    for i in range(1, max_height+1):
        visited = [[0] * n for _ in range(n)]
        cnt = 0
        for x in range(n):
            for y in range(n):
                if visited[x][y]:
                    continue
                if maps[x][y] <= i:
                    continue
                bfs(x, y, i)
                cnt += 1
        answer = max(answer, cnt)
                
    print(answer)

if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]
    solve(n, maps)
 