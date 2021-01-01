def solution(s):
    '''
    리스트를 이용한 풀이 
    '''
    stack = []
    
    for i in range(len(s)):
        if i == 0:
            stack.append(s[i])
        elif len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
            
    if stack:
        return 0
    else:
        return 1

from collections import deque 
def solution(s):
    '''
    링크드 리스트를 이용한 풀이
    리스트에 비해 2배정도 걸림 
    '''
    s1 = deque(s)
    s2 = deque() 
    
    while s1: 
        x1 = s1.popleft() 
        if len(s1) != 0 and x1 == s1[0]: # aa 겹치는 경우 popleft() 
            s1.popleft()
            if len(s2) != 0: 
                s1.appendleft(s2.pop())
        else: # ba 겹치지 않는 경우 
            s2.append(x1) 
        
    if len(s2) == 0: 
        return 1 
    else:
        return 0 
