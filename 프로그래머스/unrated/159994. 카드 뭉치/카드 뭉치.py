def solution(cards1, cards2, goal):
    idx1, idx2, state = 0, 0, 1
    for i in goal:
        if idx1 < len(cards1) and cards1[idx1] == i:
            idx1 += 1
        elif idx2 < len(cards2) and cards2[idx2] == i:
            idx2 += 1
        else:
            state = 0
            break
    return 'No' if state == 0 else 'Yes'