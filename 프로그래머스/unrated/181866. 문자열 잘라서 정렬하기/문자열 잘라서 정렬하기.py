def solution(myString):
    return sorted(myString.split('x')) if '' not in myString.split('x') else sorted(myString.split('x'))[sorted(myString.split('x')).count(''):]