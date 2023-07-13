def solution(picture, k):
    answer, tmp = [], ''
    for i in picture:
        for j in i:
            tmp += j * k
        for _ in range(k):
            answer.append(tmp)
        tmp = ''
    return answer