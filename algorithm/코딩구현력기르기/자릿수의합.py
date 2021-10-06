import sys
#sys.stdin = open("input.txt", "rt")

"""
자릿수의 합
N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 그 합이 최대인 자연수를 출력
하는 프로그램을 작성하세요. 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 
꼭 작성해서 프로그래밍 하세요.

자릿수의 합이 최대인 자연수를 출력한다. 자릿수의 합이 같을 경우 입력순으로 먼저인 숫자
를 출력합니다.

입력예제 1 
3
125 15232 97
출력예제 1
97
"""


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

def solve(nums, n):
    answer = 0
    max = -1
    for num in nums:
        sum = digit_sum(num)
        if max < sum:
            answer = num
            max = sum

    return answer


n= int(input())
nums = list(map(int, input().split()))
print(solve(nums, n))

