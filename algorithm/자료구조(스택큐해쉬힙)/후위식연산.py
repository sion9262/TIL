# 후위표기식 연산
import sys

#sys.stdin = open("input.txt", "rt")

def solve(lines):
    stack = []

    for line in lines:
        if line.isdecimal():
            stack.append(line)
        else:
            num = 0
            num1 = stack.pop()
            num2 = stack.pop()
            if line == "+":   
                num = int(num1) + int(num2)
            if line == "-":   
                num = int(num2) - int(num1)
            if line == "*":   
                num = int(num1) * int(num2)
            if line == "/":   
                num = int(num2) / int(num1)
            stack.append(num)

    return stack[0]

if __name__ == "__main__":
    lines = input()
    answer = solve(lines)
    print(answer)
