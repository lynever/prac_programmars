def solution(score):
    tmplist = []
    answer = []
    for i in score:
        tmplist.append(sum(i) / 2)
    tmplist2 = sorted(tmplist)[::-1]
    for j in tmplist:
        answer.append(tmplist2.index(j) + 1)
    return answer