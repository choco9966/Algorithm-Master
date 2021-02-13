# 트리의 지름 
## 메모리 초과로 다시 풀어야함 
from itertools import chain
from collections import deque
#import sys 
#input = sys.stdin.readline
N = int(input())
matrix = [[10001 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    mess = deque(list(map(int, input().split())))
    x = mess.popleft() - 1
    while mess[0] != -1: 
        y = mess.popleft() - 1
        w = mess.popleft() 
        matrix[x][y] = w

for k in range(0, N):
    for i in range(0, N):
        for j in range(0, N):
            if i == j: 
                matrix[i][j] = 0
            else:
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

result = 0
for i in range(N):
    for j in range(i, N):
        result = max(result, matrix[i][j])
print(result)
