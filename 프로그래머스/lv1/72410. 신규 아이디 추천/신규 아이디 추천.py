def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in '-_.':
            answer += i
    for j in range(answer.count('.'), 1, -1):
        answer = answer.replace('.' * j, '.')
    if len(answer) != 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]
    if answer == '':
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    elif len(answer) <= 2:
        while len(answer) <= 2:
            answer += answer[-1]
    return answer