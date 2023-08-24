def solution(n):
    answer, tmp , trans = 0, 1, ''
    while n // (3 ** tmp) != 0:
        tmp += 1
    tmp -= 1
    for i in range(tmp, -1, -1):
        trans += str(n // (3 ** i))
        n = n % (3 ** i)
    trans = trans[::-1]
    for i in range(len(trans)):
        answer += (3 ** i) * int(trans[-1])
        trans = trans[:-1]
    return answer