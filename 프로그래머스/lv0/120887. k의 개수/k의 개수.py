def solution(i, j, k):
    answer = 0
    for tmp in range(i, j + 1):
        answer += str(tmp).count(str(k))
    return answer