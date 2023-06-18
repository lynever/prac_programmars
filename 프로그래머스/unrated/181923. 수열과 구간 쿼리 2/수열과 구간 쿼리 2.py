def solution(arr, queries):
    answer = []
    for i in queries:
        tmp = arr[i[0]:i[1] + 1]
        tmp.sort()
        for j in tmp:
            if j == tmp[-1] and j <= i[2]:
                answer.append(-1)
            elif j > i[2]:
                answer.append(j)
                break
    return answer