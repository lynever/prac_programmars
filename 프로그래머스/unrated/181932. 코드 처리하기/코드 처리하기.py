def solution(code):
    answer = ''
    state = 0
    for idx, val in enumerate(code):
        if state == 0:
            if val == '1':
                state = 1
            elif idx % 2 == 0:
                answer += val
        elif state == 1:
            if val == '1':
                state = 0
            elif idx % 2 == 1:
                answer += val
    return answer if len(answer) != 0 else 'EMPTY'