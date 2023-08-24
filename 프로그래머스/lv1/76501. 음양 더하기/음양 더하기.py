def solution(absolutes, signs):
    answer = ''
    for idx in range(len(absolutes)):
        answer = answer + '+' + str(absolutes[idx]) if signs[idx] == True else answer + '-' + str(absolutes[idx])
    return eval(answer)