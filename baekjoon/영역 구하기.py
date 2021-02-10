from collections import deque
def bfs(x, y): 
    queue = deque([(x, y)])
    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    area = 1
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for delta in deltas: 
            nx, ny = x+delta[0], y+delta[1]
            if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] == 0 and visited[nx][ny] == 0 and (nx, ny) not in queue:
                queue.append((nx, ny))
                area += 1
    return area

M, N, K = map(int, input().split(' '))
rectangle = [list(map(int, input().split())) for _ in range(K)]
visited = [[0] * N for _ in range(M)]
matrix = [[0] * N for _ in range(M)]
for rec in rectangle: 
    x1, y1, x2, y2 = rec[0], rec[1], rec[2], rec[3]
    for i in range(M-y2, M-y1):
        for j in range(min(x1, x2), max(x1, x2)):
            matrix[i][j] = 1

cnt = 0
result = []
for i in range(0, M):
    for j in range(0, N):
        if matrix[i][j] == 0 and visited[i][j] == 0: 
            result.append(bfs(i, j))
            cnt += 1
result = sorted(result)
print(cnt)
print(' '.join(list(map(str, result))))
