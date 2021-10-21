# 공주 구하기
import sys

#sys.stdin = open("input.txt", "rt")

def solve(n, k):
    
    numbers = [i+1 for i in range(n)]

    while True:
        if len(numbers) == 1 : return numbers[0]
        for i in range(k-1):
            numbers.append(numbers.pop(0))
        numbers.pop(0)
    


if __name__ == "__main__":
    n, k = map(int, input().split())
    answer = solve(n, k)
    print(answer)
