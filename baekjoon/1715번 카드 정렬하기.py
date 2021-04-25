from heapq import heappush, heappop
import sys

N = int(input())
arr = []
for i in range(N):
    heappush(arr, int(sys.stdin.readline()))

result = 0
while len(arr) >= 2: 
    val = heappop(arr) + heappop(arr)
    result += (heappop(arr) + heappop(arr))
    heappush(arr, val)
print(result)
