def solution(my_string):
    answer, tmpstr = 0, ""
    for i in my_string:
        if i.isdigit():
            tmpstr += i
        elif tmpstr != '':
            answer += int(tmpstr)
            tmpstr = ''
    if tmpstr != '':
        answer += int(tmpstr)
    return answer