def solution(maps):
    xlen, ylen = len(maps[0]), len(maps)
    maps = sum(maps, [])
    visited = [-1 for _ in range(len(maps))]
    visited[0] = 1
    now = {0}
    while 1:
        if visited[-1] != -1:
            break
        if len(now) == 0:
            break
        else:
            tmp = set()
            for nxt in now:
                if nxt + 1 < len(maps) and nxt // xlen == (nxt + 1) // xlen and maps[nxt + 1] == 1 and visited[nxt + 1] == -1:
                    visited[nxt + 1] = visited[nxt] + 1
                    tmp.add(nxt + 1)
                if nxt - 1 >= 0 and nxt // xlen == (nxt - 1) // xlen and maps[nxt - 1] == 1 and visited[nxt - 1] == -1:
                    visited[nxt - 1] = visited[nxt] + 1
                    tmp.add(nxt - 1)
                if nxt + xlen < len(maps) and maps[nxt + xlen] == 1 and visited[nxt + xlen] == -1:
                    visited[nxt + xlen] = visited[nxt] + 1
                    tmp.add(nxt + xlen)
                if nxt - xlen >= 0 and maps[nxt - xlen] == 1 and visited[nxt - xlen] == -1:
                    visited[nxt - xlen] = visited[nxt] + 1
                    tmp.add(nxt - xlen)
            now = tmp
    return visited[-1]