def solution(elements):
    elements *= 2
    tmpst, n = set(), len(elements)
    for i in range(1, n // 2 + 1):
        for j in range(n // 2):
            tmpst.add(sum(elements[j:j + i]))
    return len(tmpst)