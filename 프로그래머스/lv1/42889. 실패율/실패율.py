def solution(N, stages):
    answer, stgdic, sucdic = [], {i + 1: [] for i in range(0, N + 1)}, {}
    n = len(stages)
    for idx, val in enumerate(stages):
        stgdic[val].append(idx)
    for key, value in stgdic.items():
        sucdic[key] = len(stgdic[key]) / n if n != 0 else 0
        n -= len(stgdic[key])
    sucdic.pop(N + 1, None)
    answer = [i[0] for i in sorted(sucdic.items(), key = lambda item:item[1], reverse = True)]
    return answer