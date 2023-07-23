def solution(spell, dic):
    answer = 2
    spell.sort()
    for i in dic:
        if len(i) == len(spell) and sorted(i) == spell:
            answer = 1
            break
    return answer