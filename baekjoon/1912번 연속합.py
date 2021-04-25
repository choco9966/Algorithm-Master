N = int(input())
arr = list(map(int, input().split()))
DP = [arr[0]] + [0] * (N-1)
for i in range(1, N):
    DP[i] = max(DP[i-1] + arr[i], arr[i])
print(max(DP))
