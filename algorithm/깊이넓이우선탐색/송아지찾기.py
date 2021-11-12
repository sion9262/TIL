# 송아지 찾기(BFS)
import sys

#sys.stdin = open("input.txt", "rt")

"""
BFS 이용
이동은 1, -1, 5 만 가능.
조건에 따라 1 미만 10000초과면 추가 X

리스트의 앞에 것을 추출 (큐방식)
이미 방문한 것이면 continue (가지치기)

s+step == e 면 찾은 것.
아니면
s+step 과 해당 노드의 깊이 +1을 넣어준다.
"""

def parse_string(num):
    return chr(65 + int(num) - 1)

def solve(s, e):
    
    steps = [1, -1, 5]
    queue = []
    visited = [False] * 10001
    # 첫번째 현수 위치 넣기
    queue.append((s, 0))
    while queue:
        s, v = queue.pop(0)
        if visited[s]:
            continue

        visited[s] = True
        
        for step in steps:
            if s + step < 1 or s + step > 10000:
                continue
            if s + step == e:
                print(v+1)
                exit(0)
            elif not visited[s+step]:
                queue.append((s+step, v+1))

    
if __name__ == "__main__":

    s, e  = map(int, input().split())
    solve(s, e)
 