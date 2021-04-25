n, s = map(int, input().split())
nums = list(map(int, input().split()))

interval_sum, end, length = 0, 0, n+1
for start in range(n): 
    while interval_sum < s and end < n: 
        interval_sum += nums[end]
        end += 1

    if interval_sum >= s: 
        length = min([length, end-start])
    
    interval_sum -= nums[start]
print(length if length != n+1 else 0)
