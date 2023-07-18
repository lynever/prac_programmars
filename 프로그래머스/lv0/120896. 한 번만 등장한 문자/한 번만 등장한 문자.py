def solution(s):
    tmp = ''
    for i in s:
        if s.count(i) == 1:
            tmp += i
    answer = ''.join(sorted(tmp))
    return answer