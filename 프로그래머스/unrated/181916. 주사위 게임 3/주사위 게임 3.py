def solution(a, b, c, d):
    answer = 0
    tmplst, tmpst = [a, b, c, d], set({a, b, c, d})
    if len(tmpst) == 1:
        answer = 1111 * a
    elif len(tmpst) == 2:
        tmplst.sort()
        if tmplst.count(tmplst[0]) == tmplst.count(tmplst[-1]):
            answer = (tmplst[-1] + tmplst[0]) * (tmplst[-1] - tmplst[0])
        else:
            answer = (10 * tmplst[0] + tmplst[-1]) ** 2 if tmplst.count(tmplst[0]) == 3 else (10 * tmplst[-1] + tmplst[0]) ** 2
    elif len(tmpst) == 3:
        for i in tmplst:
            if tmplst.count(i) == 2:
                tmpst.remove(i)
                break
        answer = 1
        for j in tmpst:
            answer *= j
    elif len(tmpst) == 4:
        answer = min(tmpst)
    return answer