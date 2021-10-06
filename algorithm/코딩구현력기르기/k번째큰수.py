import sys
#sys.stdin = open("input.txt", "rt")

"""
K번째 큰 수
1~100사이의 N장의 카드.
이 중 3장을 뽑아 더함.
기록한 값 중 k번째로 큰 수를 출력
"""


def solve(nums, n, k):
    answer = 0

    addNums = set()
    # 조합
    for one in range(n-2):
        for two in range(one+1, n-1):
            for three in range(two+1, n):
                addNums.add(nums[one]+nums[two]+nums[three])
    addNums = list(addNums)
    addNums.sort(reverse=True)
    answer = addNums[k-1]
    return answer

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(solve(nums, n, k))

