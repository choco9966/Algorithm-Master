from collections import deque
import heapq, sys
# input = sys.stdin.readline
N = int(input())
T = int(input())
graph = {v:{} for v in range(1, N+1)}
for _ in range(T):
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
                path[new_destination] = []
                for p in path[current_destination]:
                    path[new_destination].append(p)
                path[new_destination].append(new_destination)
    return distances

start, end = map(int, input().split())
path = [[] for _ in range(N+1)] 
path[start].append(start)

distances = dijkstra(start)
print(distances[end])
print(len(path[end]))
print(*path[end])
