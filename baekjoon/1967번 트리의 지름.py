# 다익스트라 알고리즘 
## 참고 : https://www.acmicpc.net/problem/1167
## 다익스트라를 2번 적용해서 1에서 가장 먼 곳을 먼저 찾음 : idx 
## idx에서 가장 먼 곳을 찾아서 해당 거리를 출력
from collections import deque
import heapq, sys
# input = sys.stdin.readline
N = int(input())
graph = {v:{} for v in range(1, N+1)}
for _ in range(N-1):
    x, y, w = map(int, input().split())
    graph[x][y] = w
    graph[y][x] = w

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
