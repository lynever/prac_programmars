def solution(s):
    answer, s = '', s.lower()
    for idx, string in enumerate(s):
        if idx == 0 and string.isalpha():
            answer += string.upper()
        elif idx != 0 and s[idx - 1] == ' ' and string.isalpha():
            answer += string.upper()
        else:
            answer += string
    return answer