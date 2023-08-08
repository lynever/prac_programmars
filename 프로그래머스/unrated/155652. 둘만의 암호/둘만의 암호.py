def solution(s, skip, index):
    answer, alplist = '', []
    for i in range(97, 123):
        if chr(i) not in skip:
            alplist.append(chr(i))
    for j in s:
        answer += alplist[(alplist.index(j) + index) % len(alplist)]
    return answer