def solution(babbling):
    answer = 0
    for i in babbling:
        i = i.replace('aya', '0')
        i = i.replace('ye', '0')
        i = i.replace('woo', '0')
        i = i.replace('ma', '0')
        if i.isdigit() == True:
            answer += 1
    return answer