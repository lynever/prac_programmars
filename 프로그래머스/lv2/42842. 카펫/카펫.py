def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            if (i + 2) * ((yellow // i) + 2) == brown + yellow:
                answer = [max(i, yellow // i) + 2, min(i, yellow // i) + 2]
    return answer