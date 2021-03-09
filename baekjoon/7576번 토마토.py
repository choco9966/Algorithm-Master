# 7576번 : 토마토 
from collections import deque, Counter
from itertools import chain
import sys 

input = sys.stdin.readline # 속도 빠르게 검증하기 위한 용도 (입력속도를 빠르게함)

M, N = map(int, input().split())
# List Comprehension 사용시에 속도가 600ms 정도 향상 
matrix = [list(map(int, input().split())) for _ in range(N)]
    
tomatoes = deque([])
for i in range(N): 
    for j in range(M): 
        if matrix[i][j] == 1: 
            tomatoes += [(i, j, 0)]

while tomatoes: 
    tomato = tomatoes.popleft()
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for delta in deltas: 
        new_x, new_y = tomato[0] + delta[0], tomato[1] + delta[1]
        if 0 <= new_x < N and 0 <= new_y < M and matrix[new_x][new_y] == 0: 
            matrix[new_x][new_y] = 1
            tomatoes += [(new_x, new_y, tomato[2]+1)]

# Counter - Set의 경우 속도, 메모리 비슷 
if 0 not in set(chain(*matrix)): 
    print(tomato[2])
else: 
    print(-1)
