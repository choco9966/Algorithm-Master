# 방법1. Dict 활용 
## 35948메모리	4600ms
N, M = map(int, input().split())
d, db = {}, {}

for _ in range(N):
    mess = input() 
    d[mess] =  1

for _ in range(M):
    mess = input() 
    if mess in d: db[mess] = 1 

print(len(db))
for i in sorted(db.keys()): 
    print(i)
 
# 방법2. Array 활용 
## 42324KB 4040ms
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
