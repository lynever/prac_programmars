def solution(n):
    answer, tmpstr = 0, str(n)
    for i in tmpstr:
        answer += int(i)
    return answer