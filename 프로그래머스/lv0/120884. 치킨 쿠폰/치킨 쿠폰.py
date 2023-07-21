def solution(chicken):
    answer, cou = 0, chicken
    while cou >= 10:
        answer += int(cou / 10)
        cou = cou - 9 * int(cou / 10)
    return answer