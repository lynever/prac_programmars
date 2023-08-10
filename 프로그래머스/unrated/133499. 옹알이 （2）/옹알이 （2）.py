def solution(babbling):
    answer = 0
    for i in babbling:
        i = i.replace('ayaaya', '#')
        i = i.replace('yeye', '#')
        i = i.replace('woowoo', '#')
        i = i.replace('mama', '#')
        i = i.replace('aya', '0')
        i = i.replace('ye', '1')
        i = i.replace('woo', '2')
        i = i.replace('ma', '3')
        answer = answer + 1 if i.isdigit() == True else answer
    return answer