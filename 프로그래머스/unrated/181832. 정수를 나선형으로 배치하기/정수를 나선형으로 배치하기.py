def solution(n):
    answer = [[0 for _ in range(n)] for __ in range(n)]
    answer[0][0] = 1
    now, strt, num = 1, [0, 1], 2
    while sum(answer, []).count(0) != 0:
        answer[strt[0]][strt[1]] = num
        if now == 0:
            if strt[1] - 1 < 0 or answer[strt[0]][strt[1] - 1] != 0:
                now = 2
                strt[0] -= 1
            else:
                strt[1] -= 1
        elif now == 1:
            if strt[1] + 1 >= n or answer[strt[0]][strt[1] + 1] != 0:
                now = 3
                strt[0] += 1
            else:
                strt[1] += 1
        elif now == 2:
            if strt[0] - 1 < 0 or answer[strt[0] - 1][strt[1]] != 0:
                now = 1
                strt[1] += 1
            else:
                strt[0] -= 1
        elif now == 3:
            if strt[0] + 1 >= n or answer[strt[0] + 1][strt[1]] != 0:
                now = 0
                strt[1] -= 1
            else:
                strt[0] += 1
        num += 1
    return answer