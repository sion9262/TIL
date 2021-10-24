# 이진트리 순회 깊이 우선탐색
import sys

#전위순회
def solve(n):
	if n > 7:
		return
	else:
		print(n, end=" ")
		solve(n * 2)
		solve(n * 2 + 1)

# 중위순회
def solve2(n):
	if n > 7:
		return
	else:
		solve2(n * 2)
		print(n, end=" ")
		solve2(n * 2 + 1)

# 후위순회
def solve3(n):
	if n > 7:
		return
	else:
		solve3(n * 2)
		solve3(n * 2 + 1)
		print(n, end=" ")

if __name__ == "__main__":
	#solve(1)
	solve2(1)
	#solve3(1)
