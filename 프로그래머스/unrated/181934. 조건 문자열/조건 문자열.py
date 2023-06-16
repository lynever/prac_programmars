def solution(ineq, eq, n, m):
    return 1 if eval(str(n) + ineq + eq + str(m) if eq == '=' else str(n) + ineq + str(m)) else 0