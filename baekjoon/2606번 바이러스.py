# 방법1. 단순하게 matrix 활용하는 방법 
from collections import deque 
N = int(input())
myArray = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(int(input())): 
    n, m = map(int, input().split())
    myArray[n].append(m)
    myArray[m].append(n)

result = []
myQueue = deque(myArray[1])
visited[1] = True
while myQueue: 
    m = myQueue.popleft()
    result.append(m)
    visited[m] = True
    for n in myArray[m]: 
        if not visited[n] and n not in result: 
            myQueue.append(n)
            result.append(n)
            visited[n] = True
print(len(set(result)))

# 방법2. BFS 활용 

# 방법3. DFS 활용 
