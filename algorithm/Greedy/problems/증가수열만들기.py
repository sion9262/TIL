
# 증가수열 만들기(그리디)


import sys
#sys.stdin = open("input.txt", "rt")

def solve(numbers, n):
    answer = ""
    prev = -1
    lt, rt = 0, n-1
    while lt <= rt:
        ck = []
        if prev < numbers[lt]:
            ck.append((numbers[lt], 'L'))
        if prev < numbers[rt]:
            ck.append((numbers[rt], 'R'))

        if len(ck) == 0:
            break
        ck.sort()
        answer += ck[0][1]   
        prev = ck[0][0]         
        if ck[0][1] == 'L':
            lt += 1
        else:
            rt -= 1

    return answer
    

if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    answer = solve(numbers, n)
    print(len(answer))
    print(answer)
