import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) != 1:
        answer += 1
        add1 = heapq.heappop(scoville)
        add2 = heapq.heappop(scoville)
        heapq.heappush(scoville, add1 + add2 * 2)
    if len(scoville) == 1 and scoville[0] < K:
        answer = -1
    return answer