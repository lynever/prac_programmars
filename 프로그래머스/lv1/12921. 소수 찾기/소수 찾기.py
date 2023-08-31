def solution(n):
    answer = 1
    for i in range(3, n + 1):
        if i % 2 != 0:
            state = 0
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    state = 1
                    break
            if state == 0:
                answer += 1
    return answer