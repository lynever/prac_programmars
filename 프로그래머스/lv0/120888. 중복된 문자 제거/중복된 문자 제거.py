def solution(my_string):
    answer = ''
    for i in my_string:
        if answer.find(i) == -1:
            answer += i
    return answer