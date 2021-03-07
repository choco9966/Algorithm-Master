# 53712KB	376ms
from collections import deque 
import sys
input = sys.stdin.readline 
myarray = []
for i in range(int(input())): 
    n, m = map(int, input().split())
    myarray.append((n, m))

myqueue = deque(sorted(myarray, key = lambda x:(x[1], x[0])))

cnt = 1
start = myqueue.popleft()
while myqueue: 
    next = myqueue.popleft()
    if next[0] >= start[1]: 
        cnt += 1 
        start = next 
print(cnt)
