# 벨만-포드 알고리즘 
def BF(): 
    for i in range(1, N+1): 
        for j in range(1, N+1):
            for time, node in road[j]: 
                if dist[node] > time + dist[j]: 
                    dist[node] = time + dist[j] 
                    if i == N: 
                        print("YES")
                        return
    print("NO")
    return 

for _ in range(int(input())): 
    N, M, W = map(int, input().split())

    road = [[] for _ in range(N+1)]
    dist = [1e9] * (N+1)

    for _ in range(M): 
        S, E, T = map(int, input().split()) # S와 E는 연결된 지점의 번호, T는 이 도로를 통해 이동하는데 걸리는 시간
        road[S] += [(T, E)]
        road[E] += [(T, S)]
        
    for _ in range(W): 
        S, E, T = map(int, input().split()) # S는 시작 지점, E는 도착 지점, T는 줄어드는 시간
        road[S] += [(-T, E)]
    
    BF()
