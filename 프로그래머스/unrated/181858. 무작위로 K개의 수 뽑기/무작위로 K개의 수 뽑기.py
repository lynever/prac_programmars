def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    answer = answer[:k] if len(answer) > k else answer + [-1] * (k - len(answer))
    return answer