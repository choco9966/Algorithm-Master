# DFS
# 33604KB, 108ms
import sys 
from collections import deque 
input = sys.stdin.readline
T = int(input())
sys.setrecursionlimit(10**6)

def visitable(n, m, x, y, visited):
    return 0 <= x < n and 0 <= y < m and (visited[x][y] == 0)

def dfs(n, m, x, y, matrix, visited, cnt):
    visited[x][y] = 1
    deltas = ((0, 1), (0, -1), (1, 0), (-1, 0))
    for dx, dy in deltas: 
        next_x, next_y = x + dx, y + dy 
        if visitable(n, m, next_x, next_y, visited) and (matrix[next_x][next_y] == 1): 
            visited[next_x][next_y] = 1
            cnt = dfs(n, m, next_x, next_y, matrix, visited, cnt+1)
    return cnt

for _ in range(T): 
    answer = []
    M, N, K = map(int, input().split(' '))
    matrix = [[0 for c in range(N)] for c in range(M)]
    for _ in range(K): 
        x, y = map(int, input().split(' '))
        matrix[x][y] = 1
    visited = [[0] * (N) for _ in range(M)]
    for i in range(M): 
        for j in range(N): 
            if (visited[i][j] == 0) & (matrix[i][j]==1): 
                visited[i][j] = 1 
                answer += [dfs(M, N, i, j, matrix, visited, 1)]
    print(len(answer))
    
# BFS 
# 32788KB, 116ms
import sys 
from collections import deque 
input = sys.stdin.readline
T = int(input())

def visitable(n, m, x, y, visited):
    return 0 <= x < n and 0 <= y < m and (visited[x][y] == 0)

def bfs(n, m, x, y, matrix, visited, cnt):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visited[i][j] = 1
        deltas = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dx, dy in deltas: 
            next_x, next_y = x + dx, y + dy 
            if visitable(n, m, next_x, next_y, visited) and (matrix[next_x][next_y] == 1): 
                queue.append((next_x, next_y))
                visited[next_x][next_y] = 1
                cnt += 1
    return cnt

for _ in range(T): 
    answer = []
    M, N, K = map(int, input().split(' '))
    matrix = [[0 for c in range(N)] for c in range(M)]
    for _ in range(K): 
        x, y = map(int, input().split(' '))
        matrix[x][y] = 1
    visited = [[0] * (N) for _ in range(M)]
    for i in range(M): 
        for j in range(N): 
            if (visited[i][j] == 0) & (matrix[i][j]==1): 
                visited[i][j] = 1 
                answer += [bfs(M, N, i, j, matrix, visited, 1)]
    print(len(answer))
