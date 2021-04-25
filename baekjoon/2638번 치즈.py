from collections import deque 
import sys 

input = sys.stdin.readline 
# input_file = open('./input/2638.txt', 'r')
# input = input_file.readline 

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

from itertools import chain
from copy import deepcopy 

deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def cheese(matrix, day): 
    queue = deque([(0, 0)])
    visited = [[0 for _ in range(M)] for _ in range(N)]    
    new_matrix = deepcopy(matrix)
    while queue: 
        x, y = queue.popleft()
        visited[x][y] += 1
        for delta in deltas:  
            new_x, new_y = x+delta[0], y+delta[1]
            if new_x >= 0 and new_x < N and new_y >= 0 and new_y < M: 
                if matrix[new_x][new_y] == 0 and visited[new_x][new_y] == 0 and (new_x, new_y) not in queue: 
                    queue += [(new_x, new_y)]
                else: 
                    # 첫방문인 경우에 대해서만 넣기 
                    if matrix[new_x][new_y] == 1 and visited[x][y] == 1:
                        visited[new_x][new_y] += 1
                        if visited[new_x][new_y] >= 2: 
                            new_matrix[new_x][new_y] = 0 
    '''
    for x in range(N): 
        print(new_matrix[x])
    print()
    '''
    return new_matrix, day 
    
from itertools import chain

day = 0
while sum(chain(*matrix)) != 0: 
    matrix, day = cheese(matrix, day+1)
print(day)
