# 풀이 : 다익스트라를 여러번 반복해서 결과를 더함 
from collections import deque
import heapq, sys
input = sys.stdin.readline
N, M, X = map(int, input().split())
graph = {v:{} for v in range(1, N+1)}
for _ in range(M):
    x, y, d = map(int, input().split())
    if y not in graph[x]: 
        graph[x][y] = d 
    else:
        graph[x][y] = min(graph[x][y], d) 

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

matrix = [[0 for _ in range(N)] for _ in range(N)]
for start in range(1, N+1):
    matrix[start-1] = list(dijkstra(start).values())

result = []
for i in range(1, N+1):
    result += [matrix[i-1][X-1] + matrix[X-1][i-1]]

print(max(result))
