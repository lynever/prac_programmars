from fractions import Fraction
def chkPrime(a):
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return 0
    return 1
def solution(a, b):
    answer = 1
    tmp = Fraction(a, b).denominator
    tmpst = set()
    for i in range(2, tmp + 1):
        if tmp % i == 0 and chkPrime(i) == 1:
            tmpst.add(i)
    if len(tmpst) > 2:
        answer = 2
    elif len(tmpst) == 2:
        if 2 not in tmpst or 5 not in tmpst:
            answer = 2
    elif len(tmpst) == 1:
        if 2 not in tmpst and 5 not in tmpst:
            answer = 2
    return answer