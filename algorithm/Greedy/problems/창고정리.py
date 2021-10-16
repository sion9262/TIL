
#창고 정리
import sys
#sys.stdin = open("input.txt", "rt")

def solve(boxs, l, m):
    answer = 999999
    boxs.sort()
    for i in range(m):
        boxs[0] += 1
        boxs[-1] -= 1
        boxs.sort()
    answer = boxs[-1] - boxs[0]
    return answer
    

if __name__ == "__main__":
    l = int(input())
    boxs = list(map(int, input().split()))
    m = int(input())
    answer = solve(boxs, l, m)
    print(answer)
