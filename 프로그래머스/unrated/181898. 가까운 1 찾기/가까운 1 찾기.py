def solution(arr, idx):
    answer = -1
    for arridx, val in enumerate(arr):
        if arridx >= idx and val == 1:
            answer = arridx
            break
    return answer