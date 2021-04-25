N = int(input())
before = [0]
for _ in range(N): 
    now = list(map(int, input().split()))
    now[0] = now[0] + before[0]
    now[-1] = now[-1] + before[-1]
    for i in range(1, len(now)-1): 
        now[i] = max(now[i]+before[i-1], now[i]+before[i])
    before = now 
print(max(now))
