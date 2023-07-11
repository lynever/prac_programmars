def solution(n_str):
    answer, state = '', 0
    for idx, val in enumerate(n_str):
        if val != '0':
            answer += val
            state = 1
        elif val == '0' and state == 1:
            answer += val
    return answer