"""
dfs를 이용한 풀이
"""

numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx + 1, result + numbers[idx])
            dfs(idx + 1, result - numbers[idx])

    dfs(0, 0)
    return answer

solution(numbers, target)