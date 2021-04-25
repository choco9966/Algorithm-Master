from collections import deque
N = int(input())
dist = deque(list(map(int, input().split())))
cost = deque(list(map(int, input().split())))
before_cost = cost.popleft()

result = 0
while cost: 
    d = dist.popleft()
    c = cost.popleft()
    if before_cost <= c: 
        result += (before_cost*d)
    else:
        result += (before_cost*d)
        before_cost = c
print(result)
