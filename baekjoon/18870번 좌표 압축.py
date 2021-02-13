# 풀이 
## 1. SET을 이용해서 중복을 제거 
## 2. Dictionary를 이용해서 미리 순서를 계산 
N = int(input())
x = list(map(int, input().split()))

arr = sorted(set(x))
idx2num = {}
for i, j in enumerate(arr):
    idx2num[j] = i

for xi in x:
    print(idx2num[xi], end=' ')

# 시간 초과된 코드 
N = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
for i in arr:
    idx = sorted_arr.index(i)
    print(len(sorted_arr[0:idx]), end=' ')
