# 수열 추측하기
import sys
import copy

#sys.stdin = open("input.txt", "rt")

"""
파스칼 삼각형을 구하는 방법
이항 계수 이용
b = [1] * n
규칙을 보면
n = 4 일때

3C0, 3C1, 3C2, 3C3 
즉 앞에 숫자는 N-1

1, 3/1, 3*2/2*1, 3*2*1/3*2*1
"""


def solve(n, f):
    
    answer = []
    res = [0] * n
    ck = [0] * (n+1)
    b = [1] * n

    # 이항계수 초기화
    for i in range(1, n):
        b[i] = b[i-1] * (n-i) / i

    def dfs(L):
        nonlocal answer
        # 해당 깊이 까지 왔다면
        if L == n:
            sum = 0
            for i in range(n):
                sum += res[i] * b[i]
            if sum == f:
                for i in range(n):
                    print(res[i], end=" ")
                print("")
                exit()
            
                
        else:
            for i in range(1, n+1):
                if ck[i] == 0:
                    ck[i] = 1
                    res[L] = i
                    dfs(L+1)
                    ck[i] = 0
                
    dfs(0)
    print(answer)

    
    





if __name__ == "__main__":
    n, f = map(int, input().split())
    solve(n, f)
