def solution(board):
    cprlst, n  = [], len(board)
    safezone = [0 for _ in range(n ** 2)]
    for i in range(n ** 2):
        if board[i // n][i % n] == 1:
            if (i - n - 1) // n == (i - n) // n:
                cprlst.append(i - n - 1)
            cprlst.append(i - n)
            if (i - n + 1) // n == (i - n) // n:
                cprlst.append(i - n + 1)
            if (i - 1) // n == i // n:
                cprlst.append(i - 1)
            cprlst.append(i)
            if (i + 1) // n == i // n:
                cprlst.append(i + 1)
            if (i + n - 1) // n == (i + n) // n:
                cprlst.append(i + n - 1)
            cprlst.append(i + n)
            if (i + n + 1) // n == (i + n) // n:
                cprlst.append(i + n + 1)
            for j in cprlst:
                if 0 <= j < len(safezone) and not safezone[j]:
                    safezone[j] = 1
    return safezone.count(0)