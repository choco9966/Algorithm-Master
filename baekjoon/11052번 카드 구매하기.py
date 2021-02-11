N = int(input())
DP = [0 for _ in range(N+1)]
CARDS = [0] + list(map(int, input().split(' ')))

for i in range(1, N+1):
    if i == 1: 
        DP[1] = CARDS[1]
    elif i == 2: 
        DP[2] = max(CARDS[1]*2, CARDS[2])
    else:
        DP[i] = CARDS[i]
        for j in range(1, 1+i//2):
            DP[i] = max(DP[i], DP[i-j]+DP[j])
print(DP[N])
