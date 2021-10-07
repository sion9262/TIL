import sys
#sys.stdin = open("input.txt", "rt")

"""
격자판 최대합
5*5 격자판에 아래롸 같이 숫자가 적혀있습니다. 
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합
니다.
▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50) 
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
다. 
▣ 출력설명
최대합을 출력합니다.
▣ 입력예제 1 
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
▣ 출력예제 1
155
"""
def solve(maps, n):
    answer = -1
    
    # 가로 
    for map in maps:
        answer = max(answer, sum(map))

    # 세로
    for i in range(n):
        v = 0
        for j in range(n):
            v += maps[j][i]
        answer = max(answer, v)

    # 대각선
    d = 0
    for i in range(n):
        for j in range(n):
            if i == j :
                d += maps[i][j]
    answer = max(answer, d)
    d = 0
    for i in range(n):
        d += maps[i][n-i-1]
    answer = max(answer, d)

    return answer

if __name__ == "__main__":
    n = int(input())
    maps = [list(map(int, input().split())) for _ in range(n)]

    answer = solve(maps, n)
    print(answer)
