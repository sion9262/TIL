import sys
sys.stdin = open("input.txt", "rt")

"""
K번째 약수
n의 약수들 중 k번째 작은 수를 출력하라.
만약 약수의 개수가 k개보다 작으면 -1을 출력하라
"""
n, k = map(int, input().split())

def solve(n, k):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
        if cnt == k:
            return i
    return -1

print(solve(n, k))

