def solution(n, words):
    answer = [0, 0]
    tmplst = []
    for idx, val in enumerate(words):
        if val in tmplst:
            answer = [(idx % n) + 1, (idx // n) + 1]
            break
        elif len(val) == 1:
            answer = [(idx % n) + 1, (idx // n) + 1]
            break
        elif len(tmplst) >= 1 and val[0] != tmplst[-1][-1]:
            answer = [(idx % n) + 1, (idx // n) + 1]
            break
        else:
            tmplst.append(val)
    return answer