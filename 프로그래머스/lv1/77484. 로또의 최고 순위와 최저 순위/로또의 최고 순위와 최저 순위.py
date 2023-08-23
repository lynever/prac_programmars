def solution(lottos, win_nums):
    answer = []
    if lottos.count(0) == len(lottos):
        answer = [1, 6]
    elif len(lottos + win_nums) == len(set(lottos + win_nums)):
        answer = [6, 6]
    else:
        lottos.sort()
        posnum = lottos.count(0)
        lottos = lottos[lottos.count(0):]
        answer.append(7 - (len(lottos + win_nums) - len(set(lottos + win_nums)) + posnum))
        answer.append(7 - (len(lottos + win_nums) - len(set(lottos + win_nums))))
    return answer