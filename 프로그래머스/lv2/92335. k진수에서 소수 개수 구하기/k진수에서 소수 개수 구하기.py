def solution(n, k):
    answer = 0
    tmp, tmpstr = 0, ''
    while k ** tmp <= n:
        tmp += 1
    tmp -= 1
    for i in range(tmp, -1, -1):
        tmpstr += str(n // k ** i)
        n -= (n // k ** i) * (k ** i)
    tmpstr = tmpstr.split('0')
    for j in tmpstr:
        if j != '' and j != '1':
            leng = 0
            for k in range(2, int(int(j) ** 0.5) + 1):
                if int(j) % k == 0:
                    leng += 1
                    break
            if leng == 0:
                answer += 1
    return answer