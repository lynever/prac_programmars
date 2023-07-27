def checkPrime(n):
    tmp = 0
    for i in range(2, n + 1):
        if n % i == 0:
            tmp += 1
    return 1 if tmp == 1 else 0
def solution(n):
    answer = []
    for i in range(2, n + 1):
        if n % i == 0 and checkPrime(i) == 1:
            answer.append(i)
    return answer