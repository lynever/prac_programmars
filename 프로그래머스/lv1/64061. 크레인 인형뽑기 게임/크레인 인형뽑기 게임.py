def solution(board, moves):
    answer, bas = 0, []
    board = [j for i in board for j in i]
    for k in moves:
        for l in range(k - 1, len(board), int(len(board) ** 0.5)):
            if board[l] != 0:
                bas.append(board[l])
                board[l] = 0
                if len(bas) > 1 and bas[-1] == bas[-2]:
                    bas = bas[:-2]
                    answer += 2
                break
    return answer