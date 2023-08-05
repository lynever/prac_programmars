def solution(array):
    mydic = {val: 0 for val in array}
    for i in array:
        mydic[i] += 1
    mydic = sorted(mydic.items(), key = lambda item: item[1], reverse = True)
    return mydic[0][0] if len(mydic) == 1 or mydic[0][1] != mydic[1][1] else -1