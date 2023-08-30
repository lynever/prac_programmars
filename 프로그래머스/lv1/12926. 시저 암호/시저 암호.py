def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif i.isupper() == True:
            answer = answer + chr(ord(i) + n - 26) if ord(i) + n > 90 else answer + chr(ord(i) + n)
        elif i.islower() == True:
            answer = answer + chr(ord(i) + n - 26) if ord(i) + n > 122 else answer + chr(ord(i) + n)
    return answer