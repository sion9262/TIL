# 동전분배하기
import sys

#sys.stdin = open("input.txt", "rt")

"""
L == n 까지 순회
같으면 총액비교후 서로 다르면 최대 - 최소 가 answer 작은지 확인 후 대입
"""
def solve(n, coins):
    answer = 987654321
    ck = [0] * 3
    def dfs(L, ck):
        nonlocal answer
        if L == n:
            # 세 사람의 총액은 서로 달라야함.
            if ck[0] != ck[1] and ck[0] != ck[2] and ck[1] != ck[2]:
                answer = min(answer, max(ck) - min(ck))    
        else:
            ck[0] += coins[L]
            dfs(L+1, ck)
            ck[0] -= coins[L]
            ck[1] += coins[L]
            dfs(L+1, ck)
            ck[1] -= coins[L]
            ck[2] += coins[L]
            dfs(L+1, ck)
            ck[2] -= coins[L]
    dfs(0, ck)
    print(answer)
    
if __name__ == "__main__":
    n  = int(input())
    
    coins = [int(input()) for _ in range(n)]
    solve(n, coins)
 