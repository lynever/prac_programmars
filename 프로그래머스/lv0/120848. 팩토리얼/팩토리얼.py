def solution(n):
    for i in range(1, 11):
        n //= i
        if n == 1:
            answer = i
        elif n == 0:
            answer = i - 1
            break
    return answer