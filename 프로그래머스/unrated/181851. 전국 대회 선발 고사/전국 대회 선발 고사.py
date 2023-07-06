def solution(rank, attendance):
    answer = 0
    tmp, cnt = [], 4
    for idx, val in enumerate(rank):
        tmp.append([idx, val, attendance[idx]])
    tmp = sorted(tmp, key = lambda x : x[1])
    for i in tmp:
        if i[2]:
            answer += (10 ** cnt) * i[0]
            cnt -= 2
            if cnt < 0:
                break
    return answer