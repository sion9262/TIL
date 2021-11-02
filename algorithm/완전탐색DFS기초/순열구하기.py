# 순열 교환
import sys

#sys.stdin = open("input.txt", "rt")

"""
중복 순열과 다르게 해당 배열에 자기 자신이 있다면 continue
-> 이때 [2, 3] 이후 res[0] 의 3이되는데 뒤에 3이 있어서 오류 발생
따라서 깊이가 L ~ M 까지 배열을 0으로 초기화 해야함.

다른 풀이
ck = [0] * n+1 
ck == 0 일때만 값을 추가할 수 있게함.
ck[i] = 1
res[L] = i
dfs(L+1)
ck[i] = 0 
... 와 같은 방식으로
"""


def solve(n, m):
    
    answer = 0 
    res = [0] * m
    
    def dfs(L):
        nonlocal answer
        # 해당 깊이 까지 왔다면
        if L == m:
            for i in range(m):
                print(res[i], end=" ")
            print("")
            answer += 1
        else:
            for i in range(1, n+1):
                for j in range(L, m):
                    res[j] = 0 
                if i in res:
                    continue
                else:
                    
                    res[L] = i

                    dfs(L+1)
    dfs(0)
    print(answer)

    
    





if __name__ == "__main__":
    n, m = map(int, input().split())
    solve(n, m)
