from itertools import combinations
def solution(number):
    answer = 0
    for i in list(combinations(number, 3)):
        answer = answer + 1 if sum(i) == 0 else answer
    return answer