def solution(s):
    tmplst = []
    for i in s:
        tmplst.append(i)
        while len(tmplst) >= 2:
            if tmplst[-2] == tmplst[-1]:
                tmplst.pop()
                tmplst.pop()
            elif tmplst[-2] != tmplst[-1]:
                break  
    return 1 if len(tmplst) == 0 else 0