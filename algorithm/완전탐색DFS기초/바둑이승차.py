# 바둑이 승차
import sys

# sys.stdin = open("input.txt", "rt")

"""
기존 풀이 -> 시간 초가

이유 : 가지치기를 안했기때문이다.

(total - tsum) 남은 원소의 합
따라서 현재 값과 남은 원소의 합이 정답보다 작으면 굳이 더 할 필요없음.

"""


def solve(c, n, numbers):
    answer = 0
    total = sum(numbers)

    def dfs(i, res, tsum):
        nonlocal c, n, answer
        if res + (total - tsum) < answer:
            return
        if res > c:
            return
        if i == n:
            if res < c:
                answer = max(answer, res)
        else:
            dfs(i + 1, res + numbers[i], tsum + numbers[i])
            dfs(i + 1, res, tsum + numbers[i])

    dfs(0, 0, 0)
    return answer


if __name__ == "__main__":
    c, n = map(int, input().split())
    numbers = [int(input()) for _ in range(n)]
    answer = solve(c, n, numbers)
    print(answer)
