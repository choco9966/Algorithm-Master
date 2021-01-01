import heapq

def solution(scoville, K):
    heap = []
    MIX_CNT = 0
    for elm in scoville:
        heapq.heappush(heap, elm)
    
    while heap[0] < K:
        try:
            heapq.heappush(heap, (heapq.heappop(heap) + heapq.heappop(heap)*2))
        except IndexError:
            return -1
        MIX_CNT += 1
        
    return MIX_CNT
