def solution(keymap, targets):
    answer, keydic = [], {}
    for i in keymap:
        for idx, val in enumerate(i):
            if val not in keydic:
                keydic[val] = [idx]
            else:
                keydic[val].append(idx)
    for j in targets:
        tmp = 0
        for k in j:
            if k in keydic:
                tmp += min(keydic[k]) + 1
            else:
                tmp = - 1
                break
        answer.append(tmp)
    return answer