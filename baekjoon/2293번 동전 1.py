N, K = map(int, input().split())
coin = []
DP = [1] + [0 for _ in range(K)]

for i in range(N):
    coin.append(int(input()))

for c in coin:
    for i in range(c, K+1):
        DP[i] += DP[i-c]
print(DP[K])
