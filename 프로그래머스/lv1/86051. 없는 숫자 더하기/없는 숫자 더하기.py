def solution(numbers):
    answer, mydic = 0, {i: 0 for i in range(0, 10)}
    for j in numbers:
        mydic[j] += 1
    for key, val in mydic.items():
        if val == 0:
            answer += key
    return answer