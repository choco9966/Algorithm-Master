import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))
arr = sorted(arr, key = lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])
