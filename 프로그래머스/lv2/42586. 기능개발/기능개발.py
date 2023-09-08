def solution(progresses, speeds):
    answer, tmplst = [], []
    fin = [(100 - i) // j if (100 - i) % j == 0 else (100 - i) // j + 1 for i, j in zip(progresses, speeds)]
    for idx, val in enumerate(fin):
        if len(tmplst) == 0:
            tmplst.append(val)
        elif val <= tmplst[0]:
            tmplst.append(val)
        elif val > tmplst[0]:
            answer.append(len(tmplst))
            tmplst = [val]
        if idx == len(fin) - 1:
            answer.append(len(tmplst))
    return answer