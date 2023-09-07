def solution(s):
    answer, tmplst = 0, []
    for i in range(len(s)):
        s = s[1:] + s[0]
        for j in s:
            tmplst.append(j)
            while 1:
                if len(tmplst) >= 2:
                    if ''.join(tmplst[-2:]) in '[] {} ()':
                        tmplst.pop()
                        tmplst.pop()
                    else:
                        break
                else:
                    break
        if tmplst == []:
            answer += 1
        tmplst.clear()
    return answer