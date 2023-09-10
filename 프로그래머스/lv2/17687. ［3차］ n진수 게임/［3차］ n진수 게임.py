def solution(n, t, m, p):
    answer, numstr = '', ''
    for i in range(t * m):
        if i == 0 or i == 1:
            numstr += str(i)
        else:
            tmp = 0
            while n ** tmp <= i:
                tmp += 1
            tmp -= 1
            for j in range(tmp, -1, -1):
                if str(i // n ** j) == '10':
                    numstr += 'A'
                elif str(i // n ** j) == '11':
                    numstr += 'B'
                elif str(i // n ** j) == '12':
                    numstr += 'C'
                elif str(i // n ** j) == '13':
                    numstr += 'D'
                elif str(i // n ** j) == '14':
                    numstr += 'E'
                elif str(i // n ** j) == '15':
                    numstr += 'F'
                else:
                    numstr += str(i // n ** j)
                i -= (i // n ** j) * (n ** j)
            if len(numstr) >= t * m:
                break
    numstr = numstr[:m * t]
    for idx, val in enumerate(numstr):
        if m != p and (idx + 1) % m == p:
            answer += val
        elif m == p and (idx + 1) % m == 0:
            answer += val
    return answer