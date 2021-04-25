import heapq, sys
input = sys.stdin.readline

def check(heap, visited):
    # 방문한 녀석들을 모두 제거 
    while heap and visited[heap[0][1]]: 
        heapq.heappop(heap)

    # 방문하지 않은 녀석을 만난경우 위의 while문이 종료되고 이때 그 다음 값을 제거 
    if heap: 
        visited[heap[0][1]] = True 
        heapq.heappop(heap)
    return heap, visited
    
for _ in range(int(input())):
    max_heap, min_heap = [], []
    visited = [False] * 10000001
    for n in range(int(input())): 
        a, b = map(str, input().split())
        if a == 'I':
            heapq.heappush(min_heap, (int(b), n))
            heapq.heappush(max_heap, (-int(b), n))
            
        else:
            if b == '-1': 
                min_heap, visited = check(min_heap, visited)
                
            else:
                max_heap, visited = check(max_heap, visited)
    # 마지막으로 방문한 내용 모두 제거    
    while min_heap and visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
        
    while max_heap and visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if min_heap and max_heap:
        print(max_heap[0][0] * -1, min_heap[0][0])
    else:
        print('EMPTY')
