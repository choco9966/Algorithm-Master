N = int(input())
arr = list(map(int, input().split()))
if arr == sorted(arr, reverse=True): 
    print(-1)
else:
    find = False
    for i in range(N-1, 0, -1):
        if arr[i-1] < arr[i]: 
            for j in range(N-1, 0, -1):
                if arr[i-1] < arr[j]:
                    arr[i-1], arr[j] = arr[j], arr[i-1]
                    arr = arr[:i] + sorted(arr[i:])
                    find = True 
                    break
        if find: 
            print(*arr)
            break