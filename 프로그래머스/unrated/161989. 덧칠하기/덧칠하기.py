def solution(n, m, section):
    answer, strt = 0, section[0] - 1
    for i in section:
        if strt < i:
            strt = i + m - 1
            answer += 1
    return answer