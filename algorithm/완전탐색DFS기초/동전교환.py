# 동전교환
import sys

#sys.stdin = open("input.txt", "rt")

"""
첫번째 생각
- 그리디 용법으로 가장 큰 액수 부터 계산하기

하지만 항상 옳은 정답은 아님..

dfs 이용하여 풀이 -> 중복순열과 비슷한 문제
하지만, 시간초과 -> 가지치기

sum + coins[i] 가 타겟보다 크거나
지금까지 추가한 코인 갯수가 정답보다 크면 순회 X
"""


def solve(n, coins, target):
    
    answer = 987654321
    
    coins.sort(reverse=True)

    def dfs(sum, ck):
        nonlocal answer
        if ck >= answer:
            return
        if sum == target:
            answer = min(answer, ck)
        if sum > target:
            return
        else:
            for i in range(n):
                if sum + coins[i] > target:
                    continue
                else:
                    dfs(sum + coins[i], ck+1)
    dfs(0, 0)
    print(answer)






if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    solve(n, coins, target)
