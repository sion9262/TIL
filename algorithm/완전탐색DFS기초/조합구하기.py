# 조합 구하기
import sys

#sys.stdin = open("input.txt", "rt")

"""
조합은 이전까지 나왔던 것들이 나오면 안됨, 중복 안됨, 순서 상관 없음
"""


def solve(n, m):
    
    answer = 0
    res = [0] * (n+1)
    def dfs(L, s):
        nonlocal answer
        if L == m:
            for j in range(L):
                print(res[j], end=" ")
            print("")
            answer += 1
        else:
            for i in range(s, n+1):
                res[L] = i
                dfs(L+1, i+1)
    
    dfs(0, 1)
    print(answer)

if __name__ == "__main__":
    n, m = map(int, input().split())
    solve(n, m)
 