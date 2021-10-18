# 쇠막대기
import sys
#sys.stdin = open("input.txt", "rt")

"""
내 생각 

stack은 현 상태에서의 쇠막대기의 갯수 

괄호 ( 가 들어올 때 stack += 1

괄호 ) 가 들어올 때 
stack -= 1
이전 ( 가 들어왔으면 레이저 -> answer += stack 
이전이 ) 면 쇠막대기의 끝을 알림 -> answer += 1
"""

def solve(lines):
    answer = 0

    stack = 0
    prev = "("
    for line in lines:
        # 쇠막대기 시작
        if line == "(":
            stack += 1
            prev = "("
        else:
            # 쇠막대기 끝
            stack -= 1
            if prev == "(":
                answer += stack
            else:
                answer += 1
            prev = ")"

    return answer

if __name__ == "__main__":
    lines = input()
    answer = solve(lines)
    print(answer)
