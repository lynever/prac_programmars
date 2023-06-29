def solution(myString):
    return ''.join([i.upper() if i in 'aA' else i.lower() for i in myString])