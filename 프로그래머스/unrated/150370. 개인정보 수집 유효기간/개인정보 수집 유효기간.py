def solution(today, terms, privacies):
    answer, tmplst = [], []
    today = list(map(int, today.split('.')))
    todaynum = today[0] * 12 * 28 + today[1] * 28 + today[2]
    terms = [i.split(' ') for i in terms]
    for idx, val in enumerate(privacies):
        tmplst.append(val.split(' '))
        tmplst[idx][0] = list(map(int, tmplst[idx][0].split('.')))
        tmplst[idx][0] = tmplst[idx][0][0] * 12 * 28 + tmplst[idx][0][1] * 28 + tmplst[idx][0][2] - 1
        for state, num in terms:
            if tmplst[idx][1] == state:
                tmplst[idx] = tmplst[idx][0] + int(num) * 28
                break
    for j, k in enumerate(tmplst):
        if k < todaynum:
            answer.append(j + 1)
    return answer