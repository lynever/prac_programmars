import itertools
def solution(nums):
    answer = 0
    nums = list(itertools.combinations(nums, 3))
    for i in nums:
        tmp, state = sum(i), 0
        for j in range(2, int(tmp ** 0.5) + 1):
            if tmp % j == 0:
                state = 1
                break
        if state == 0:
            answer += 1
    return answer