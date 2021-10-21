# 아나그램
import sys

#sys.stdin = open("input.txt", "rt")

def solve(a, b):
    a.sort()
    b.sort()
    for i in range(len(a)):
        if a[i] == b[i]:
            pass
        else:
            return "NO"
    return "YES"
    
    
    

if __name__ == "__main__":
    
    a = list(input())
    b = list(input())
    answer = solve(a, b)
    print(answer)
