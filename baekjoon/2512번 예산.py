N = int(input())
arr = list(map(int, input().split())) 
K = int(input())

start, end = 1, max(arr) # 참고 : start를 min(arr)으로 잡았을 때 답을 탐지하지 못하는 경우도 있었음 

while start <= end: 
    mid = (start + end) // 2
    result = 0
    for i in arr:
        result += min(mid, i)
    
    if result <= K: 
        start = mid + 1
    else:
        end = mid - 1
print(end)
