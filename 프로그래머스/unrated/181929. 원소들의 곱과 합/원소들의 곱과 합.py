def solution(num_list):
    tmp = 1
    for i in num_list:
        tmp *= i
    return 1 if tmp < sum(num_list) ** 2 else 0