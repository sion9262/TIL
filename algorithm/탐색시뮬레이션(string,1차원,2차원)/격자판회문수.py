import sys

#sys.stdin = open("input.txt", "rt")

"""
격자판 회문수
1부터 9까지의 자연수로 채워진 7*7 격자판이 주어지면 격자판 위에서 가로방향 또는 
세로방향으로 길이 5자리 회문수가 몇 개 있는지 구하는 프로그램을 작성하세요.
회문수란 121과 같이 앞에서부터 읽으나 뒤에서부터 읽으나 같은 수를 말합니다.
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5
빨간색처럼 구부러진 경우(87178)는 회문수로 간주하지 않습니다.
▣ 입력설명
1부터 9까지의 자연수로 채워진 7*7격자판이 주어집니다.
▣ 출력설명
5자리 회문수의 개수를 출력합니다.
▣ 입력예제 1 
2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1 
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5
▣ 출력예제 1
3

"""

def solve(maps):
    answer = 0

    # 가로 축
    for i in range(3):
        for j in range(7):
            tmp = maps[j][i:i+5]
            if tmp == tmp[::-1]:
                answer += 1
            for k in range(2):
                if maps[i+k][j] != maps[i+5-k-1][j]:
                    break
            else:
                answer += 1
            

    return answer

if __name__ == "__main__":
    maps = [list(map(str, input().split())) for _ in range(7)]
    answer = solve(maps)
    print(answer)
