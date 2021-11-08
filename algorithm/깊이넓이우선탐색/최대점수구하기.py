# 최대 점수 구하기
import sys

#sys.stdin = open("input.txt", "rt")


def solve(n, m, scores):
    answer = -1

    def dfs(L, sum, time):
        nonlocal answer    
        if time > m:
            return
        if L == n:
            if sum > answer:
                answer = sum
        else:
            # 부분집합에 넣은 경우
            dfs(L+1, sum+scores[L][0], time+scores[L][1])
            # 넣지 않았을 떄
            dfs(L+1, sum, time)
    dfs(0, 0, 0)
    print(answer)

if __name__ == "__main__":
    n, m = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(n)]

    solve(n, m, scores)
 