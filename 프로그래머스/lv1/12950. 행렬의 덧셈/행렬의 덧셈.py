def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmplst = []
        for j in range(len(arr1[0])):
            tmplst.append(arr1[i][j] + arr2[i][j])
        answer.append(tmplst)
    return answer