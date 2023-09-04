def solution(n):
    answer = 0
    tmp = n
    while tmp != 0:
        sum = 0
        for i in range(tmp, 0, -1):
            sum += i
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
        tmp -= 1
    return answer