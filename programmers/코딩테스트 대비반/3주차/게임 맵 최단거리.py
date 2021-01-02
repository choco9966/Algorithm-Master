from collections import deque

def bfs(starts, maps):
    answer = 0
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    queue = deque()
    queue.append(starts)
    
    while queue:
        x, y, cnt = queue.popleft()
        maps[x][y] = 0
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if nx == len(maps)-1 and ny == len(maps[0])-1:
                return cnt + 1
            elif visitable(nx, ny, maps):
                maps[nx][ny] = 0
                queue.append((nx, ny, cnt+1))
    return -1

def visitable(nx, ny, maps):
    return 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny]

def solution(maps):
    return bfs((0,0,1), maps)
