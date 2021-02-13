from collections import deque
import sys
input = sys.stdin.readline
A, B = map(int, input().split())
queue = deque([(A, 1)])
result = -1
while queue: 
    num, cnt = queue.popleft()
    if num == B: 
        result = (cnt)
        break

    if num*2 <= B:
        queue.append((num*2, cnt+1))
        
    if int(str(num)+'1') <= B: 
        queue.append((int(str(num)+'1'), cnt+1))

print(result)
