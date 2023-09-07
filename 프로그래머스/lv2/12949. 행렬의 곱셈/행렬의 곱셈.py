def solution(arr1, arr2):
    answer = []
    n, m, o = len(arr1), len(arr1[0]), len(arr2[0])
    arr2 = sum(arr2, [])
    for i in arr1:
        tmplst = []
        for j in range(o):
            tmp = 0
            for k in range(m):
                tmp += i[k] * arr2[k * o + j]
            tmplst.append(tmp)
        answer.append(tmplst)
    return answer