from heapq import heappush, heappop
def solution(scoville, K):
    answer = 0
    scoville = sorted(scoville)

    while len(scoville) > 1:
        if scoville[0] >= K:
            return answer
        else:
            a = heappop(scoville)
            b = heappop(scoville)
            heappush(scoville, a+b*2)
            answer += 1
    if scoville[0] < K:
        return -1
    else:
        return answer
