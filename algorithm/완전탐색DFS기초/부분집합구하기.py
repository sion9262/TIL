# 부분 집합 만들기
import sys


def solve(v, n, ch):
	if v == n + 1:
		for i in range(1, n+1):
			if ch[i] == 1:
				print(i, end=" ")
		print()
	else:
		ch[v] = 1
		solve(v+1, n, ch)
		ch[v] = 0
		solve(v+1, n, ch)
		
	

if __name__ == "__main__":
	n = int(input())
	ch = [0 for i in range(n+1)]
	solve(1, n, ch)

