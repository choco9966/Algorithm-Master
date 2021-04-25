import sys
from collections import deque
mystack = deque([])
N = int(input())
# input = sys.stdin.readline
for _ in range(N):
    m = list(map(str,input().split()))   
    if m[0] == 'push_front':
        mystack.appendleft(int(m[1]))
    elif m[0] == 'push_back':
        mystack.append(int(m[1]))
    elif m[0] == 'pop_front':
        if len(mystack) == 0: print(-1)
        else: print(mystack.popleft())
    elif m[0] == 'pop_back':
        if len(mystack) == 0: print(-1)
        else: print(mystack.pop())
    elif m[0] == 'size':
        print(len(mystack))
    elif m[0] == 'empty':
        if len(mystack) == 0: print(1)
        else: print(0)    
    elif m[0] == 'front':
        if len(mystack) == 0: print(-1)
        else: print(mystack[0])
    else:
        if len(mystack) == 0: print(-1)
        else: print(mystack[-1])        
