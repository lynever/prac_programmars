def solution(msg):
    answer = []
    wordic = {chr(i): i - 64 for i in range(65, 91)}
    pos, dicidx = 0, len(wordic) + 1
    while pos < len(msg):
        tmpidx, tmpstr = 0, msg[pos]
        while tmpstr in wordic.keys():
            state = 0
            tmpidx += 1
            if pos + tmpidx < len(msg):
                tmpstr += msg[pos + tmpidx]
            else:
                state = 1
                break
        answer.append(wordic[tmpstr[:-1]] if state == 0 else wordic[tmpstr])
        wordic[tmpstr] = dicidx
        dicidx += 1
        pos += tmpidx
    return answer