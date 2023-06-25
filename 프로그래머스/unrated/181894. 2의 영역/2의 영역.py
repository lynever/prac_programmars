def solution(arr):
    if 2 not in arr:
        answer = [-1]
    else:
        tmpdic = {2 : []}
        for idx, val in enumerate(arr):
            if val == 2:
                tmpdic[val].append(idx)
        answer = [arr[tmpdic[2][0]]] if len(tmpdic[2]) == 1 else arr[tmpdic[2][0]:tmpdic[2][-1] + 1]
    return answer