def solution(players, callings):
    idxdic = {player: idx + 1 for idx, player in enumerate(players)}
    pdic = {idx + 1: player for idx, player in enumerate(players)}
    for i in callings:
        pos = idxdic[i]
        idxdic[i] -= 1
        pdic[pos] = pdic[pos - 1]
        pdic[pos - 1] = i
        idxdic[pdic[pos]] += 1
    return list(pdic.values())