def solution(s):
    answer = 0
    s = s.split(' ')
    for i in range(0, len(s)):
        answer = answer - int(s[i - 1]) if s[i] == 'Z' else answer + int(s[i])
    return answer