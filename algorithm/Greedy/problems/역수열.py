
# 역수열(그리디)


import sys
#sys.stdin = open("input.txt", "rt")

"""
생각한 것
- 큰 것부터 집어넣는다.
"""
def solve(numbers, n):
    answer = []
    
    for i in range(n-1, -1, -1):
        if numbers[i] == 0:
            answer.insert(0, i + 1)
            continue
        else:
            answer.insert(numbers[i], i + 1)


    return answer
    

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    answer = solve(numbers, n)
    print(' '.join(map(str, answer)))
