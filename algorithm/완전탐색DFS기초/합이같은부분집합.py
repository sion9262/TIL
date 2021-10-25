# 합이 같은 부분집합
import sys

#sys.stdin = open("input.txt", "rt")
"""
기존 부분집합 방식을 이용하여 풀이.

개선 방안
현재 i==n 같을 때 다시 for 문을 돌려 원소를 파악하고 있지만.

if i == n :
    if sum == total-sum:
        # 종료
else:
    dfs(i, sum + numbers[i])
    dfs(i, sum)

이런식으로 비교하면 된다.
dfs(i, sum + numbers[i]) // 현재 값을 사용
dfs(i, sum) // 현재 값을 사용안함.
"""
def solve(n, numbers):

    used = [0] * n
    ck = False
    
    def dfs(i):
        nonlocal ck
        
        if i == n:
            sum1 = 0
            sum2 = 0
            for j in range(n):
                if used[j] == 1:
                    sum1 += numbers[j]
                else:
                    sum2 += numbers[j]

            if sum1 == sum2:
                ck = True
        else:
            used[i] = 1
            dfs(i+1)
            used[i] = 0
            dfs(i+1)
    dfs(0)

    if ck :
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    answer = solve(n, numbers)
    print(answer)
