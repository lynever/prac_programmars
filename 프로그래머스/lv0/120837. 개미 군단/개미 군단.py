def solution(hp):
    answer = 0
    for i in range(5, 0, -2):
        ant = hp // i
        answer += ant
        hp -= i * ant
    return answer