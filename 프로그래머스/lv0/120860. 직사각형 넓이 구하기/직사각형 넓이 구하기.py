def incline(dot1, dot2):
    if dot1[0] - dot2[0] == 0:
        return 0
    else:
        return (dot1[1] - dot2[1]) / (dot1[0] - dot2[0])
def distance(dot1, dot2):
    return ((dot2[0] - dot1[0]) ** 2 + (dot2[1] - dot1[1]) ** 2) ** 0.5
def solution(dots):
    answer = 0
    if incline(dots[0], dots[1]) == 0 or incline(dots[0], dots[2]) == 0:
        wid = hei = 0
        for i in range(1, len(dots)):
            if dots[0][0] == dots[i][0]:
                hei = abs(dots[i][1] - dots[0][1])
            elif dots[0][1] == dots[i][1]:
                wid = abs(dots[i][0] - dots[0][0])
        answer = wid * hei
    elif incline(dots[0], dots[1]) * incline(dots[0], dots[2]) == -1:
        answer = distance(dots[0], dots[1]) * distance(dots[0], dots[2])
    elif incline(dots[0], dots[1]) * incline(dots[0], dots[3]) == -1:
        answer = distance(dots[0], dots[1]) * distance(dots[0], dots[3])
    elif incline(dots[0], dots[2]) * incline(dots[0], dots[3]) == -1:
        answer = distance(dots[0], dots[2]) * distance(dots[0], dots[3])
    return answer