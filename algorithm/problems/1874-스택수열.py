import sys

input = sys.stdin.readline

n = int(input())
stack = []
answer = []
cnt = 1

for _ in range(n):
    data = int(input())
    while cnt <= data:
        stack.append(cnt)
        cnt += 1
        answer.append("+")
    if stack[-1] == data:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        exit(0)
print("\n".join(answer))