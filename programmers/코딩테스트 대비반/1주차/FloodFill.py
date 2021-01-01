from collections import deque

def solution(n, m, images):
    answer = 0
    visited = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                answer += 1
                visited[i][j] = True
                bfs(n, m, i, j, images, visited)
                
    return answer

def bfs(n, m, x, y, images, visited):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        
        DELTAS = ((0, 1),(0, -1),(1, 0),(-1, 0))
        for dx, dy in DELTAS:
            next_x, next_y = x + dx, y + dy
            
            if visitable(n, m, next_x, next_y, visited) and images[next_x][next_y] == images[x][y]:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True

def visitable(n, m, x, y, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]
