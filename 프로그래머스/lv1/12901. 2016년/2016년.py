def solution(a, b):
    daylst = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    idx = 5
    for i in range(a - 1):
        idx = (idx + mon[i]) % 7
    return daylst[(idx + b - 1) % 7]