def solution(t, p):
    answer, complist = 0, []
    for i in range(0, len(t)):
        if i + len(p) <= len(t):
            complist.append(t[i:i + len(p)])
    for j in complist:
        if int(j) <= int(p):
            answer += 1
    return answer