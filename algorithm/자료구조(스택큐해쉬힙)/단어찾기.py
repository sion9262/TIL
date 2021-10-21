# 단어 찾기
import sys

#sys.stdin = open("input.txt", "rt")

def solve(n, prevNotes, notes):
    
    
    prevNotes.sort()
    notes.sort()

    for i in range(n-1):
        if prevNotes[i] != notes[i]:
            return prevNotes[i]
    
    return prevNotes[-1]

if __name__ == "__main__":
    n = int(input())
    prevNotes = [input() for i in range(n)]
    notes = [input() for i in range(n-1)]
    answer = solve(n, prevNotes, notes)
    print(answer)
