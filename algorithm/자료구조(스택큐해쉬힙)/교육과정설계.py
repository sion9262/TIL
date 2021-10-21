# 교육과정 설계
import sys

#sys.stdin = open("input.txt", "rt")

def solve(find, n, study):
    
    answer = "YES"
    find = list(find)
    for i in range(len(study)):
        if study[i] in find:
            if study[i] == find[0]:
                find.pop(0)
            else:
                answer ="NO"
                break
    
    if len(find) > 0:
        answer = "NO"
        
    return answer 


if __name__ == "__main__":
    find = input()
    n = int(input())
    for i in range(n):
        study = input()
        answer = solve(find, n, study)
        print("#{} {}".format(i+1, answer))
