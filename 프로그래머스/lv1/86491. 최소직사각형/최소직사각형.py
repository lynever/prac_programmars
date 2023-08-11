def solution(sizes):
    maxlst, minlst = [], []
    for i in sizes:
        maxlst.append(max(i))
        minlst.append(min(i))
    return max(maxlst) * max(minlst)