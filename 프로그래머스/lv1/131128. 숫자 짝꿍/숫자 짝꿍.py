def solution(X, Y):
    answer = ''
    Xdic, Ydic = {num : 0 for num in range(0, 10)}, {num : 0 for num in range(0, 10)}
    for i in X:
        Xdic[int(i)] += 1
    for j in Y:
        Ydic[int(j)] += 1
    for k in range(0, 10):
        answer = answer + str(k) * min(Xdic[k], Ydic[k]) if Xdic[k] != 0 and Ydic[k] != 0 else answer
    if len(answer) == 0:
        answer = '-1'
    elif answer.count('0') == len(answer):
        answer = '0'
    else:
        answer = answer[::-1]
    return answer