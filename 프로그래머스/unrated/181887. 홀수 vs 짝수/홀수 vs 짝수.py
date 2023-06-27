def solution(num_list):
    oddsum, evensum = 0, 0
    for i in range(0, len(num_list), 2):
        oddsum += num_list[i]
        evensum = evensum + num_list[i + 1] if i + 1 < len(num_list) else evensum + 0
    return max(oddsum, evensum)