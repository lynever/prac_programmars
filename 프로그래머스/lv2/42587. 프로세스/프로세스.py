from collections import deque
def solution(priorities, location):
    idxlst, reslst = deque([i for i in range(len(priorities))]), []
    priorities = deque(priorities)
    while len(priorities) != 0:
        maxprt = max(priorities)
        if priorities[0] == maxprt:
            reslst.append((priorities[0], idxlst[0]))
            priorities.popleft()
            idxlst.popleft()
        else:
            priorities.append(priorities[0])
            priorities.popleft()
            idxlst.append(idxlst[0])
            idxlst.popleft()
    for idx, val in enumerate(reslst):
        if val[1] == location:
            answer = idx + 1
    return answer