n, m = map(int, input().split())
trees = list(map(int, input().split()))

s, e = 0, 2000000000
while s <= e: 
    mid = (s+e)//2
    left = sum([max(0, tree-mid) for tree in trees])
    if left >= m: 
        s = mid + 1
    else: 
        e = mid - 1
print(e)
