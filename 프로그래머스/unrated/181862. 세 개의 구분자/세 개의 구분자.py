def solution(myStr):
    answer = [i for i in myStr.replace('a', '1').replace('b', '1').replace('c', '1').split('1') if i != '']
    return answer if len(answer) != 0 else ['EMPTY']