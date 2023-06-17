def solution(num_list):
    oddstr, evenstr = '', ''
    for i in num_list:
        if i % 2 == 0:
            evenstr += str(i)
        else:
            oddstr += str(i)
    return eval(oddstr + '+' + evenstr)