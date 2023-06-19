def solution(number):
    answer = 0
    tmplst = list(str(number))
    for i in tmplst:
        answer += int(i)
    return answer % 9