def solution(n,a,b):
    answer = 1
    matchlst, tmplst = [], []
    for i in range(n):
        tmplst.append(i + 1 if i + 1 == a or i + 1 == b else 0)
        if len(tmplst) == 2:
            matchlst.append(tmplst)
            tmplst = []
    while [a, b] not in matchlst and [b, a] not in matchlst:
        answer += 1
        for j in range(0, len(matchlst), 2):
            tmplst.append([max(matchlst[j]), max(matchlst[j + 1])])
        matchlst = tmplst
        tmplst = []
    return answer