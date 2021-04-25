# 배낭 알고리즘 
## DP를 이용해서 Row는 가치, Col은 무게로 구성 
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)] # N X N 행렬
DP = [[0 for _ in range(K+1)] for _ in range(N)] # N X K 행렬 

for i in range(N):
    for j in range(1, K+1):
        weight = arr[i][0]
        value = arr[i][1]
    
        if j < weight: 
            DP[i][j] = DP[i-1][j]
        else:
            DP[i][j] = max(value + DP[i-1][j-weight], DP[i-1][j])
print(DP[N-1][K])
