def solution(arr):
    divlst, divdic = [], {}
    for i in range(len(arr)):
        tmp, tmplst, j = arr[i], [], 2
        while tmp != 1:
            if tmp % j == 0:
                tmplst.append(j)
                tmp /= j
            else:
                j += 1
        divlst.append(tmplst)
    for j in divlst:
        for k in j:
            divdic[k] = max(divdic[k], j.count(k)) if k in divdic.keys() else j.count(k)
    return eval('*'.join(list(map(str, [key ** val for key, val in divdic.items()]))))