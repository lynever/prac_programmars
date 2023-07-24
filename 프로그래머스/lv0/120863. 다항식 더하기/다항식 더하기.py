def solution(polynomial):
    answer = ''
    x, num = 0, 0
    polynomial = polynomial.split(' + ')
    for i in polynomial:
        if 'x' in i:
            x += 1 if len(i) == 1 else int(i[:-1])
        else:
            num += int(i)
    if x == 0:
        answer = str(num)
    elif x == 1:
        answer = 'x' if num == 0 else 'x + ' + str(num)
    else:
        answer = str(x) + 'x' if num == 0 else str(x) + 'x + ' + str(num)
    return answer