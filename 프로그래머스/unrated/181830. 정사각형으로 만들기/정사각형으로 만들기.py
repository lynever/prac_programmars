def solution(arr):
    if len(arr) > len(arr[0]):
        for i in range(len(arr)):
            for _ in range(len(arr) - len(arr[i])):
                arr[i].append(0)
    elif len(arr) < len(arr[0]):
        tmplst = [0] * len(arr[0])
        for _ in range(len(arr[0]) - len(arr)):
            arr.append(tmplst)
                    
    return arr