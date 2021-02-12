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
