def solution(sides):
    answer = 0
    for i in range(abs(sides[0] - sides[1]), sum(sides) + 1):
        if sum(sides) + i > max(sides[0], sides[1], i) * 2:
            answer += 1
    return answer