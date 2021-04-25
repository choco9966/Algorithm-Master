import sys
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
    # arr.append(int(input()))

result = 0
for i in sorted(arr, reverse=True):
    if M == 0: 
        break
    
    if i <= M:
        result += (M // i)
        M -= i*(M // i)
print(result)
