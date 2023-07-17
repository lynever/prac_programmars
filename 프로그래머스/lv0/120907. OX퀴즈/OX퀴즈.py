def solution(quiz):
    answer = []
    for i in quiz:
        tmp1, tmp2 = i.split('=')
        answer.append('O' if eval(tmp1) == eval(tmp2) else 'X')
    return answer