# 28776KB	116ms
from itertools import chain
def recursion(matrix, n): 
    global cnt1, cnt2 
    if sum(chain(*matrix)) == n**2: 
        cnt1 += 1
        return 
    
    elif sum(chain(*matrix)) == 0: 
        cnt2 += 1
        return 
    
    else: 
        # 1번째 사각형 
        recursion([c[0:n//2] for c in matrix[0:n//2]], n//2)
        
        # 2번째 사각형 
        recursion([c[n//2:] for c in matrix[0:n//2]], n//2)
        
        # 3번째 사각형 
        recursion([c[0:n//2] for c in matrix[n//2:]], n//2)
        
        # 4번째 사각형 
        recursion([c[n//2:] for c in matrix[n//2:]], n//2)
    
N = int(input())
matrix = [[] for _ in range(N)] 

for i in range(N): 
    matrix[i] = list(map(int, input().split()))
    
cnt1, cnt2 = 0, 0 
recursion(matrix, N)
print(cnt2)
print(cnt1)
