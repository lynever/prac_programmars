def solution(want, number, discount):
    answer, tmpdic = 0, {want[i] : number[i] for i in range(len(want))}
    for j in range(len(discount) - 9):
        cprdic = {}
        for k in range(j, j + 10):
            cprdic[discount[k]] = 1 if discount[k] not in cprdic.keys() else cprdic[discount[k]] + 1
        if cprdic == tmpdic:
            answer += 1
    return answer