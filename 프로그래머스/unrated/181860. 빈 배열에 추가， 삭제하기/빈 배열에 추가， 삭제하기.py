def solution(arr, flag):
    answer = []
    for idx, val in enumerate(flag):
        if val:
            for i in range(0, arr[idx] * 2):
                answer.append(arr[idx])
        else:
            answer = answer[:-arr[idx]]
    return answer