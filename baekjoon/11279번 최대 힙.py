import sys
from heapq import heappush, heappop
myHeap = [] 
input = sys.stdin.readline
for _ in range(int(input())): 
    mess = int(input())
    if mess == 0: 
        if len(myHeap) == 0:  
            print(0)
        else: 
            print(-heappop(myHeap))
    else:
        heappush(myHeap, -mess)
