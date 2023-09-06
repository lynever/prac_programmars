from math import comb
def solution(n):
    answer = 0
    if n % 2 == 0:
        for i in range(0, n // 2 + 1):
            answer += comb(n - i, i)
    else:
        for i in range(0, n // 2 + 1):
            answer += comb(n - i, i)
    return answer % 1234567