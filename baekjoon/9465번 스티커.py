# DP를 이용한 풀이 
## DP[0][i]의 경우 max(DP[1][i-1], DP[1][i-2]) 중 큰 값에 자기자신을 더한 값 
for _ in range(int(input())):
    n = int(input())
    DP = [list(map(int, input().split())) for _ in range(2)]
    DP[0][1] += DP[1][0]
    DP[1][1] += DP[0][0]

    for i in range(2, n): 
        DP[0][i] += max(DP[1][i-1], DP[1][i-2])
        DP[1][i] += max(DP[0][i-1], DP[0][i-2])

    print(max(DP[0][n-1], DP[1][n-1]))
