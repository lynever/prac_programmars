def solution(myString, pat):
    return 1 if pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B') else 0