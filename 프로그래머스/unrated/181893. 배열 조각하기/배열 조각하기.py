def solution(arr, query):
    for idx, val in enumerate(query):
        arr = arr[:val + 1] if idx % 2 == 0 else arr[val:]
    return arr