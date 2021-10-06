import sys
#sys.stdin = open("input.txt", "rt")

"""
정다면체
두 개의 n, m 정다면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력
정답이 여러 개일 경우 오름차순으로 출력
"""


def solve(n, m):
    answer = []
    sums = dict()
    # sums = {1 : 2, 2 : 4 ...}
    for i in range(1, n+1):
        for j in range(1, m+1):
            sum = i + j
            if sum in sums:
                sums[sum] += 1
            else:
                sums[sum] = 1
    # maxValue 값 찾기
    maxValue = max(sums.values())
    # dict 순회
    for key, value in sums.items():
        if value == maxValue:
            answer.append(key)
    answer.sort()
    # join() 시 int 면 안되기에 str 로 타입 변경
    answer = map(str, answer)
    return ' '.join(answer)


n, m = map(int, input().split())
print(solve(n, m))

