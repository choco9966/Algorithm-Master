import sys
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))

start, end = 1, max(arr)
while start <= end:
    num = (start + end)//2
    result = 0
    for lan in arr: 
        result += (lan // num)

    if result >= M: 
        start = num + 1
    else:
        end = num - 1
print(end)
