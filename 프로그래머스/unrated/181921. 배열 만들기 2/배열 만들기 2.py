def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        if str(i).count('5') + str(i).count('0') == len(str(i)):
            answer.append(i)
    return answer if len(answer) != 0 else [-1]