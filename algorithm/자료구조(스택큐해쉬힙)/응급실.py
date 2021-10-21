# 응급실
import sys

#sys.stdin = open("input.txt", "rt")

def solve(n, m, risks):
    
    answer = 0
    risks = [(risk, i) for i, risk in enumerate(risks)]

    while risks:
        answer += 1
        maxNum = max(risks)
        
        while risks:
            risk = risks.pop(0)
            if risk[0] == maxNum[0]:
                if risk[1] == m:
                    return answer
                else:
                    break
            else:
                risks.append(risk)
        
    return answer 


if __name__ == "__main__":
    n, m = map(int, input().split())
    risks = list(map(int, input().split()))
    answer = solve(n, m, risks)
    print(answer)
