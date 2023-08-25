def dist(pos, tar):
    dis, phonepos = 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11]
    npos, tpos = phonepos.index(pos), phonepos.index(tar)
    dis = (tpos // 3 - npos // 3) + abs((tpos // 3 - npos // 3) * 3 + npos - tpos) if tpos > npos else (npos // 3 - tpos // 3) + abs((npos // 3 - tpos // 3) * 3 + tpos - npos)
    return dis

def solution(numbers, hand):
    answer = ''
    lpos, rpos = 10, 11
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            lpos = i
        elif i in [3, 6, 9]:
            answer += 'R'
            rpos = i
        elif i in [2, 5, 8, 0]:
            ldis, rdis = dist(lpos, i), dist(rpos, i)
            if ldis == rdis:
                if hand == 'right':
                    answer += 'R'
                    rpos = i
                else:
                    answer += 'L'
                    lpos = i
            else:
                if ldis > rdis:
                    answer += 'R'
                    rpos = i
                else:
                    answer += 'L'
                    lpos = i
    return answer