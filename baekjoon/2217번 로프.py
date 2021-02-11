import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr = sorted(arr)

result = 0
for j in range(0, N):
    if result < arr[j] * (N-j):
        result = arr[j] * (N-j)
print(result)

# 참고 
# Combination을 이용한 완전 탐색 -> 메모리 에러 발생
from itertools import combinations 
import sys
N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

result = 0
for j in range(1, N+1):
    for k in list(combinations(arr, j)):
        if result < (min(k) * j):
            result = min(k) * j
print(result)
