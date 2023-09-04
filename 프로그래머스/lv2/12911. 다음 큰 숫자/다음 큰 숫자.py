def solution(n):
    answer = n + 1
    while 1:
        if bin(n).count('1') == bin(answer).count('1'):
            break
        else:
            answer += 1
    return answer