def solution(s):
    answer = 0
    tmpstr, fcnt, scnt = '', 0, 0
    for i in s:
        if tmpstr == '':
            tmpstr += i
            fcnt += 1
        elif i == tmpstr[0]:
            tmpstr += i
            fcnt += 1
        elif i != tmpstr[0]:
            tmpstr += i
            scnt += 1
            if fcnt == scnt:
                answer += 1
                tmpstr = ''
                fcnt = 0
                scnt = 0
    if tmpstr != '':
        answer += 1
    return answer