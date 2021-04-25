from itertools import combinations

N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
for i in list(combinations(arr, M)):
    print(' '.join(map(str, list(i))))
