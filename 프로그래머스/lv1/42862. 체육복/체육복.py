def solution(n, lost, reserve):
    have = [1 for _ in range(n)]
    for i in range(n):
        have[i] = have[i] - 1 if i + 1 in lost else have[i]
        have[i] = have[i] + 1 if i + 1 in reserve else have[i]
    have_left = list(have)
    for idx, val in enumerate(have_left):
        if val == 0 and idx != n - 1:
            if have_left[idx + 1] == 2:
                have_left[idx] += 1
                have_left[idx + 1] -= 1
    for j in range(n - 1, -1, -1):
        if have_left[j] == 0 and j != 0:
            if have_left[j - 1] == 2:
                have_left[j] += 1
                have_left[j - 1] -= 1
    have_right = list(have)
    for j in range(n - 1, -1, -1):
        if have_right[j] == 0 and j != 0:
            if have_right[j - 1] == 2:
                have_right[j] += 1
                have_right[j - 1] -= 1
    for idx, val in enumerate(have_right):
        if val == 0 and idx != n - 1:
            if have_right[idx + 1] == 2:
                have_right[idx] += 1
                have_right[idx + 1] -= 1
    return n - min(have_left.count(0), have_right.count(0))