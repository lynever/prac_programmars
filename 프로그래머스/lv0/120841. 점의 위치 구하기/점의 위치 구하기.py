def solution(dot):
    if dot[0] > 0:
        answer = 1 if dot[1] > 0 else 4
    else:
        answer = 2 if dot[1] > 0 else 3
    return answer