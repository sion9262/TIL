import sys
"""
배열 문제 
ascending 1 ~ 8
descending 8 ~ 1
mixed 순서 상관 X
"""
input = sys.stdin.readline

numbers = list(map(int, input().split()))

ascending = True
descending = True

for i in range(0, len(numbers) - 1):
    if numbers[i] > numbers[i+1]:
        ascending = False
    elif numbers[i] < numbers[i+1]:
        descending = False
if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")
