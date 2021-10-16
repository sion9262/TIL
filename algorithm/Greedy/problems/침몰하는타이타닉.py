
# 침몰하는 타이타닉(그리디)

import sys
#sys.stdin = open("input.txt", "rt")

def solve(w, n, m):
    answer = 0
    w.sort()
    
    # 구출한 인원
    cnt = 0

    lt, rt = 0, n-1
    while cnt < n and lt <= rt:
        # 가벼운 + 무거운 <= 기준 이면 같이 탐. 
        if w[lt] + w[rt] <= m:
            answer += 1
            cnt += 2
            lt +=1
            rt -= 1
        else:
            # 아닐 시 무거운 사람은 다른 사람이랑 절대 타지 못함.
            rt -= 1
            cnt += 1
            answer += 1
    return answer
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    w = list(map(int, input().split()))
    answer = solve(w, n, m)
    print(answer)
