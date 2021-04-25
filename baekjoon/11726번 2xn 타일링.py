N = int(input())
DP = [0 for _ in range(1000+1)]
DP[1] = 1
DP[2] = 2 
for i in range(3, 1001): 
    DP[i] = DP[i-1] + DP[i-2]
print(DP[N] % 10007)
