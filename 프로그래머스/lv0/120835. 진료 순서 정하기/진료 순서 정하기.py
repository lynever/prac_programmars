def solution(emergency):
    answer = []
    tmplst = sorted(emergency)
    emgdic = {x : idx + 1 for idx, x in enumerate(reversed(tmplst))}
    for i in emergency:
        answer.append(emgdic[i])
    return answer