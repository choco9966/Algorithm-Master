import sys
N = int(input())
DP = [0 for c in range(10**3+1)]
DP[1] = 1
DP[2] = 2
DP[3] = 4

case = []
for i in range(N): 
    case.append(int(sys.stdin.readline()))
    
for i in range(4, max(case)+1): 
    DP[i] = DP[i-3] + DP[i-2] + DP[i-1]

for i in case: 
    print(DP[i])