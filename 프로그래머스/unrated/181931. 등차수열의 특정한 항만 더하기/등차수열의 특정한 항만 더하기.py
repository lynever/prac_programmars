def solution(a, d, included):
    answer = 0
    for idx, val in enumerate(included):
        if val:
            answer += a + d * (idx)
    return answer