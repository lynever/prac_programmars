def solution(a, b, c):
    tmplst = [a, b, c]
    if max(tmplst) == min(tmplst):
        answer = sum(tmplst) * (a ** 2 + b ** 2 + c ** 2) * (3 * (a ** 3))
    elif sum(tmplst) - max(tmplst) == 2 * min(tmplst) or sum(tmplst) - min(tmplst) == 2 * max(tmplst):
        answer = sum(tmplst) * (a ** 2 + b ** 2 + c ** 2)
    else:
        answer = sum(tmplst)
    return answer