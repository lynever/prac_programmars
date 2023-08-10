def solution(ingredient):
    answer, tmpstk = 0, []
    for i in ingredient:
        tmpstk.append(i)
        if len(tmpstk) >= 4:
            while tmpstk[-4:] == [1, 2, 3, 1]:
                for j in range(4):
                    tmpstk.pop()
                answer += 1
    return answer