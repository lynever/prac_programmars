def solution(num, total):
    answer = []
    if total // num == total / num:
        for i in range(total // num - num // 2, total // num + num // 2 + 1):
            answer.append(i)
    else:
        for i in range(total // num - num // 2 + 1, total // num + num // 2 + 1):
            answer.append(i)
    return answer