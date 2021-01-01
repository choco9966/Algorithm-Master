from collections import deque
from itertools import chain
import copy

def solution(m, n, infests, vaccinateds):
    '''
    BFS 이용 - 속도 초과 
    '''
    answer = 0
    infests = deque(infests)
    infested = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)] # 방문한 곳을 다시 방문할 이유가 없음 

    for i in infests: 
        infested[i[0]-1][i[1]-1] = 1

    for i in vaccinateds: 
        visited[i[0]-1][i[1]-1] = 1
        
    # 모든 직원이 백신 or 감염인 경우 탈출 
    cnt = 0
    while infests: 
        # 매일 작업 진행 
        for i in range(len(infests)): 
            candidate = infests.popleft()
            x, y = candidate[0], candidate[1]

            if visited[x-1][y-1] == 0: 
                visited[x-1][y-1] = 1
                infested, infests = bfs_virus(m, n, x, y, infested, infests, visited)
        
        if len(infests) != 0: 
            cnt += 1
            continue 
        else:
            if 0 in sum(visited, []): 
                return -1 
            else:
                return cnt
    return cnt

def bfs_virus(m, n, x, y, infested, infests, visited):
    DELTAS = ((0, 1),(0, -1),(1, 0),(-1, 0))
    for dx, dy in DELTAS:
        next_x, next_y = x + dx, y + dy
        
        # 백신이 아니고 테이블 안에 있는 경우 
        if 0 <= next_x-1 < m and 0 <= next_y-1 < n and visited[next_x-1][next_y-1] == 0 and infested[next_x-1][next_y-1] == 0:
            infested[next_x-1][next_y-1] = 1
            infests.append([next_x, next_y])
    return infested, infests


def solution(m, n, infests, vaccinateds):
    '''
    BFS 이용 - 속도 초과 
    '''
    answer = 0
    infested = [[0] * n for _ in range(m)]
    vacciend = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)] # 방문한 곳을 다시 방문할 이유가 없음 
    
    for i in infests: 
        infested[i[0]-1][i[1]-1] = 1
        
    for i in vaccinateds: 
        vacciend[i[0]-1][i[1]-1] = 1
        
    # 모든 직원이 백신 or 감염인 경우 탈출 
    cnt = 0
    infested_ = []
    while sum(list(chain(*infested))) + sum(list(chain(*vacciend))) != n*m: 
        before_infested = infested
        cnt += 1 
        for x in range(m):
            for y in range(n):
                if infested[x][y] == 1 and vacciend[x][y] == 0 and visited[x][y] == 0: 
                    visited[x][y] = 1
                    infested_.append(bfs_virus(m, n, x, y, infested, vacciend, visited))
                    
        # 매일의 감염자 현황 계산 
        for i in infested_:
            infested = matrix_element_wise_sum(infested, i)
            
        if before_infested == infested: 
            return -1 
    return cnt   

def bfs_virus(m, n, x, y, infested, vacciend, visited):
    infested_ = copy.deepcopy(infested)
    DELTAS = ((0, 1),(0, -1),(1, 0),(-1, 0))
    for dx, dy in DELTAS:
        next_x, next_y = x + dx, y + dy
        
        # 백신이 아니고 테이블 안에 있는 경우 
        if 0 <= next_x < m and 0 <= next_y < n and vacciend[next_x][next_y] != 1 and visited[next_x][next_y] != 1:
            infested_[next_x][next_y] = 1
    return infested_

def matrix_element_wise_sum(mat1, mat2): 
    sum_list_1 = []
    for i, j in zip(mat1, mat2): 
        sum_list_2 = [1 if a + b >= 1 else 0 for a, b in zip(i, j)]
        sum_list_1.append(sum_list_2)
    return sum_list_1


