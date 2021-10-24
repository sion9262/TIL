# 재귀함수를 이용한 이진수 출력
import sys
#sys.stdin = open("input.txt", "rt")
"""
1. 이진수 구하는 법
n == 0 이면 0 추가
n == 1 이면 1 추가
n % 2 == 0 일 때 0 추가
n % 2 == 1 일 때 1 추가
"""
def solve(n):
	answer = ""
	if n == 0:
		return "0"
	
	if n == 1:
		return "1"
	if n % 2 == 0:
		answer += "0"
		n = n // 2
		answer += solve(n)
	else:
		answer += "1"
		n = n // 2
		answer += solve(n)
	return answer
"""
강사님 풀이.
def dfs(x):
	if x == 0:
		return
	else:
		dfs(x//2)
		print(x%2, end=' ')

"""
if __name__ == "__main__":
	n = int(input())
	print(solve(n)[::-1])
