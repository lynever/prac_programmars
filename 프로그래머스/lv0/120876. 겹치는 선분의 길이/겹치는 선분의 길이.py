def solution(lines):
    answer = 0
    for i in range(min(lines[0][0], lines[1][0], lines[2][0]), max(lines[0][1], lines[1][1], lines[2][1]) + 1):
        state = 0
        if i >= lines[0][0] and i < lines[0][1]:
            state += 1
        if i >= lines[1][0] and i < lines[1][1]:
            state += 1
        if i >= lines[2][0] and i < lines[2][1]:
            state += 1
        if state > 1:
            answer += 1
    return answer