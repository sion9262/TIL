# 알파코드(DFS)
import sys

#sys.stdin = open("input.txt", "rt")

"""
A~Z 1~26
해당 조건은 2가지가 있다.
1. 한자리만 사용하기 1~9
2. 두자리만 사용하기 10~26

공통 조건 0 -> 10 20 만 가능
두자리일 경우 26을 초과해서는 안됨.
"""

def parse_string(num):
    return chr(65 + int(num) - 1)

def solve(string):
    
    answer = 0
    n = len(string)

    def dfs(L, sum):
        nonlocal answer
        if L == n:
            print(sum)
            answer += 1
        else:
            if string[L] == '0':
                pass
            elif L+1 == n:
                dfs(L+1, sum + parse_string(string[L]))
            else:
                dfs(L+1, sum + parse_string(string[L]))
                if int(string[L:L+2]) > 26:
                    pass
                else:
                    dfs(L+2, sum + parse_string(string[L:L+2]))
    dfs(0, '')
    print(answer)
    
if __name__ == "__main__":

    string  = input()
    solve(string)
 