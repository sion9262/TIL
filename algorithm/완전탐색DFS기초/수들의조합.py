# 수들의 조합
import sys

#sys.stdin = open("input.txt", "rt")

"""
이전 조합방식을 이용
numbers의 인덱스를 맞춰주기 위한 0, 0 삽입
이후 L == K 일때 총 합이 m의 배수인지만 체크
"""


def solve(n, k, numbers, m):
    
    answer = 0
    numbers.insert(0, 0)
    res = [0] * (n+1)
    def dfs(L, s):
        nonlocal answer
        if L == k:
            s = sum(res)
            if s % m == 0:
                answer += 1
        else:
            for i in range(s, n+1):
                res[L] = numbers[i]
                dfs(L+1, i+1)
    
    dfs(0, 1)
    print(answer)

if __name__ == "__main__":
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    m = int(input())
    solve(n, k, numbers, m)
 