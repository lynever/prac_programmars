def solution(my_string, m, c):
    answer, tmplst = '', []
    for idx, val in enumerate(my_string):
        if m == 1:
            tmplst.append([val])
        elif idx % m == 0:
            tmp = [val]
        elif idx % m == m - 1:
            tmp.append(val)
            tmplst.append(tmp)
        else:
            tmp.append(val)
    for i in tmplst:
        answer += i[c - 1]
    return answer

