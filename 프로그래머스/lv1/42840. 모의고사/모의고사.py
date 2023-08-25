def solution(answers):
    answer = []
    stuplst = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    corlst = [0 for x in stuplst]
    for i in range(0, len(answers)):
        for j in range(0, len(stuplst)):
            if i >= len(stuplst[j]):
                stuplst[j] = stuplst[j] * 2
            if answers[i] == stuplst[j][i]:
                corlst[j] += 1
    for k in range(0, len(corlst)):
        if corlst[k] == max(corlst):
            answer.append(k + 1)
    return answer