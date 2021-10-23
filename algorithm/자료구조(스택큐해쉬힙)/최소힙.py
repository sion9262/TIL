# 최소힙
import sys
import heapq
#sys.stdin = open("input.txt", "rt")

def solve(n):
	#heapq 생성 후 조건에 맞춰 실행
	q = []
	while True:
		num = int(input())
		if num == -1:
			return
		elif num == 0:
			if len(q) == 0:
				print(-1)
				return
			else:
				print(heapq.heappop(q))
		else:
			heapq.heappush(q, num)

if __name__ == "__main__":
	n = int(input())
	solve(n)
