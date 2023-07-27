def checkmax(n, maxn):
    if abs(n) > abs(maxn):
        return 0
    else:
        return 1
def solution(keyinput, board):
    answer, maxn = [0, 0], [board[0]//2, board[1]//2]
    for i in keyinput:
        if i == 'left':
            if checkmax(answer[0] - 1, maxn[0]):
                answer[0] -= 1
        elif i == 'right':
            if checkmax(answer[0] + 1, maxn[0]):
                answer[0] += 1
        elif i == 'up':
            if checkmax(answer[1] + 1, maxn[1]):
                answer[1] += 1
        elif i == 'down':
            if checkmax(answer[1] - 1, maxn[1]):
                answer[1] -= 1
    return answer