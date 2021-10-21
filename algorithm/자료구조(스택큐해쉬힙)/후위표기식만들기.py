# 후위표기식 연산
import sys

#sys.stdin = open("input.txt", "rt")

def solve(lines):
    answer = ""
    stack = []

    for line in lines:
        if line.isdecimal():
            answer += line
        else:
            if line == "(":
                stack.append(line)
            elif line == "*" or line == "/":
                while stack and (stack[-1] == "*" or stack[-1] == "/"):
                    answer += stack.pop()
                stack.append(line)
            elif line == "+" or line == "-":
                while stack and stack[-1] != "(":
                    answer += stack.pop()
                stack.append(line)
            else:
                while stack[-1] != "(":
                    answer += stack.pop()
                stack.pop()
    
    while stack:
        answer += stack.pop()

    return answer

if __name__ == "__main__":
    lines = input()
    answer = solve(lines)
    print(answer)
