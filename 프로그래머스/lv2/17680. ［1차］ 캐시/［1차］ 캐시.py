from collections import deque
def solution(cacheSize, cities):
    cachelst = deque()
    answer = len(cities) * 5 if cacheSize == 0 else 0
    if answer == 0:
        for i in cities:
            i = i.lower()
            if i not in cachelst:
                answer += 5
                if len(cachelst) >= cacheSize:
                    cachelst.popleft()
                cachelst.append(i)
            else:
                answer += 1
                cachelst.remove(i)
                cachelst.append(i)
    return answer