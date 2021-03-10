DP = [0, 1, 2, 4]
for i in range(4, 11):
    DP += [DP[i-1] + DP[i-2] + DP[i-3]]
    
for _ in range(int(input())):
    print(DP[int(input())])
