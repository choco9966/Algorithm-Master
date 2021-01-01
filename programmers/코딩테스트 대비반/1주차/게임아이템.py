import heapq
from collections import deque

def solution(healths, items):
    '''
    정답은 맞았지만 시간초과한 코드
    '''
    answer = []
    healths = sorted(healths)
        
    items_ = [] 
    for idx, item in enumerate(items): 
        items_.append((idx+1, item[0], item[1]))
    
    items = sorted(items_, key = lambda x: -x[1])
    for item in items: 
        for idx, health in enumerate(healths): 
            if health - item[2] >= 100:
                answer.append(item[0])
                if idx != (len(healths) -1): 
                    healths = healths[0:idx] + healths[idx+1:]
                    break
                else:
                    healths.pop()
    return sorted(answer)



import heapq
from collections import deque

def solution(healths, items):
    '''
    heap을 이용한 풀이
    - 체력이 낮은 순서와 아이템의 체력을 낮추는 값이 작은 순서대로 매핑
    - candidates에 기존의 탐색한 값도 저장되어있어서 시간이 효과적 
    '''
    healths.sort()
    items = [(*item, idx) for idx, item in enumerate(items, 1)]
    ATK, HP, INDEX = 0, 1, 2
    items.sort(key=lambda x: x[HP])
    items = deque(items)
    candidates = []
    answer = []
    
    for health in healths:
        while items and health - items[0][HP] >= 100:
            item = items.popleft()
            heapq.heappush(candidates, (-item[ATK], item[INDEX]))
        if candidates:
            answer.append(heapq.heappop(candidates)[1])

    answer.sort()
    return answer


