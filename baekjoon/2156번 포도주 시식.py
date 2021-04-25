N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))
DP = [0] + [0 for _ in range(N)]
# i <= n <= 10000 이므로 인덱스 에러를 방지하기위해서 1부터 시작 
for i in range(1, N+1):
    if i == 1: 
        DP[1] = arr[1]
    elif i == 2: 
        DP[2] = arr[1] + arr[2]
    else:
        # DP[i]의 Max값에는 자기 자신을 먹지 않은 경우도 포함해야함 
        DP[i] = max(DP[i-2] + arr[i], DP[i-3] + arr[i-1] + arr[i], DP[i-1])
print(max(DP))
