def solution(strArr):
    return [val.upper() if idx % 2 == 1 else val.lower() for idx, val in enumerate(strArr)]