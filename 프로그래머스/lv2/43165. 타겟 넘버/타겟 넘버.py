from itertools import product
def solution(numbers, target):
    answer = 0
    sel = [1, -1]
    case = list(product(sel, repeat=len(numbers)))
    for i in case:
        tmp = 0
        for j, k in zip(i, numbers):
            tmp += j * k
        if tmp == target:
            answer += 1
    return answer