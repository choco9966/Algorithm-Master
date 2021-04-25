# 다익스트라 알고리즘 
## 다익스트라를 2번 적용해서 1에서 가장 먼 곳을 먼저 찾음 : idx 
## idx에서 가장 먼 곳을 찾아서 해당 거리를 출력
from collections import deque
import heapq, sys
input = sys.stdin.readline
N = int(input())
graph = {v:{} for v in range(1, N+1)}
for _ in range(N):
    mess = deque(list(map(int, input().split())))
    x = mess.popleft()
    while mess[0] != -1: 
        y = mess.popleft()
        w = mess.popleft() 
        graph[x][y] = w

def dijkstra(start):
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
    return distances

distances = dijkstra(1)
max_value = max(distances.values())
for key, value in distances.items():
    if value == max_value: 
        break

print(max(dijkstra(key).values()))

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
