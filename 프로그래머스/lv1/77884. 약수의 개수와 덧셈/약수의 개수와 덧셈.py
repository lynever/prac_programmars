def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        divisor = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                divisor = divisor + 1 if j ** 2 == i else divisor + 2
        answer = answer + i if divisor % 2 == 0 else answer - i
    return answer