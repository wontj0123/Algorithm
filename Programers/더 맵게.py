import heapq as hq


def solution(scoville, K):
    count = 0
    hq.heapify(scoville)

    while 1:
        if len(scoville) <= 1 and scovile[0] < K:
            break
        if scoville[0] >= K:
            break
        new_num = hq.heappop(scoville) + (hq.heappop(scoville) * 2)
        hq.heappush(scoville, new_num)
        count += 1
    return count