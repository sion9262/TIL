import sys

#sys.stdin = open("input.txt", "rt")

"""
씨름 선수(그리디)
"""

def solve(players, n):
    answer = 0
    max_w = 0
    # 키 순으로 정렬
    players = sorted(players, key=lambda x:(x[0], x[1]), reverse=True)
    for k, w in players:
        # 몸무게만 크면 됨
        if max_w < w:
            answer += 1
            max_w = w 

    return answer
    

if __name__ == "__main__":
    n = int(input())
    players = []
    for _ in range(n):
        k, w = map(int, input().split())
        players.append((k, w))
     
    answer = solve(players, n)
    print(answer)
