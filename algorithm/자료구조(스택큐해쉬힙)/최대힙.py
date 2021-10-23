# 최대힙
import sys
import heapq
#sys.stdin = open("input.txt", "rt")

def solve(n):
	#heapq는 최소힙 제공, 트릭을 이용하여 최대 -> 음수를 붙이면 최소가 됨 
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
				print(heapq.heappop(q)[1])
		else:
			heapq.heappush(q, (-num, num))

if __name__ == "__main__":
	n = int(input())
	solve(n)
