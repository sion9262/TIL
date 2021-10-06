import sys
#sys.stdin = open("input.txt", "rt")

"""
K번째 수
N개의 숫자로 이루어진 리스트 중 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때
k번째로 나타나는 숫자를 출력하라.
"""


def solve(nums, n, s, e, k):
    answer = 0

    # s-1 ~ e 자르기
    numsSplit = nums[s-1:e]
    # 정렬
    numsSplit.sort()
    answer = numsSplit[k-1]

    return answer
T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))

    print("#{} {}".format(t+1, solve(nums, n, s, e, k)))

