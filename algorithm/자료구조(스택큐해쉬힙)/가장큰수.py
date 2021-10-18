# 가장 큰 수
import sys
#sys.stdin = open("input.txt", "rt")

"""
내 생각 

모든 조합을 추출하여 max 값 추출

조합의 갯수 - len(n)Clen(n)-m

-> 시간 초과

풀이

for 문 돌려서
앞자리가 자신보다 작으면 지우고 앞으로감.
만약 지우는 갯수만큼 갔으면 뒤에 붙힘.
"""

def solve(n, m):
    answer = []

    # 순회 하기 위함.
    numbers = list(map(int, str(n)))
    cnt = 0

    for number in numbers:
        # 길이가 0이면 바로 집어 넣음.
        if len(answer) == 0:
            answer.append(number)
            continue

        # 해당 길이까지 갔으면 break
        if len(answer) == len(numbers) - m: 
            break
        
        # 만약 맨뒤 숫자가 현 숫자보다 작고 변경 횟수도 작으면 아래 조건까지 pop()
        if answer[-1] < number and cnt < m:
            while cnt < m and len(answer) > 0 and answer[-1] < number:
                answer.pop()
                cnt += 1
        answer.append(number)

    return int(''.join(map(str, answer)))

if __name__ == "__main__":
    n,  m = map(int, input().split())
    answer = solve(n, m)
    print(answer)
