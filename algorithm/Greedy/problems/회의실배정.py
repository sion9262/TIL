import sys

#sys.stdin = open("input.txt", "rt")


# 회의실 배정(그리디)


def solve(schedule, n):
    answer = 1

    # 빨리 끝나는 순으로 sort
    schedule = sorted(schedule, key=lambda x: x[1])

    end = schedule[0][1]

    for i in range(1, n):
        if schedule[i][0] >= end:
            end = schedule[i][1]
            answer += 1    
    
    return answer
    

if __name__ == "__main__":
    n = int(input())
    schedule = []
    for _ in range(n):
        start, end = map(int, input().split())
        schedule.append((start, end))
     
    answer = solve(schedule, n)
    print(answer)
