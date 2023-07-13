def solution(n):
    answer = []
    for i in range(n):
        tmp = []
        for j in range(n):
            tmp.append(int(i == j))
        answer.append(tmp)
    return answer