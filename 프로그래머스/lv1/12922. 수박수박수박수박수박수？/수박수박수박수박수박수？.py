def solution(n):
    return ''.join(['수' if _ % 2 == 1 else '박' for _ in range(1, n + 1)])