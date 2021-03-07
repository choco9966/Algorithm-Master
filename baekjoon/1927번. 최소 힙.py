# 34700KB	168ms
import sys 
from heapq import heappop, heappush  
input = sys.stdin.readline 
minQueue = []
N = int(input())
for _ in range(N): 
    mess = int(input())
    if mess == 0: 
        if len(minQueue) == 0: 
            print(0)
        else:
            print(heappop(minQueue))
    else: 
        heappush(minQueue, mess)
