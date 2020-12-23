import heapq


def solution(scoville, K):
    answer = 0  # 횟수
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while len(heap) > 1:
        if heap[0] >= K:
            return answer
        else:
            make_it_spicy(heap)
            answer += 1
    if heap[0] >= K:
        return answer
    else:
        return -1


def make_it_spicy(heap: list):
    min1 = heapq.heappop(heap)
    min2 = heapq.heappop(heap)
    new_value = min1 + (2 * min2)
    heapq.heappush(heap, new_value)