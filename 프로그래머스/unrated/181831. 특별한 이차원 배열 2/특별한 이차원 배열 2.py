def solution(arr):
    answer = 1
    for idx, val in enumerate(arr):
        for inidx, inval in enumerate(val):
            if arr[idx][inidx] != arr[inidx][idx]:
                answer = 0
                break
    return answer