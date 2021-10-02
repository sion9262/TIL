import sys
input = sys.stdin.readline

"""
꽃길을 걷고 싶은 진아
꽃을 심으면 1년후 꽃이 핌.
씨앗이 3개, 하나도 죽지 않고 만개
꽃이 피면 상하좌우로 꽃이 핌. 만약 다른 꽃잎과 닿게 되면 꽃은 죽음.
화단 대여시 꽃이 모두 피면서 가장 싼 가격에 화단을 대여
꽃 하나당 5평의 땅을 대여
이때 꽃을 심기 위해 필요한 최소비용을 구하라
"""
N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 0, 1, 0 ,-1], [0, -1, 0, 1, 0]
ans = 987654321

def solve(lst):
	ret = 0
	flower = []
	for flow in lst:
		x = flow // N
		y = flow % N

		if x == 0 or y == 0 or x == N-1 or y == N-1:
			return 987654321
		for k in range(5):
			flower.append((x + dx[k], y + dy[k]))
			ret += M[x+dx[k]][y+dy[k]]
	if len(set(flower)) >= 15:
		return ret
	else:
		return 987654321
"""
3가지의 꽃을 배치하기 위한 반목문
"""
for i in range(N*N):
	for j in range(N*N):
		for k in range(N*N):
			ans = min(ans, solve([i, j, k]))

print(ans)