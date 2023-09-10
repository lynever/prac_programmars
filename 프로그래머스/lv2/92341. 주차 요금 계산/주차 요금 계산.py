import math
def solution(fees, records):
    answer, cardic = [], {}
    for i in records:
        i = i.split(' ')
        hour, minute = i[0].split(':')
        if i[1] not in cardic.keys() and i[2] == 'IN':
            cardic[i[1]] = [(int(hour) * 60 + int(minute)) * -1, 0]
        elif i[2] == 'OUT':
            cardic[i[1]][0] += int(hour) * 60 + int(minute)
            cardic[i[1]][1] = 1
        elif i[2] == 'IN':
            cardic[i[1]][0] += (int(hour) * 60 + int(minute)) * -1
            cardic[i[1]][1] = 0
    for key, val in cardic.items():
        if val[1] == 0:
            val[0] += 23 * 60 + 59
            val[1] = 1
    cardic = sorted(cardic.items())
    for num, time in cardic:
        answer.append(fees[1] + math.ceil((time[0] - fees[0]) / fees[2]) * fees[3] if time[0] > fees[0] else fees[1])
    return answer