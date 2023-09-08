from math import comb
def solution(clothes):
    answer = 1
    ctgdic = {i[1]: set() for i in clothes}
    for cloth, ctg in clothes:
        ctgdic[ctg].add(cloth)
        ctgdic[ctg].add('none')
    for key, val in ctgdic.items():
        answer *= comb(len(val), 1)
    return answer - 1