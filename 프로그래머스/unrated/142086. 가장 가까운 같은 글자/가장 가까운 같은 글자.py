def solution(s):
    answer = []
    for i in range(0, len(s)):
        compstr = s[0:i]
        answer.append(compstr[::-1].find(s[i]) if compstr[::-1].find(s[i]) == -1 else compstr[::-1].find(s[i]) + 1)
    return answer