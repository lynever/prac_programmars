def solution(array, n):
    array.sort()
    answer = array[0]
    for i in array:
        if abs(i - n) < abs(answer - n):
            answer = i
    return answer