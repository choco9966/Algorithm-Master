'''
다음 후보가 맞으면 탐색을 안하기에 코드는 길어졌지만 속도는 빨라짐 
35532KB, 224ms
'''
from collections import deque
N, K = map(int, input().split())
if N == K : 
    print(0)
else:
    visited = [0] * (100000+1)
    queue = deque([[N, 0]])
    while queue: 
        x, t = queue.popleft()
        if x-1 == K or 2*x == K or x+1 == K: 
            t += 1
            break 
        else: 
            if 2*x >= 0 and 2*x <= 100000 and 2*x and visited[2*x] == 0: 
                queue.append([2*x, t+1])
                visited[2*x] = t+1
            
            if x-1 >= 0 and x-1 <= 100000 and x-1 and visited[x-1] == 0: 
                queue.append([x-1, t+1])
                visited[x-1] = t+1

            if x+1 >= 0 and x+1 <= 100000 and x+1 and visited[x+1] == 0: 
                queue.append([x+1, t+1])
                visited[x+1] = t+1
    print(t)

'''
43764KB, 372ms
'''
from collections import deque
N, K = map(int, input().split())
T = max(N, K)
visited = [0 for _ in range(0, T*2+1)]

queue = deque([(N, 0)])
while queue:
    v = queue.popleft()
    n, cnt = v[0], v[1]
    if n == K: 
        print(cnt)
        break
    else:
        if not visited[n]:
            visited[n] = 1
            if (n*2) <= T*2: 
                queue.append((2*n, cnt+1))
            if (n+1) <= T*2: 
                queue.append((n+1, cnt+1))
            if (n-1) >= 0: 
                queue.append((n-1, cnt+1))
