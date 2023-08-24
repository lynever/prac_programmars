import itertools
def solution(numbers):
    answer, tmp = [], list(itertools.combinations(numbers, 2))
    for i in tmp:
        if sum(i) not in answer:
            answer.append(sum(i))
    return sorted(answer)