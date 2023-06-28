def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else eval('*'.join([str(i) for i in num_list]))