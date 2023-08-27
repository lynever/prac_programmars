def solution(x):
    return x % eval('+'.join(str(x))) == 0