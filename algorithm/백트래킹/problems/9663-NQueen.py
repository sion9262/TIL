import sys
"""
Queen은 수직, 수평, 대각선 이동 가능
"""
input = sys.stdin.readline

N = int(input())

def dfs(queen, row, N):
    count = 0
    # 현재 배열, N
    count = 0
    if N == row:
        return 1
    for col in range(N):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i]-queen[row]) == row - i:
                break
        else:
            # break로 끊기지 않고 끝까지 간경우 실행
            count += dfs(queen, row + 1, N)
    return count

queen = [0] * N
print(dfs(queen, 0, N))
