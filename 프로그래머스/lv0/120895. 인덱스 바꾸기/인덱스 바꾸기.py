def solution(my_string, num1, num2):
    tmplist = list(my_string)
    tmp = tmplist[num1]
    tmplist[num1] = tmplist[num2]
    tmplist[num2] = tmp
    return ''.join(tmplist)