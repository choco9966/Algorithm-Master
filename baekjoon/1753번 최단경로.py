# 메모리 초과 발생 코드 
from itertools import chain
from collections import deque
#import sys 
#input = sys.stdin.readline
N, M = map(int, input().split())
K = int(input())
matrix = [[10001 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    matrix[u-1][v-1] = min(matrix[u-1][v-1], w)

for k in range(0, N):
    for i in range(0, N):
        for j in range(0, N):
            if i == j: 
                matrix[i][j] = 0
            else:
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

for i in range(N):
    if matrix[K-1][i] != 10001: 
        print(matrix[K-1][i])
    else:
        print("INF")
