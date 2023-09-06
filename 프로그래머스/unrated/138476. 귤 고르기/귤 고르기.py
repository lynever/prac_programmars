def solution(k, tangerine):
    answer, cntdic = 0, {}
    for i in tangerine:
        cntdic[i] = 1 if i not in cntdic.keys() else cntdic[i] + 1
    for key, val in sorted(cntdic.items(), key = lambda x : x[1], reverse = True):
        answer += 1
        k -= val
        if k <= 0:
            break
    return answer