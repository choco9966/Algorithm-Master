N = int(input())
arr = list(map(int, input().split(' ')))
DP = [1 for _ in range(N)]
for i in range(0, N):
    for j in range(i):
        if arr[j] < arr[i]:
            DP[i] = max(DP[i], DP[j]+1)
print(max(DP))
