def solution(s):
    answer, tmplst, tmp, tmpstr = [], [], set(), ''
    s = s[1:-1]
    for idx, val in enumerate(s):
        if val.isdigit() and not s[idx + 1].isdigit():
            tmpstr += val
            tmp.add(int(tmpstr))
            tmpstr = ''
        elif val.isdigit():
            tmpstr += val
        elif val == '}':
            tmplst.append(tmp)
            tmp = set()
            tmpstr = ''
    for j in sorted(tmplst, key= len):
        for k in j:
            if k not in answer:
                answer.append(k)
    return answer