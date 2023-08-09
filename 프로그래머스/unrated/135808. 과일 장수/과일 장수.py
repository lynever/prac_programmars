def solution(k, m, score):
    answer = 0
    score = sorted(score)[len(score) - len(score) // m * m:]
    for i in range(0, len(score), m):
        answer += score[i] * m
    return answer