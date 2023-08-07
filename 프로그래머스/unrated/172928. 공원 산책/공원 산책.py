def solution(park, routes):
    w, h = len(park[0]), len(park)
    park = list(''.join(park))
    now = park.index('S')
    for i in routes:
        dire, num = i.split(' ')
        if dire == 'E':
            if (now + int(num)) // w == now // w:
                state = 1
                for j in range(now, now + int(num) + 1):
                    if park[j] == 'X':
                        state = 0
                        break
                if state == 1:
                    now += int(num)
        elif dire == 'W':
            if abs(now - int(num)) // w == now // w and now - int(num) >= 0:
                state = 1
                for j in range(now, now - int(num) - 1, -1):
                    if park[j] == 'X':
                        state = 0
                        break
                if state == 1:
                    now -= int(num)
        elif dire == 'S':
            if now + w * int(num) < len(park):
                state = 1
                for j in range(now, now + w * int(num) + 1, w):
                    if park[j] == 'X':
                        state = 0
                        break
                if state == 1:
                    now += w * int(num)
        elif dire == 'N':
            if now - w * int(num) >= 0:
                state = 1
                for j in range(now, now - w * int(num) - 1, -w):
                    if park[j] == 'X':
                        state = 0
                        break
                if state == 1:
                    now -= w * int(num)
    return [now // w, now % w]