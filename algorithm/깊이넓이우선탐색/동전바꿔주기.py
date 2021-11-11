# 동전바꿔주기
import sys

#sys.stdin = open("input.txt", "rt")

"""
L -> 계층
for 문을 통해 0~동전의 갯수까지 순회
coins[L][0] * i 는 i의 따라 
0 -> 사용안함. 1 -> 1개만 사용 ..
"""
def solve(T, k, coins):
    answer = 0
    length = len(coins)
    def dfs(L, sum):
        nonlocal answer
        if sum > T:
            return
        if L == k:
            if sum == T:
                answer += 1
        else:
            for i in range(coins[L][1] + 1):
                dfs(L+1, sum + (coins[L][0] * i))
    dfs(0, 0)
    print(answer)
    
if __name__ == "__main__":
    T  = int(input())
    k = int(input())
    
    coins = [list(map(int, input().split())) for _ in range(k)]
    
    solve(T, k, coins)
 