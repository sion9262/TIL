# 중복순열 구하기
import sys

#sys.stdin = open("input.txt", "rt")

"""
L = 깊이 체크
dfs(0) -> for문으로 1~n까지 loop
L == m 깊이가 같다면 res에 저장된 변수를 출력
"""


def solve(n, m):
    
    res = [0] * m
    answer = 0

    def dfs(L):
        nonlocal answer
        if L == m:
            for i in range(L):
                print(res[i], end=" ")
            print()
            answer += 1
        else:
            for i in range(1, n+1):
                res[L] = i
                dfs(L+1)

    dfs(0)
    print(answer)






if __name__ == "__main__":
    n, m = map(int, input().split())
    solve(n, m)
