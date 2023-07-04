def solution(arr, n):
    return [val + n if idx % 2 == 0 else val for idx, val in enumerate(arr)] if len(arr) % 2 == 1 else [val + n if idx % 2 == 1 else val for idx, val in enumerate(arr)]