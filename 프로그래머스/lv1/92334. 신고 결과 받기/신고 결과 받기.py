def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    rptcnt, rptlst = {i : 0 for i in id_list}, {i : [] for i in id_list}
    for j in report:
        tmp = j.split(' ')
        if tmp[0] not in rptlst[tmp[1]]:
            rptcnt[tmp[1]] += 1
            rptlst[tmp[1]].append(tmp[0])
    for key, val in rptcnt.items():
        if val >= k:
            for l in rptlst[key]:
                answer[id_list.index(l)] += 1
    return answer