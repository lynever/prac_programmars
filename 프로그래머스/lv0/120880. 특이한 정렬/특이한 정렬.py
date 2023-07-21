def solution(numlist, n):
    answer = []
    numlist.sort()
    tmpdic = {}
    for i in numlist:
        tmpdic[i] = abs(i - n)
    srtlst = sorted(tmpdic.items(), key = lambda item:item[1], reverse = True)
    for j in reversed(srtlst):
        answer.append(j[0])
    return answer
