# 다익스트라 알고리즘 
## pypy3으로 제출해야 통과함 
import heapq, sys
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
graph = {v:{} for v in range(1, V+1)}
for i in range(E):
    u, v, w = map(int, input().split())
    if v not in graph[u]: 
        graph[u][v] = w
    else:
        graph[u][v] = min(graph[u][v], w)
    
distances = {node: float('inf') for node in graph}
distances[start] = 0

queue = []
heapq.heappush(queue, [distances[start], start])
while queue:
    current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

    if distances[current_destination] < current_distance: 
        continue 
    
    for new_destination, new_distance in graph[current_destination].items():
        distance = current_distance + new_distance  
        if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
            distances[new_destination] = distance
            heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

for i, j in distances.items():
    if j != float('inf'): 
        print(j)
    else:
        print("INF")
        
# 메모리 초과 발생 코드 (플로이드 와샬)
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
