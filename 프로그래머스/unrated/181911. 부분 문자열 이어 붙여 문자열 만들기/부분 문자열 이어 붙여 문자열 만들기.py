def solution(my_strings, parts):
    answer = ''
    for idx, val in enumerate(my_strings):
        answer += val[parts[idx][0] : parts[idx][1] + 1]
    return answer