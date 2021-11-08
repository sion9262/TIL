# 양팔저울
import sys

#sys.stdin = open("input.txt", "rt")

"""
저울에 넣을 수 있는건 3가지 방법
1. 왼쪽에 넣어서 +
2. 오른쪽에 넣어서 -
3. 안넣어서 0

set 자료형을 써서 중복을 제거
음수일 때는 굳이 안넣어도 된다.
정답은 모든 무게의 합 - answer의 갯수
"""

def solve(n, weights):
    answer = set()

    def dfs(L, sum):  
        if L == n:
            if 0 < sum:
                answer.add(sum)

        else:
            dfs(L+1, sum+weights[L])
            dfs(L+1, sum-weights[L])
            dfs(L+1, sum)

    dfs(0, 0)
    print(sum(weights) - len(answer))

if __name__ == "__main__":
    n  = int(input())
    weights = list(map(int, input().split()))

    solve(n, weights)
 