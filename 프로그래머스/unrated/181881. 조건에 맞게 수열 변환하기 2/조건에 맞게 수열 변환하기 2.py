def solution(arr):
    answer = -1
    cprlst, tmplst, chglst = [], arr, arr
    while cprlst != chglst:
        cprlst = tmplst
        chglst = []
        for i in tmplst:
            if i >= 50 and i % 2 == 0:
                chglst.append(i // 2)
            elif i < 50 and i % 2 == 1:
                chglst.append(i * 2 + 1)
            else:
                chglst.append(i)
        answer += 1
        tmplst = chglst
    return answer