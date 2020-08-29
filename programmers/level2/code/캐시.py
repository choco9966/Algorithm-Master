# deque 패키지 : queue에서 left 삽입, 삭제의 메모리 효율을 위해 만든 패키지 
from collections import deque 
def solution(cacheSize, cities):
    answer = 0
    buffer = deque()

    # cacheSize가 0인 경우에는 참조하는 값이 없으므로 전부 5를 곱함 
    if cacheSize == 0: 
        return len(cities) * 5
    # 그렇지 않은경우에는, 모든 city에 대해서 확인 
    # 1. city가 buffer에 있으면 +1, 그렇지 않으면 +5 
    # 2. city가 buffer에 있으면 삭제하고 가장 먼저 참조된 값으로 변경 `buffer.remove(i) -> buffer.append(i)` 
        # city가 buffer에 없으면, buffer의 크기와 cacheSize의 크기를 비교 
        # cacheSize 보다 크기가 크면 가장 오래전 참조된 값을 삭제 `buffer.popleft()`
        # cacheSize 보다 작으면, 단순 삽입 `buffer.append(i)`
    else: 
        for i in cities: 
            # 대소문자는 구분하지 않으므로 lower으로 변경 
            i = i.lower()
            if i in buffer: answer += 1
            else: answer += 5 

            if i in buffer: 
                buffer.remove(i)
            else:
                if len(buffer) >= cacheSize: 
                    buffer.popleft()

            buffer.append(i)
    return answer