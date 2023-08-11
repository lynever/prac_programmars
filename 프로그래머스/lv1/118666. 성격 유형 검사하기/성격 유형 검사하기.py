def score(charactertype, num):
    scr = ''
    if num == 1:
        scr = charactertype[0] + '3'
    elif num == 2:
        scr = charactertype[0] + '2'
    elif num == 3:
        scr = charactertype[0] + '1'
    elif num == 4:
        scr = '0'
    elif num == 5:
        scr = charactertype[1] + '1'
    elif num == 6:
        scr = charactertype[1] + '2'
    elif num == 7:
        scr = charactertype[1] + '3'
    return scr

def solution(survey, choices):
    answer = ''
    survtype = 'RTCFJMAN'
    survdic = {tmp : 0 for tmp in survtype}
    for idx, x in enumerate(survey):
        scr = score(x, choices[idx])
        if len(scr) != 1:
            survdic[scr[0]] += int(scr[1])
    answer += survtype[0] if survdic[survtype[0]] >= survdic[survtype[1]] else survtype[1]
    answer += survtype[2] if survdic[survtype[2]] >= survdic[survtype[3]] else survtype[3]
    answer += survtype[4] if survdic[survtype[4]] >= survdic[survtype[5]] else survtype[5]
    answer += survtype[6] if survdic[survtype[6]] >= survdic[survtype[7]] else survtype[7]
    return answer