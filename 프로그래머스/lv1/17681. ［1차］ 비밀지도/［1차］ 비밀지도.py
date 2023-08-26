def solution(n, arr1, arr2):
    answer, tmp, tmp2 = [], [], []
    for val in arr1:
        tmp.append('0' * (n - len(bin(val)[2:])) + bin(val)[2:] if len(bin(val)[2:]) < n else bin(val)[2:])
    for val2 in arr2:
        tmp2.append('0' * (n - len(bin(val2)[2:])) + bin(val2)[2:] if len(bin(val2)[2:]) < n else bin(val2)[2:])
    for i in range(0, n):
        tmpstr = ''
        for j in range(0, n):
            tmpstr = tmpstr + '#' if tmp[i][j] == '1' or tmp2[i][j] == '1' else tmpstr + ' '
        answer.append(tmpstr)
    return answer