N, M = map(int, input().split())
arr1, arr2 = [], []
for i in range(N):
    arr1.append(str(input()))

for j in range(M):
    arr2.append(str(input()))
arr = sorted(set(arr1).intersection(set(arr2)))
print(len(arr))
for i in arr: 
    print(i)
