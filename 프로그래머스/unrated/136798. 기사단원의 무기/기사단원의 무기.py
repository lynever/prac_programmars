def solution(number, limit, power):
    answer = 1
    for i in range(2, number + 1):
        divcnt = 0
        for j in range(1, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                divcnt = divcnt + 1 if j ** 2 == i else divcnt + 2
        answer = answer + power if divcnt > limit else answer + divcnt
    return answer