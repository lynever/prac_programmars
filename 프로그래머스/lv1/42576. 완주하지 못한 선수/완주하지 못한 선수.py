def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for idx, val in enumerate(participant):
        if idx == len(participant) - 1:
            answer = participant[-1]
        elif val != completion[idx]:
            answer = val
            break
    return answer