def solution(numLog):
    answer = ''
    for idx, val in enumerate(numLog):
        if idx == 0:
            pass
        else:
            if val - numLog[idx - 1] == 1:
                answer += 'w'
            elif val - numLog[idx - 1] == -1:
                answer += 's'
            elif val - numLog[idx - 1] == 10:
                answer += 'd'
            elif val - numLog[idx - 1] == -10:
                answer += 'a'
    return answer