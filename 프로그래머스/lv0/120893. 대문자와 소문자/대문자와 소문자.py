def solution(my_string):
    answer = ''
    for i in my_string:
        answer += i.lower() if i.isupper() == True else i.upper()
    return answer