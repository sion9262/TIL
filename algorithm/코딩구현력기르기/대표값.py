import sys
#sys.stdin = open("input.txt", "rt")

"""
대표값
n명의 학생의 점수가 주어미
학생들의 평균 (소수 첫째자리 반올림) 구하고
평균에 가장 가까운 학생은 몇 번째 학생인지 출력
만약 평균과 가장 가까운 점수가 여러 개일 경우 
1. 점수가 높은 학생의 번호로 답.
2. 높은 점수가 여러 명일 경우 학생번호가 빠른 순으로 답하여라

round(숫자, 번째) = 소수점 번째 자리에서 반올림
# 오류 수정
round(5.5) -> 5가 나옴 round_half_even 방식이기에.
따라서 int(5.5 + 0.5) 로 변경
abs() = 절대값
"""


def solve(students, n):
    avg = int(sum(students) / n + 0.5)
    idx = 101
    score = 0
    gap = 999
    for i, student in enumerate(students):
        if abs(avg - student) == gap:
            if score < student:
                idx = i
                score = student
                gap = abs(avg - student)
            
        elif abs(avg - student) < gap:
            idx = i
            score = student
            gap = abs(avg - student)

    return avg, idx+1


n = int(input())
students = list(map(int, input().split()))
avg, idx = solve(students, n)
print(avg, idx)

