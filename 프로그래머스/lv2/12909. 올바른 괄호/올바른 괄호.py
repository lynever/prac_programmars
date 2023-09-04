def solution(s):
    tmplst = []
    for i in s:
        tmplst.append(i)
        if len(tmplst) >= 2 and tmplst[-2:] == ['(', ')']:
            while tmplst[-2:] == ['(', ')']:
                tmplst.pop()
                tmplst.pop()
    return True if len(tmplst) == 0 else False