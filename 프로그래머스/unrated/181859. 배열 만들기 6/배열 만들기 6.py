def solution(arr):
    answer, i = [], 0
    while i < len(arr):
        if answer == []:
            answer.append(arr[i])
        elif answer[-1] == arr[i]:
            answer = answer[:-1]
        else:
            answer.append(arr[i])
        i += 1
    return answer if len(answer) != 0 else [-1]