# 휴가
import sys

#sys.stdin = open("input.txt", "rt")


def solve(n, scores):
    answer = -1

    def dfs(L, sum):
        nonlocal answer    
        if L == n:
            if sum > answer:
                answer = sum
        else:
            if L+scores[L][0] <= n:
                dfs(L + scores[L][0], sum + scores[L][1])
            dfs(L+1, sum)
    dfs(0, 0)
    print(answer)

if __name__ == "__main__":
    n  = int(input())
    scores = [list(map(int, input().split())) for _ in range(n)]

    solve(n, scores)
 