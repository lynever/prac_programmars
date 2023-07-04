def solution(strArr):
    cntdic = {len(i) : 0 for i in strArr}
    for j in strArr:
        cntdic[len(j)] += 1
    return max(cntdic.values())