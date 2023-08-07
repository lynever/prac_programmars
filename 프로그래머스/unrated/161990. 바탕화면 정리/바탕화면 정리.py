def solution(wallpaper):
    answer, start, end = [], [len(wallpaper), len(wallpaper[0])], [0, 0]
    for xidx, val in enumerate(wallpaper):
        for yidx, val2 in enumerate(val):
            if val2 == '#':
                if xidx <= start[0]:
                    start[0] = xidx
                if xidx >= end[0]:
                    end[0] = xidx + 1
                if yidx <= start[1]:
                    start[1] = yidx
                if yidx >= end[1]:
                    end[1] = yidx + 1
    answer = start + end
    return answer