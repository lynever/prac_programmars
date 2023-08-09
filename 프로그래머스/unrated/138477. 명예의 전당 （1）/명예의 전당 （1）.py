def solution(k, score):
    answer, scrlst = [], []
    for i in score:
        if len(scrlst) < k:
            scrlst.append(i)
        elif i > scrlst[0]:
            scrlst[0] = i
        scrlst.sort()
        answer.append(scrlst[0])
    return answer