import heapq

def solution(N, works):
    if N > sum(works) :
        return 0
    # heap은 원래 최소 힙을 기준으로 하지만 -를 붙여서 최대 힙으로 변경이 가능 
    works = [(-i, i) for i in works]
    # 기존 리스트를 heap으로 변환하는 코드
    heapq.heapify(works)
    for _ in range(N) :
        # 가장 값이 큰 작업을 꺼내서 작업량 1을 수행 
        # [1]은 우선 순위에는 관심이 없으므로 값만 가져옴 
        w = heapq.heappop(works)[1] - 1
        # works에 수정된 w를 추가 
        heapq.heappush(works, (-w, w))
    return sum([i[1]**2 for i in works])
