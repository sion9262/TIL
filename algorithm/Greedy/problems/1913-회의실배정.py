"""
풀이
    1. 회의 시간이 빠른 순이 아니라 빨리 끝나는 순으로 정렬해야한다.
    2. 회의가 끝나는 시간과 시작하는 순간은 같거나 커야한다.
"""
answer = 0
N = int(input())
plans = []

for _ in range(N):
    start, end = map(int, input().split())
    plans.append((start, end))

# 끝나는 시간이 가장 작은 회의순으로 정렬
plans = sorted(plans, key=lambda x : (x[1], x[0]))

time = 0

for plan in plans:
    if plan[0] >= time:
        time = plan[1]
        answer += 1

print(answer)