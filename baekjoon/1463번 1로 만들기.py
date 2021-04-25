N = int(input())
DP = [0 for _ in range(10**6+1)]
DP[2] = DP[3] = 1
for i in range(4, 10**6+1): 
    if i % 2 == 0 and i % 3 == 0: 
        DP[i] = min(DP[i-1], DP[i//2], DP[i//3]) + 1
    else: 
        if i % 2 == 0: 
            DP[i] = min(DP[i-1], DP[i//2]) + 1
        elif i % 3 == 0: 
            DP[i] = min(DP[i-1], DP[i//3]) + 1
        else:
            DP[i] = DP[i-1] + 1
print(DP[N])
