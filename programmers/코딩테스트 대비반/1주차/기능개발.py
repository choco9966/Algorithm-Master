import math

def solution(progresses, speeds):
    '''
    리스트로 작성 
    '''
    answer = []
    remain_day = []
    
    for i in range(len(progresses)):
        remain_day.append(math.ceil((100-progresses[i])/speeds[i]))
    
    for i in range(1, len(progresses)):
        if remain_day[i] <= remain_day[i-1]:
            remain_day[i] = remain_day[i-1]
    
    cnt = 1
    for i in range(1, len(remain_day)):
        if remain_day[i] == remain_day[i-1]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
    
    answer.append(cnt)
    
    return answer

from collections import deque 
def solution(progresses, speeds):
    '''
    deque으로 작성 (리스트에 비해 속도가 5~10배 빠름) 
    '''
    answer = []
    
    remain_day = deque()
    # 작업이 완료되는 요일을 저장하는 곳 
    for i, j in zip(progresses, speeds): 
        remain_day.append(int((100 - i)/j))
        
    # 작업 완료에서 하나를 추출하고 끝난 작업이 몇개인지 확인  
    
    while len(remain_day) > 0: 
        cnt = 1
        start = remain_day.popleft()
        while len(remain_day) > 0: 
            if remain_day[0] <= start: 
                cnt += 1
                remain_day.popleft()
            else:
                break 
        answer.append(cnt)
    return answer
