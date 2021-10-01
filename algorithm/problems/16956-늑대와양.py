import sys
"""
좌표 문제
MAP dx, dy [0, 1, 0, 1], [-1, 0, 1, 0]
nx, ny를 구해 조건에 맞춰 판단.
for i in range(4):
    nx, ny = i + dx[k], j + dy[k]
    if nx < 0 or ny < 0 or nx == R or ny == C:
        continue
최소 울타리를 구하는 게 아니므로
늑대와 양이 아니면 D로 변환.
"""
input = sys.stdin.readline
R, C = map(int, input().split())
M = [list(input()) for _ in range(R)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 1

for i in range(R):
    for j in range(C):
        if M[i][j] == "W":
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if nx < 0 or ny < 0 or nx == R or ny == C:
                    continue
                if M[nx][ny] == 'S':
                    answer = 0

if answer == 0:
    print(answer)
else:
    print(answer)

    for i in range(R):
        for j in range(C):
            if M[i][j] not in "SW":
                M[i][j] = "D"

    for i in M:
        print(''.join(i))
